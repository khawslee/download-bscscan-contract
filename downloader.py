import asyncio
from bscscan import BscScan
import argparse
import json
import os
import shutil
import time

APIKEY = ""
CONTRACT = ""
FILENAME = ""

def parseandzip(parseText):
    # Extract only SourceCode
    sourceCode = parseText["SourceCode"]
    if sourceCode[0] == "{" and sourceCode[-1] == "}":
        # Remove head and tail curly brackets
        sourceCode = sourceCode[1:-1]
        # Json decode the source
        jsonSource = json.loads(sourceCode)
        # Extract List of source codes
        fullSource = jsonSource["sources"]
        
        # Remove existing folder if exist
        if os.path.exists(FILENAME) and os.path.isdir(FILENAME):
            shutil.rmtree(FILENAME)
        
        time.sleep(1)
        # Create a new folder
        os.mkdir(FILENAME)
        
        # Iterate each of source code in the dict
        for key in fullSource:
            # Extract the filename from key
            head, tail = os.path.split(key)
            # Create a new file using key as filename
            with open(FILENAME + "/" + tail, 'w', encoding="utf-8") as f:
                # Save the content in the new file
                f.write(fullSource[key]["content"])
    
        # Zip the folder using path as filename
        shutil.make_archive(FILENAME, 'zip', FILENAME)
    else:
        with open(FILENAME + ".sol", 'w', encoding="utf-8") as f:
            # Save the content in the new file
            f.write(sourceCode)
        

async def downContract():
    async with BscScan(APIKEY) as bsc:
        # Get the contract from Bscscan
        bsctext = await bsc.get_contract_source_code(contract_address = CONTRACT)
        return bsctext

# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-a", "--Apikey", help = "Bscscan API Key", required=True)
# Adding optional argument
parser.add_argument("-c", "--Contract", help = "Contract Address", required=True)
# Adding optional argument
parser.add_argument("-f", "--Filename", help = "Output Zip filename", required=True)
 
for arg, value in parser.parse_args()._get_kwargs():
    if value is not None:
        if arg == "Apikey":
            APIKEY = value
        elif arg == "Contract":
            CONTRACT = value
        elif arg == "Filename":
            FILENAME = value

if __name__ == "__main__":
    # Perform Asyn task to download the contract source code from Bscscan
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    returnbsctext = asyncio.run(downContract())
    # Parse and zip the contract source code
    parseandzip(returnbsctext[0])
<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Download BscScan contract</h3>

  <p align="center">
    <a href="https://github.com/khawslee/download-bscscan-contract">View Demo</a>
    ·
    <a href="https://github.com/khawslee/download-bscscan-contract/issues">Report Bug</a>
    ·
    <a href="https://github.com/khawslee/download-bscscan-contract/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This project use python bscscan library to download smart contract from https://bscscan.com/.

<p align="right">(<a href="#top">back to top</a>)</p>

### Python library

List of python's library used in the project,

* [bscscan](https://github.com/pcko1/bscscan-python), [asyncio](https://docs.python.org/3/library/asyncio.html), [argparse](https://docs.python.org/3/library/argparse.html), [json](https://docs.python.org/3/library/json.html), [shutil](https://docs.python.org/3/library/shutil.html), [time](https://docs.python.org/3/library/time.html), [os](https://docs.python.org/3/library/os.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.
First of all, you will need obtain your personal API key from bscscan.com, use it to download the smart contract from command line.

### Prerequisites

You are required to install required library before running the python script.

```sh
  pip install -r requirements.txt
```

## Usage

```properties
python downloader.py -a <API KEY> -c <Smart contract address> -f <Output filename>
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the Apache License Version 2.0. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Your Name - Siang Lee, Khaw - khawslee@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/khawslee/download-bscscan-contract.svg?style=for-the-badge
[contributors-url]: https://github.com/khawslee/download-bscscan-contract/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/khawslee/download-bscscan-contract.svg?style=for-the-badge
[forks-url]: https://github.com/khawslee/download-bscscan-contract/network/members
[stars-shield]: https://img.shields.io/github/stars/khawslee/download-bscscan-contract.svg?style=for-the-badge
[stars-url]: https://github.com/khawslee/download-bscscan-contract/stargazers
[issues-shield]: https://img.shields.io/github/issues/khawslee/download-bscscan-contract.svg?style=for-the-badge
[issues-url]: https://github.com/khawslee/download-bscscan-contract/issues
[license-shield]: https://img.shields.io/github/license/khawslee/download-bscscan-contract.svg?style=for-the-badge
[license-url]: https://github.com/khawslee/download-bscscan-contract/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/khawslee

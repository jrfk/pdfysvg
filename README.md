# pdfysvg

<img src="https://github.com/jrfk/pdfysvg/assets/5325478/a12ebfb3-ea56-4c93-85e8-1a1c73918d20" alt="pdfysvg logo" width="300" role="img">

[![PyPI - Version](https://img.shields.io/pypi/v/pdfysvg.svg)](https://pypi.org/project/pdfysvg)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pdfysvg.svg)](https://pypi.org/project/pdfysvg)

`pdfysvg` is a simple **CLI tool** that converts SVG files to PDF format. It leverages the Python libraries `svglib` and `reportlab` to perform the conversion efficiently.  
(This is a sample project using [Hatch](https://github.com/pypa/hatch), the Python project manager.)

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Installation

> [!WARNING]
> This project is not yet available on PyPI. The following instructions are for demonstration purposes only.

To install `pdfysvg`, simply run the following command in your terminal:

```console
pip install pdfysvg
```

## Usage
After installation, you can use pdfysvg directly from the command line. Here's how you can convert an SVG file to a PDF:

```console
pdfysvg input.svg -o output.pdf
```


### Options

- `-o`, `--output` Specify the output PDF file name and path.

## Dependencies

`pdfysvg` depends on the following libraries:
- **svglib**: Licensed under the GNU Lesser General Public License v3 (LGPLv3). Changes to `svglib` itself, if distributed, must also be shared under the LGPLv3. [svglib · PyPI](https://pypi.org/project/svglib/)
- **reportlab**: Licensed under the BSD License. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the copyright notice and this permission notice are included. [reportlab · PyPI](https://pypi.org/project/reportlab/)

## License

`pdfysvg` is distributed under the terms of the [MIT License](https://spdx.org/licenses/MIT.html).

## Contributing

Contributions to `pdfysvg` are welcome! Please refer to the repository's issues page on GitHub to propose new features or report bugs.

## Support

If you encounter any problems or have any suggestions, please open an issue on the GitHub repository or contact support via email.

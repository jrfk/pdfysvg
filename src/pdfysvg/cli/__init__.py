# SPDX-FileCopyrightText: 2024-present Junya Fukuda <junya.fukuda.e@gmail.com>
#
# SPDX-License-Identifier: MIT
from __future__ import annotations

import click

from pdfysvg.__about__ import __version__
from .main import pdfy_svg


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(version=__version__, prog_name="pdfysvg")
@click.argument("input_file", type=click.Path(exists=True))
@click.option("-o", "--output", "output_file", type=click.Path(), help="Output PDF file")
def pdfysvg(input_file: str, output_file: str | None = None):
    pdfy_svg(input_file, output_file)

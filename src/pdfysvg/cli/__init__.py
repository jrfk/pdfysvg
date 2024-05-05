# SPDX-FileCopyrightText: 2024-present Junya Fukuda <junya.fukuda.e@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from pdfysvg.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="pdfysvg")
def pdfysvg():
    click.echo("Hello world!")

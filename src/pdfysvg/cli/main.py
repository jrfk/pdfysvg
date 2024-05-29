from __future__ import annotations

import logging
import os

import click
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg


def pdfy_svg(input_file: str, output_file: str | None = None):
    """
    Convert an SVG file to PDF format.

    input_file: The path to the SVG file to be converted.
    output_file: The path to save the converted PDF file.
    """
    logging.getLogger("svglib").setLevel(logging.ERROR)

    if not output_file:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{base_name}.pdf"

    drawing = svg2rlg(input_file)
    renderPDF.drawToFile(drawing, output_file)

    click.echo(f"✨ Converted {input_file} to {output_file}")

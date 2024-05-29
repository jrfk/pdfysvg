import os
import pytest
from click.testing import CliRunner
from pdfysvg.cli import pdfysvg


@pytest.fixture
def temp_svg_file(tmp_path):
    # テスト用の一時的なSVGファイルを作成
    svg_content = """
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100">
        <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
    </svg>
    """
    file_path = tmp_path / "test.svg"
    with open(file_path, "w") as f:
        f.write(svg_content)
    return file_path


def test_pdfysvg(temp_svg_file, tmp_path):
    runner = CliRunner()
    pdf_file = tmp_path / "test.pdf"
    result = runner.invoke(pdfysvg, [str(temp_svg_file), "-o", str(pdf_file)])

    assert result.exit_code == 0, f"CLI exited with an error: {result.output}"
    assert os.path.exists(pdf_file), f"{pdf_file} was not created."

    # Clean up generated file
    if os.path.exists(pdf_file):
        os.remove(pdf_file)

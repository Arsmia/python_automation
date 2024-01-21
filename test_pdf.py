from PyPDF2 import PdfReader


def test_pdf():

    reader = PdfReader("docs-pytest-org-en-4.6.x.pdf")

    number_of_pages = len(reader.pages)
    text = reader.pages[0].extract_text()

    print(f"num of pages:{number_of_pages}")
    print(text)

    assert "holger krekel" in text
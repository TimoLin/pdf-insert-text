pdf_insert_text
==============
Insert the given text on each page in the user-defined position. For now the text is taken from the fisrt 6 characters of the PDF filename.

## Prerequisite
`Python 3.10` and `PyMuPDF`.

## How to use
1. Prepare the PDF files and put them to `files`.
2. Run the script at the root folder.
   ```sh
   python3 ./insertText.py
   ```
3. The processed PDF files locate at `outputs` folder.

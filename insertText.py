import fitz
import os
import io

def add_text_to_pdf(input_pdf_path, output_pdf_path, text, position=[290,40], font_size=12):
    '''
    :param input_pdf_path: Source pdf filename
    :param output_pdf_path: Output pdf filename
    :param text: Text to add on the header of each page
    :param position: Postion of the text
    :param font_size: Font size of the text
    :return: None
    '''

    # Papers
    position = [290, 40]
    # Patents
    position = [280, 25]
    # Exp.
    position = [280, 40]

    doc = fitz.open(input_pdf_path)

    # Relative position on a A4 size page
    ratioW = position[0]/590
    ratioH = position[1]/842

    for page in doc:
        # Position on the actual page
        x = page.rect.width*ratioW
        y = page.rect.height*ratioH

        # Insert the given text
        page.insert_text((x,y), text, font_size*int(page.rect.width/590), color=(0,0,0))

    # Output to a new file
    new_file = output_pdf_path
    doc.save(new_file)
    print(new_file)

# Function to process all PDF files in the folder
def process_pdfs_in_folder(folder_path, output_folder):
    '''
    :param folder_path: Source folder
    :param output_folder: Output folder
    :return: None
    '''
    os.makedirs(output_folder, exist_ok=True)

    # List all the files in the folder
    pdf_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        #if pdf_file[0:7] in ["B2-4-10","B2-4-11"]:
        #    text_to_add = pdf_file[0:7]
        #else:
        #    text_to_add = pdf_file[0:6]

        #text = pdf_file.split("-")[0:3]
        #text_to_add = "-".join(text)

        text_to_add = pdf_file[0:6]

        input_pdf_path = os.path.join(folder_path, pdf_file)
        output_pdf_path = os.path.join(output_folder, pdf_file)
        add_text_to_pdf(input_pdf_path, output_pdf_path, text_to_add)

# Example usage with Chinese characters in the folder and output folder
folder_path = './files'
output_folder = './outputs'

process_pdfs_in_folder(folder_path, output_folder)
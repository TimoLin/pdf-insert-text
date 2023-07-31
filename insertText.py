import fitz
import os
import io

def add_text_to_pdf(input_pdf_path, output_pdf_path, text, position=[290,40], font_size=12):

    # Papers
    position = [290,40]
    # Patents
    position = [280,25]

    # Exp.
    position = [280,40]
    doc = fitz.open(input_pdf_path)

    ratioW = position[0]/590
    ratioH = position[1]/842
    for page in doc:
        x = page.rect.width*ratioW
        y = page.rect.height*ratioH

        page.insert_text((x,y), text, font_size*int(page.rect.width/590), color=(0,0,0))

    new_file = output_pdf_path
    doc.save(new_file)
    print(new_file)

# Function to process all PDF files in the folder
def process_pdfs_in_folder(folder_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # List all the files in the folder
    pdf_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        #if pdf_file[0:7] in ["B2-4-10","B2-4-11"]:
        #    text_to_add = pdf_file[0:7]
        #else:
        #    text_to_add = pdf_file[0:6]
        text_to_add = pdf_file[0:6]
        #text = pdf_file.split("-")[0:3]
        #text_to_add = "-".join(text)
        print(text_to_add)
        input_pdf_path = os.path.join(folder_path, pdf_file)
        output_pdf_path = os.path.join(output_folder, pdf_file)
        add_text_to_pdf(input_pdf_path, output_pdf_path, text_to_add)

# Example usage with Chinese characters in the folder and output folder
folder_path = './files'  # Replace with the correct Chinese folder path
output_folder = './outputs'  # Replace with the correct Chinese output folder path

process_pdfs_in_folder(folder_path, output_folder)
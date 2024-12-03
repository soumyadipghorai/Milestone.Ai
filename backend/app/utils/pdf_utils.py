import fitz  # PyMuPDF
from markdownify import markdownify as md
import os
from _temp.config import PDF_UPLOAD_DIR, MD_STORE_DIR
import shutil 

class PDFBase : 
    def __init__(self, pdf_path:str = None, output_md_path: str = None, save_local: bool = True) -> None: 
        self.pdf_path = pdf_path
        self.output_md_path = output_md_path 
        self.save_local = save_local

    def pdf_to_markdown(self) -> bool: 
        try:
            pdf_document = fitz.open(self.pdf_path)
        except Exception as e:
            print(f"Error opening PDF file: {e}")
            return False 

        all_text = "" 
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text = page.get_text("text")
            all_text += f"\n\n## Page {page_num + 1}\n\n" + text

        pdf_document.close()

        markdown_text = md(all_text)
        try:
            with open(self.output_md_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)
            print(f"Markdown file saved as {self.output_md_path}")
            return markdown_text 
        except Exception as e:
            print(f"Error writing to Markdown file: {e}")

            return False 
        
class TextExtractorFromPDF(PDFBase) : 
    def __init__(self, pdf_file, unique_id: str = None) -> None:
        super().__init__()   
        self.pdf_file = pdf_file
        self.unique_id = unique_id

    def __create_folder(self) -> None : 
        if not os.path.exists(PDF_UPLOAD_DIR) : 
            os.makedirs(PDF_UPLOAD_DIR)

        if not os.path.exists(MD_STORE_DIR) : 
            os.makedirs(MD_STORE_DIR)

    def __save_pdf_file(self) -> None : 
        new_file_name = self.unique_id + "__" + self.pdf_file.filename
        self.pdf_path = os.path.join(PDF_UPLOAD_DIR, new_file_name)
        self.output_md_path = os.path.join(MD_STORE_DIR, "".join(new_file_name.split('.')[:-1])+'.md')
        
        with open(self.pdf_path, "wb") as buffer:
            shutil.copyfileobj(self.pdf_file.file, buffer)
            return True 
        return False 
    
    def extract(self) : 
        self.__create_folder() 
        if self.__save_pdf_file() : 
            return self.pdf_to_markdown(), self.pdf_path
        return False 

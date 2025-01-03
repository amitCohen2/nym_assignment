import os
from typing import Dict
import pdfplumber
from nym_assignment.extra_textual_word import PagesToExtraWords, ExtraTextualWord
from nym_assignment.textual_word import TextualWord, PagesToWords


class PdfLogic:
    @staticmethod
    def pdf_to_dict(pdfplumber_pdf: pdfplumber.PDF) -> dict:
        pdf_dict_result = {}

        for page_number, page in enumerate(pdfplumber_pdf.pages):
            page_words = []
            for word in page.extract_words():
                textual_word = TextualWord(
                    x0=float(word["x0"]),
                    x1=float(word["x1"]),
                    text=word["text"]
                )
                page_words.append(textual_word)

            pdf_dict_result[page_number] = page_words

        return pdf_dict_result

    @staticmethod
    def pdf_to_extra_dict(pdfplumber_pdf: pdfplumber.PDF) -> PagesToExtraWords:
        pdf_dict = {}

        for page_number, page in enumerate(pdfplumber_pdf.pages):
            page_words = []
            for word in page.extract_words(extra_attrs=['fontname', 'size']):
                textual_word = ExtraTextualWord(
                    x0=float(word["x0"]),
                    x1=float(word["x1"]),
                    text=word["text"],
                    fontname=word.get("fontname", ""),
                    size=float(word.get("size", 0))
                )
                page_words.append(textual_word)

            pdf_dict[page_number] = page_words

        return pdf_dict

    @staticmethod
    def process_pdf_directory(directory: str) -> Dict[str, PagesToWords]:
        result = {}

        # check if directory exists before proceeding
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory {directory} not found.")

        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory, filename)
                with pdfplumber.open(pdf_path) as pdf:
                    result[filename] = PdfLogic.pdf_to_extra_dict(pdf)

        return result

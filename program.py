from nym_assignment.chart_logic import ChartLogic
from nym_assignment.pdf_logic import PdfLogic


class Program:
    def __init__(self, pdf_dir: str):
        self.__pdf_dir = pdf_dir

    def run(self) -> None:
        pdf_dict = PdfLogic.process_pdf_directory(self.__pdf_dir)
        for pdf_name, page_to_words in pdf_dict.items():
            chart = ChartLogic.populate_chart(page_to_words)
            ChartLogic.print_chart_details(pdf_name, chart)


if __name__ == "__main__":
    files_path = input("please enter your pdf files path: ")
    try:
        program = Program(files_path)
        program.run()
    except FileNotFoundError as e:
        print(f"File Not Found Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

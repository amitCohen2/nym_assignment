from datetime import date, datetime
from nym_assignment.chart import Chart
from nym_assignment.textual_word import PagesToWords


class ChartLogic:
    @staticmethod
    def populate_chart(page_to_words: PagesToWords) -> Chart:
        name = ""
        dob = date(1900, 1, 1)  # default to this date to make sure this chart has wrong date format
        has_valid_ekg = False

        for page_number, words in page_to_words.items():
            words_text = " ".join([word.text for word in words])

            if "Patient Name:" in words_text:
                name_start = words_text.index("Patient Name:") + len("Patient Name:")
                name_end = words_text.find("DOB:", name_start)
                if name_end == -1:
                    name_end = len(words_text)
                name = words_text[name_start:name_end].strip()

            if "DOB:" in words_text:
                dob_start = words_text.index("DOB:") + len("DOB:") + 1
                dob_end = words_text.find(" ", dob_start)
                if dob_end == -1:
                    dob_end = len(words_text)
                dob_text = words_text[dob_start:dob_end].strip()
                try:
                    dob = datetime.strptime(dob_text, "%m/%d/%Y").date()
                except ValueError:
                    print(f"Invalid DOB format: {dob_text}, defaulting to 01/01/1900")

            if "EKG Results valid" in words_text:
                has_valid_ekg = True

        return Chart(name=name, dob=dob, has_valid_ekg=has_valid_ekg)

    @staticmethod
    def print_chart_details(filename: str, chart: Chart):
        print()
        print(f"Processed {filename}:")
        print(f"Name: {chart.name}")
        print(f"Dob: {chart.dob.strftime('%m/%d/%Y')}")
        print(f"Age: {chart.age:.2f}")
        print(f"Has Valid EKG: {chart.has_valid_ekg}")




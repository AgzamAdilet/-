from abc import ABC, abstractmethod
class Document(ABC):
    @abstractmethod
    def open(self):
        pass

class Report(Document):
    def open(self):
        print("Report document opened.")


class Resume(Document):
    def open(self):
        print("Resume document opened.")


class Letter(Document):
    def open(self):
        print("Letter document opened.")


class Invoice(Document):
    def open(self):
        print("Invoice document opened.")

class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self):
        pass

class ReportCreator(DocumentCreator):
    def create_document(self):
        return Report()


class ResumeCreator(DocumentCreator):
    def create_document(self):
        return Resume()


class LetterCreator(DocumentCreator):
    def create_document(self):
        return Letter()


class InvoiceCreator(DocumentCreator):
    def create_document(self):
        return Invoice()

def main():
    print("Choose document type:")
    print("1 - Report")
    print("2 - Resume")
    print("3 - Letter")
    print("4 - Invoice")

    choice = input("Your choice: ")

    creators = {
        "1": ReportCreator(),
        "2": ResumeCreator(),
        "3": LetterCreator(),
        "4": InvoiceCreator()
    }

    creator = creators.get(choice)

    if creator:
        document = creator.create_document()
        document.open()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()

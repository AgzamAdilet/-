from abc import ABC, abstractmethod

class FileSystemComponent(ABC):

    @abstractmethod
    def display(self, indent=0):
        pass

    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=0):
        print(" " * indent + f"Файл: {self.name} ({self.size} KB)")

    def get_size(self):
        return self.size


class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        if component not in self.children:
            self.children.append(component)
        else:
            print("Компонент уже существует!")

    def remove(self, component):
        if component in self.children:
            self.children.remove(component)
        else:
            print("Компонент не найден!")

    def display(self, indent=0):
        print(" " * indent + f"Папка: {self.name}")
        for child in self.children:
            child.display(indent + 2)

    def get_size(self):
        total = 0
        for child in self.children:
            total += child.get_size()
        return total



if __name__ == "__main__":
    file1 = File("file1.txt", 10)
    file2 = File("file2.txt", 20)
    file3 = File("file3.txt", 5)

    folder1 = Directory("Documents")
    folder2 = Directory("Images")
    root = Directory("Root")

    folder1.add(file1)
    folder1.add(file2)

    folder2.add(file3)

    root.add(folder1)
    root.add(folder2)

    root.display()

    print(f"\nОбщий размер: {root.get_size()} KB")

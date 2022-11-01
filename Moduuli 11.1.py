class Release:
    def __init__(self, release_name, person_name):
        self.release_name = release_name
        self.person_name = person_name

    def print_info(self):
        print(f"{self.release_name}")


class Magazine(Release):
    def __init__(self, release_name, person_name):
        super().__init__(release_name, person_name)

    def print_info(self):
        super().print_info()
        print(f"Päätoimittaja: {self.person_name}\n")


class Book(Release):
    def __init__(self, release_name, person_name, page_count):
        self.page_count = page_count
        super().__init__(release_name, person_name)

    def print_info(self):
        super().print_info()
        print(f"Kirjoittaja: {self.person_name}\nSivumäärä: {self.page_count}\n")


magazine1 = Magazine("Aku Ankka", "Aki Hyyppä")
book1 = Book("Hytti n:0 6", "Rosa Liksom", 2000)


magazine1.print_info()
book1.print_info()
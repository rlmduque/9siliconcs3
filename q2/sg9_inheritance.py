class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    @property
    def get_title(self):
        return self._title

    @property
    def get_author(self):
        return self._author

    @get_title.setter
    def set_title(self, title):
        self._title = title

    @get_author.setter
    def set_author(self, author):
        self._author = author

    def display_info(self):
        print(self._title)
        print(self._author)

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self._number_pages = number_pages

    @property
    def get_number_of_pages(self):
        return self._number_pages

    @get_number_of_pages.setter
    def set_number_of_pages(self, number_pages):
        if number_pages <= 0:
            print("The number of pages must be a positive number.")
        else:
            self._number_pages = number_pages

    def display_info(self):
        super().display_info()
        print(self._number_pages)

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self._issue_number = issue_number

    @property
    def get_issue_number(self):
        return self._issue_number

    @get_issue_number.setter
    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("The issue number must be a positive number.")
        else:
            self._issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(self._issue_number)

# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#Printing the information
print("")
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages = -310 #setting invalid value on attribute
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()
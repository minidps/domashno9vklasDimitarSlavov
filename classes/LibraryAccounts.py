class LibraryAccount:
    name = ""
    borrowed_book_names = []

    def borrow_book(self,book_name):
        if len(self.borrowed_book_names) > 5:
            print("You have reached the maximum amount of books you can borrow.")
        else:
            self.borrowed_book_names.append(book_name)

    def return_book(self,book_name):
        if len(self.borrowed_book_names) <= 0:
            print("There aren't any books to return!")
        elif book_name not in self.borrowed_book_names:
            print("That book is not borrowed.")
        else:
            self.borrowed_book_names.remove(book_name)

    def list_books(self):
        print(f"Borrowed books: {self.borrowed_book_names}")

user = LibraryAccount()
user.name = "Alex"
user.borrow_book("Mein Kampf")
user.borrow_book("1984")
user.borrow_book("Alice in Wonderland")
user.list_books()
user.return_book("Alice in Wonderland")
user.list_books()
user.return_book("50 Shades of Grey")
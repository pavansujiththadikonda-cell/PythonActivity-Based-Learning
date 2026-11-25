# Case Study 07: Library Book Management System

print("===== Library Book Management System =====")

books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_name = input("Enter book name: ")
        books.append(book_name)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)

    elif choice == "3":
        search_name = input("Enter book name to search: ")
        if search_name in books:
            print("Book found!")
        else:
            print("Book not found.")

    elif choice == "4":
        print("Thank you for using the Library System!")
        break

    else:
        print("Invalid choice. Please try again.")

print("========================================")
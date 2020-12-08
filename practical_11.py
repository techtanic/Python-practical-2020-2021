import pickle

try:
    with open("books.dat", "rb") as f:
        BOOKS = pickle.load(f)
except FileNotFoundError:
    BOOKS = []


def save():
    with open("books.dat", "wb") as f:
        pickle.dump(BOOKS, f)   


def insert_record():
    book = {}
    book["number"] = int(input("Book Number: "))
    book["name"] = input("Name: ")
    book["category"] = input("Category: ")
    book["page_count"] = int(input("Pages: "))
    book["price"] = float(input("Price: "))
    print()

    BOOKS.append(book)
    save()


def read_records(lst=BOOKS):
    for book in lst:
        print("Book Number:", book["number"])
        print("Name:", book["name"])
        print("Category:", book["category"])
        print("Pages:", book["page_count"])
        print("Price:", book["price"], "\n")


def get_sci_books():
    sci_books = []
    for book in BOOKS:
        if book["category"] == "sci":
            sci_books.append(book)
    read_records(sci_books)


def get_books_price_great():
    matching_books = []
    for book in BOOKS:
        if book["price"] > 200:
            matching_books.append(book)
    read_records(matching_books)



print("1: Insert Record")
print("2: Display All Records")
print("3: Display Books with Category 'sci'")
print("4: Display Books with Price > 200")
print("5: Exit\n")
while True:
    choice = int(input("Choice: "))
    print()

    if choice == 1:
        insert_record()
    elif choice == 2:
        read_records()
    elif choice == 3:
        get_sci_books()
    elif choice == 4:
        get_books_price_great()
    elif choice == 5:
        break

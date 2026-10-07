print("===================================================================================================")
print("_______________________________________LIBRARY MANAGEMENT SYSTEM___________________________________")
print("===================================================================================================")
search_book = {
    1:{
        "book":"syam chi aai",
        "release date":"20-09-2008",
        "pages":"200",
        "parts":"4",
        "status":"available"
    },
    2:{
        "book":"ramayn",
        "release date":"26-05-1988",
        "pages":"900",
        "parts":"2",
        "status":"issued"
    },
    3:{
        "book":"mahabharat",
        "release date":"02-04-1975",
        "pages":"800",
        "parts":"3",
        "status":"available"
    },
    4:{
        "book":"python",
        "release date":"05-06-2045",
        "pages":"6000",
        "parts":"15",
        "status":"available"
    },
    5:{
        "book":"java",
        "release date":"22-03-1906",
        "pages":"900",
        "parts":"20",
        "status":"issued"
    },
    6:{
        "book":"c++",
        "release date":"19-10-1966",
        "pages":"2000",
        "parts":"6",
        "status":"available"
    },
    7:{
        "book":"C",
        "release date":"14-04-2006",
        "pages":"400",
        "parts":"6",
        "status":"available"
    },
    8:{
        "book":"rudy",
        "release date":"31-08-1978",
        "pages":"900",
        "parts":"2",
        "status":"available"
    },
    9:{
        "book":"c##",
        "release date":"02-04-1945",
        "pages":"900",
        "parts":"9",
        "status":"available"
    },
    10:{
        "book":"javascript",
        "release date":"25-10-2035",
        "pages":"9000",
        "parts":"12",
        "status":"available"
    },

}

def search_book_search():
    book_id = int(input("Enter book id:"))
    if book_id in search_book:
        print("\nbook is found !")
        print("book:",search_book[book_id]["book"])
        print("release date:",search_book[book_id]["release date"])
        print("pages:",search_book[book_id]["pages"])
        print("parts:",search_book[book_id]["parts"])
    else:
        print("book is not found")
# 1. Show All Books (सभी पुस्तकें दिखाने क लिए)
def show_all_books():
  if not search_book:
    print("\nNo books available!")
    return

  print("\n--- All Books ---")
  for book_id, details in search_book.items():
    print("\nBook ID:", book_id)
    print("book:", details["book"])
    print("release date:", details["release date"])
    print("pages:", details["pages"])
    print("parts:", details["parts"])
    status = "Issued" if details.get("issued", False) else "Available"
    print("status:", status)


# 2. Issue Book (किताब इश्यू करने के लिए)
def issue_book():
  book_id = int(input("Enter book id to issue:"))
  if book_id in search_book:
    if not search_book[book_id].get("issued", False):
      search_book[book_id]["issued"] = True
      print(
          f"\nbook '{search_book[book_id]['book']}' is successfully issued !"
      )
    else:
      print("\nbook is already issued !")
  else:
    print("book is not found")


# 3. Show Issued Books (जो किताबें इश्यू हो चुकी हैं उन्हें देखने के लिए)
def show_issued_books():
  found = False
  print("\n------------------------------------- Issued Books -------------------------------------")
  for  book_id,details in search_book.items():
    if details.get("issued", False):
      print(f"\nBook ID:{book_id} | book: {details['book']}")
      found = True

    if not found:
        print("No books are currently issued.")

def add_book():
    book_id = int(input("Enter book id:"))
    book = input("Enter book name:")
    release_date = input("Enter release date:")
    pages = input("Enter pages:")
    parts = input("Enter parts:")
    status = input("Enter status:")

def delete_book():
  book_id = int(input("Enter book id to delete:"))
  if book_id in search_book:
    deleted_title = search_book[book_id]["book"]
    del search_book[book_id]
    print(f"\nbook '{deleted_title}' is deleted successfully !")
  else:
    print("book is not found")

while True:
    print("\n1. Search Book\n2. Show All Books\n3. Issued Books\n4. show issued books\n5. Add Book\n6. Delete Book\n7. Exit")

    choice = input("\nEnter your choice:")

    if choice == "1":
        search_book_search()
    elif choice == "2":
        show_all_books()
    elif choice == "3":
        issue_book()
    elif choice =="4":
       show_issued_books()
    elif choice == "5":
        add_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
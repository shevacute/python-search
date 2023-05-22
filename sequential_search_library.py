def is_similiar(title1, title2):
    title1 = title1.lower()
    title2 = title2.lower()
    
    if title1[0] == title2[0]:
        return True
    
    return False

def sequential_search(books, book_title):
    for book in books:
        if is_similiar(book['title'], book_title):
            return book['shelf']

    return "Buku tidak ditemukan"
books = [
    {'title': 'Python Programming','shelf':'A1'},
    {'title': 'Data Structures and Algorithms','shelf':'B2'},
    {'title': 'Inroduction to machine Learning','shelf':'C3'},
    {'title': 'Sequential Search and Binary Search','shelf':'D4'}
]

book_title = input("Masukkan judul buku yang ingin dicari: ")
shelf_location = sequential_search(books, book_title)
print(shelf_location)

bt1 = book_title.lower
print(bt1[0])
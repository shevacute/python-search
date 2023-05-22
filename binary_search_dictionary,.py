def binary_search_definition(dictionary, word):
    low = 0
    high = len(dictionary) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if dictionary[mid][0] == word:
            return dictionary[mid][1]
        elif dictionary[mid][0] < word:
            low = mid + 1
        else:
            high = mid - 1
    
    return None

# Kamus ajaib
dictionary = [
    ['Apple', 'Buah Apel'],
    ['Banana', 'Buah Pisang'],
    ['Cat', 'Kucing'],
    ['Duck', 'Bebek'],
    ['Elephant', 'Gajah']
]

# Mengurutkan kamus berdasarkan kata
dictionary.sort(key=lambda x: x[0])

word = input("Masukkan kata :")

# Mencari definisi kata menggunakan binary search
definition = binary_search_definition(dictionary, word)

# Menampilkan hasil
if definition:
    print(f"Definisi kata '{word}': {definition}")
else:
    print(f"Tidak ditemukan definisi untuk kata '{word}'")

def binary_search_insert_pos(data, target):
    low = 0
    high = len(data) - 1
    insert_pos = 0
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            insert_pos = mid + 1
            low = mid + 1
        else:
            insert_pos = mid
            high = mid - 1
    
    return insert_pos

# Daftar yang sudah diurutkan
data = [2, 4, 6, 8, 10, 12, 14]
target = 7

# Mencari posisi sisipan elemen menggunakan binary search
insert_position = binary_search_insert_pos(data, target)

# Menampilkan hasil
print(f"Elemen {target} dapat disisipkan pada indeks {insert_position} untuk menjaga daftar tetap terurut.")

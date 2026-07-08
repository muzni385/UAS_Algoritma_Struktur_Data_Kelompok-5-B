# Main Program  Restoran

from queue_stack import Queue, Stack
from bst import BST
from Binary_heap import BinaryHeap


# Inisialisasi Struktur Data
queue = Queue()
stack = Stack()
bst = BST()
heap = BinaryHeap()


# ID otomatis
id_pesanan_counter = 1


def tambah_pesanan():
    global id_pesanan_counter

    meja = int(input("Nomor Meja: "))
    nama_menu = input("Nama Menu: ")
    prioritas = int(input("Prioritas (1 = VVIP, 2 = VIP, 3 = Umum): "))

    data = {
        "id_pesanan": id_pesanan_counter,
        "meja": meja,
        "nama_menu": nama_menu,
        "prioritas": prioritas
    }

    queue.enqueue(data)
    bst.insert(data)
    heap.insert(data)

    print(f"\n✓ Pesanan berhasil dibuat dengan ID {id_pesanan_counter}")

    id_pesanan_counter += 1


def lihat_antrian():
    print("\n===== ANTREAN PESANAN =====")
    queue.display()


def lihat_semua_pesanan():
    print("\n===== DATA PESANAN (BST) =====")
    bst.inorder()


def cari_pesanan():
    id_pesanan = int(input("Masukkan ID Pesanan: "))
    bst.search(id_pesanan)


def proses_pesanan():
    pesanan = heap.delete_root()

    if pesanan is None:
        return

    bst.delete(pesanan["id_pesanan"])

    stack.push(pesanan)

    print("\n===== PESANAN DIPROSES =====")
    print(
        f"ID {pesanan['id_pesanan']} | "
        f"Meja {pesanan['meja']} | "
        f"{pesanan['nama_menu']}"
    )


def lihat_heap():
    print("\n===== PRIORITY HEAP =====")
    heap.display()


def lihat_riwayat():
    print("\n===== RIWAYAT PESANAN =====")
    stack.display()


def undo_pesanan():
    pesanan = stack.pop()

    if pesanan is None:
        return

    bst.insert(pesanan)
    heap.insert(pesanan)
    queue.enqueue(pesanan)

    print(
        f"\n✓ Pesanan ID {pesanan['id_pesanan']} "
        f"berhasil dikembalikan."
    )


def statistik_bst():
    print("\n===== STATISTIK BST =====")
    print(f"Jumlah Node : {bst.count_node()}")
    print(f"Tinggi Tree : {bst.height()}")


while True:

    print("\n")
    print("=" * 40)
    print(" SISTEM MANAJEMEN RESTORAN ")
    print("=" * 40)

    print("1. Tambah Pesanan")
    print("2. Lihat Antrean Pesanan")
    print("3. Lihat Semua Pesanan (BST)")
    print("4. Cari Pesanan")
    print("5. Proses Pesanan Prioritas Tertinggi")
    print("6. Lihat Priority Heap")
    print("7. Lihat Riwayat Pesanan")
    print("8. Undo Pesanan Terakhir")
    print("9. Statistik BST")
    print("0. Keluar")

    pilihan = input("\nPilih Menu: ")

    if pilihan == "1":
        tambah_pesanan()

    elif pilihan == "2":
        lihat_antrian()

    elif pilihan == "3":
        lihat_semua_pesanan()

    elif pilihan == "4":
        cari_pesanan()

    elif pilihan == "5":
        proses_pesanan()

    elif pilihan == "6":
        lihat_heap()

    elif pilihan == "7":
        lihat_riwayat()

    elif pilihan == "8":
        undo_pesanan()

    elif pilihan == "9":
        statistik_bst()

    elif pilihan == "0":
        print("\nTerima kasih telah menggunakan sistem restoran.")
        break

    else:
        print("\n✗ Pilihan tidak valid.")
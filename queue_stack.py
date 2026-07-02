
#queue, antrean pesanan masuk

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"✓ Pesanan '{data['nama_menu']}' dari Meja {data['meja']} masuk ke antrean.")

    def dequeue(self):
        if self.is_empty():
            print("✗ Antrean kosong, tidak ada pesanan yang bisa diproses.")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("✗ Antrean kosong.")
            return None
        return self.front.data

    def display(self):
        if self.is_empty():
            print("  Antrean kosong.")
            return
        current = self.front
        urutan = 1
        while current:
            p = current.data
            print(f"  {urutan}. Meja {p['meja']} | {p['nama_menu']} | Prioritas: {p['prioritas']}")
            current = current.next
            urutan += 1

# STACK - Riwayat Pesanan Selesai / Undo (LIFO)

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"✓ Pesanan '{data['nama_menu']}' dari Meja {data['meja']} dicatat ke riwayat.")

    def pop(self):
        if self.is_empty():
            print("✗ Riwayat kosong, tidak ada pesanan yang bisa di-undo.")
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("✗ Riwayat kosong.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("  Riwayat kosong.")
            return
        current = self.top
        urutan = 1
        while current:
            p = current.data
            print(f"  {urutan}. Meja {p['meja']} | {p['nama_menu']} | ID: {p['id_pesanan']}")
            current = current.next
            urutan += 1
# BINARY HEAP
# Untuk menentukan pesanan yang diproses lebih dulu berdasarkan prioritas

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    # mencari parent
    def parent(self, index):
        return (index - 1) // 2

    # mencari child kiri
    def left_child(self, index):
        return (2 * index) + 1

    # mencari child kanan
    def right_child(self, index):
        return (2 * index) + 2

    # INSERT
    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

        print(
            f"✓ Pesanan '{data['nama_menu']}' dari Meja {data['meja']} "
            f"ditambahkan ke Priority Heap."
        )

    # HEAPIFY UP
    def heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index]["prioritas"] < self.heap[parent_index]["prioritas"]:
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index]
                )
                index = parent_index
            else:
                break

    # DELETE ROOT
    def delete_root(self):
        if self.is_empty():
            print("✗ Heap kosong, tidak ada pesanan yang bisa diproses.")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return root

    # HEAPIFY DOWN
    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index

            left = self.left_child(index)
            right = self.right_child(index)

            if (
                left < size
                and self.heap[left]["prioritas"]
                < self.heap[smallest]["prioritas"]
            ):
                smallest = left

            if (
                right < size
                and self.heap[right]["prioritas"]
                < self.heap[smallest]["prioritas"]
            ):
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index]
                )

                index = smallest
            else:
                break

    # PEEK
    def peek(self):
        if self.is_empty():
            print("✗ Heap kosong.")
            return None

        return self.heap[0]

    # DISPLAY
    def display(self):
        if self.is_empty():
            print("  Heap kosong.")
            return

        print("  Daftar Pesanan berdasarkan Priority Heap:")

        for i, p in enumerate(self.heap, start=1):
            print(
                f"  {i}. ID {p['id_pesanan']} | "
                f"Meja {p['meja']} | "
                f"{p['nama_menu']} | "
                f"Prioritas: {p['prioritas']}"
            )
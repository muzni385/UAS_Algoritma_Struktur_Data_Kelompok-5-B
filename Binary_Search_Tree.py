#BST untuk mengurutkan data pesanan (menggunakan id)
class NodeBST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.jumlah_node = 0

    def is_empty(self):
        return self.root is None

#insert
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            self.jumlah_node += 1
            print(f"✓ Pesanan ID {data['id_pesanan']} ({data['nama_menu']}) masuk ke BST.")
            return NodeBST(data)

        if data['id_pesanan'] < node.data['id_pesanan']:
            node.left = self._insert(node.left, data)
        elif data['id_pesanan'] > node.data['id_pesanan']:
            node.right = self._insert(node.right, data)
        else:
            print(f"✗ ID Pesanan {data['id_pesanan']} sudah ada di BST, tidak bisa ditambah lagi.")
        return node

#search
    def search(self, id_pesanan):
        return self._search(self.root, id_pesanan)

    def _search(self, node, id_pesanan):
        if node is None:
            print(f"✗ Pesanan ID {id_pesanan} tidak ditemukan.")
            return None

        if id_pesanan == node.data['id_pesanan']:
            p = node.data
            print(f"✓ Ditemukan! ID {p['id_pesanan']} | Meja {p['meja']} | {p['nama_menu']}")
            return p
        elif id_pesanan < node.data['id_pesanan']:
            return self._search(node.left, id_pesanan)
        else:
            return self._search(node.right, id_pesanan)

#delete
    def delete(self, id_pesanan):
        self.root, berhasil = self._delete(self.root, id_pesanan)
        if berhasil:
            self.jumlah_node -= 1
            print(f"✓ Pesanan ID {id_pesanan} berhasil dihapus dari BST.")

    def _delete(self, node, id_pesanan):
        if node is None:
            print(f"✗ Pesanan ID {id_pesanan} tidak ditemukan, tidak bisa dihapus.")
            return node, False

        berhasil = False
        if id_pesanan < node.data['id_pesanan']:
            node.left, berhasil = self._delete(node.left, id_pesanan)
        elif id_pesanan > node.data['id_pesanan']:
            node.right, berhasil = self._delete(node.right, id_pesanan)
        else:
            berhasil = True
            if node.left is None and node.right is None:
                return None, berhasil
            elif node.left is None:
                return node.right, berhasil
            elif node.right is None:
                return node.left, berhasil
            else:
                pengganti = self._cari_terkecil(node.right)
                node.data = pengganti.data
                node.right, _ = self._delete(node.right, pengganti.data['id_pesanan'])

        return node, berhasil

    def _cari_terkecil(self, node):
        while node.left is not None:
            node = node.left
        return node

#inorder traversal
    def inorder(self):
        hasil = []
        self._inorder(self.root, hasil)

        if not hasil:
            print("  BST kosong, belum ada pesanan.")
            return

        print("  Daftar Pesanan urut berdasarkan ID (inorder traversal):")
        urutan = 1
        for p in hasil:
            print(f"  {urutan}. ID {p['id_pesanan']} | Meja {p['meja']} | {p['nama_menu']} | Prioritas: {p['prioritas']}")
            urutan += 1

    def _inorder(self, node, hasil):
        if node is not None:
            self._inorder(node.left, hasil)
            hasil.append(node.data)
            self._inorder(node.right, hasil)

#hitung tinggi tree
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        tinggi_kiri = self._height(node.left)
        tinggi_kanan = self._height(node.right)
        return 1 + max(tinggi_kiri, tinggi_kanan)

#hitung jumlah node
    def count_node(self):
        return self.jumlah_node
#BST untuk mengurutkan data pesanan (menggunakan id)
class NodeBST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.jumlah_node = 0

    def is_empty(self):
        return self.root is None

#insert
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            self.jumlah_node += 1
            print(f"✓ Pesanan ID {data['id_pesanan']} ({data['nama_menu']}) masuk ke BST.")
            return NodeBST(data)

        if data['id_pesanan'] < node.data['id_pesanan']:
            node.left = self._insert(node.left, data)
        elif data['id_pesanan'] > node.data['id_pesanan']:
            node.right = self._insert(node.right, data)
        else:
            print(f"✗ ID Pesanan {data['id_pesanan']} sudah ada di BST, tidak bisa ditambah lagi.")
        return node

#search
    def search(self, id_pesanan):
        return self._search(self.root, id_pesanan)

    def _search(self, node, id_pesanan):
        if node is None:
            print(f"✗ Pesanan ID {id_pesanan} tidak ditemukan.")
            return None

        if id_pesanan == node.data['id_pesanan']:
            p = node.data
            print(f"✓ Ditemukan! ID {p['id_pesanan']} | Meja {p['meja']} | {p['nama_menu']}")
            return p
        elif id_pesanan < node.data['id_pesanan']:
            return self._search(node.left, id_pesanan)
        else:
            return self._search(node.right, id_pesanan)

#delete
    def delete(self, id_pesanan):
        self.root, berhasil = self._delete(self.root, id_pesanan)
        if berhasil:
            self.jumlah_node -= 1
            print(f"✓ Pesanan ID {id_pesanan} berhasil dihapus dari BST.")

    def _delete(self, node, id_pesanan):
        if node is None:
            print(f"✗ Pesanan ID {id_pesanan} tidak ditemukan, tidak bisa dihapus.")
            return node, False

        berhasil = False
        if id_pesanan < node.data['id_pesanan']:
            node.left, berhasil = self._delete(node.left, id_pesanan)
        elif id_pesanan > node.data['id_pesanan']:
            node.right, berhasil = self._delete(node.right, id_pesanan)
        else:
            berhasil = True
            if node.left is None and node.right is None:
                return None, berhasil
            elif node.left is None:
                return node.right, berhasil
            elif node.right is None:
                return node.left, berhasil
            else:
                pengganti = self._cari_terkecil(node.right)
                node.data = pengganti.data
                node.right, _ = self._delete(node.right, pengganti.data['id_pesanan'])

        return node, berhasil

    def _cari_terkecil(self, node):
        while node.left is not None:
            node = node.left
        return node

#inorder traversal
    def inorder(self):
        hasil = []
        self._inorder(self.root, hasil)

        if not hasil:
            print("  BST kosong, belum ada pesanan.")
            return

        print("  Daftar Pesanan urut berdasarkan ID (inorder traversal):")
        urutan = 1
        for p in hasil:
            print(f"  {urutan}. ID {p['id_pesanan']} | Meja {p['meja']} | {p['nama_menu']} | Prioritas: {p['prioritas']}")
            urutan += 1

    def _inorder(self, node, hasil):
        if node is not None:
            self._inorder(node.left, hasil)
            hasil.append(node.data)
            self._inorder(node.right, hasil)

#hitung tinggi tree
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        tinggi_kiri = self._height(node.left)
        tinggi_kanan = self._height(node.right)
        return 1 + max(tinggi_kiri, tinggi_kanan)

#hitung jumlah node
    def count_node(self):
        return self.jumlah_node


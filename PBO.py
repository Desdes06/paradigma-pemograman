class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def get_luas(self):
        return 0.5 * self.alas * self.tinggi



segitiga1 = segitiga(7, 5)
print(segitiga1.get_luas())

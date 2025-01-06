class Pembayaran:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    @property
    def jumlah(self):
        return self._jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if nilai < 0:
            raise ValueError("Jumlah tidak boleh negatif")
        self._jumlah = nilai

    def tampilan(self):
        return f"Total Jumlah: Rp.{self.jumlah:,.2f}"

class Pembayaran_Tunai(Pembayaran):
    def __init__(self, jumlah, tp):
        super().__init__(jumlah)
        self.tp = tp 
    
    def tampilan(self):
        return f"Pembayaran Tunai - {self.tp} - {self.jumlah:,.2f}"


class Pembayaran_NonTunai(Pembayaran):
    def __init__(self, jumlah, pn):
        super().__init__(jumlah)
        self.pn = pn
    
    def tampilan(self):
        return f"Pembayaran Non Tunai - {self.pn} - {self.jumlah:,.2f}"


if __name__ == "__main__":
    jumlah_pembayaran = float(input("Masukkan Jumlah Pembayaran : Rp. "))
    tipe_pembayaran = input("Pilih Tipe Pembayaran (Tunai atau Non Tunai):")

    if tipe_pembayaran == "Tunai":
        tipe_tunai = input("Masukkan Tipe Tunai (Kertas, Koin): ")
        pembayaran = Pembayaran_Tunai(jumlah_pembayaran, tipe_tunai)
    elif tipe_pembayaran == "Non Tunai":
        tipe_nontunai = input("Masukkan Tipe Non Tunai (Qris, Debit, Credit): ")
        pembayaran = Pembayaran_NonTunai(jumlah_pembayaran, tipe_nontunai)
    else:
        print("Kesalahan Tipe Pembayaran. Mohon Pilih Tunai Atau Non Tunai.")
        exit()

    print("Detail Pembayaran:")
    print(pembayaran.tampilan())

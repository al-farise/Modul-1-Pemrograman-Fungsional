def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

def hitung_nilai_akhir(data_mahasiswa):
    data = {}

    for nama, nilai in data_mahasiswa.items():
        data[nama] = (nilai["UTS"] + nilai["UAS"]) / 2

    return data
# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
        "salman": {"UTS": 90, "UAS": 85 },
        "yaasir": {"UTS": 92, "UAS": 89 },
        "faiz": {"UTS": 89, "UAS": 81 },
        "daffa": {"UTS": 88, "UAS": 87 },
    }

    data_nilai_akhir = hitung_nilai_akhir(data_mahasiswa)  # Menghitung nilai akhir semua mahasiswa

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
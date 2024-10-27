import datetime
import math
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# ===========================================
#            Sistem Perhitungan Mesin
#          Banner dan Credit oleh NolepFy
# ===========================================

def banner():
    print("===========================================")
    print("                ___  ___  ______                       ")
    print("               / _ \\/ _ \\_  __/                       ")
    print("              / , _/ , _/ / /                          ")
    print("             /_/|_/_/|_| /_/                            ")
    print("===========================================")
    print("         Sistem Perhitungan Mesin          ")
    print("         Dikembangkan oleh NolepFy        ")
    print("===========================================\n")

# Kelas utama untuk konfigurasi mesin
class KonfigurasiMesin:
    def __init__(self, diameter_piston, langkah_piston):
        self.diameter_piston = diameter_piston
        self.langkah_piston = langkah_piston
        self.volume_silinder = self.hitung_volume_silinder()

    def hitung_volume_silinder(self):
        return (math.pi * (self.diameter_piston ** 2) / 4) * self.langkah_piston

# Kelas untuk perhitungan rasio kompresi
class RasioKompresi:
    def __init__(self, volume_silinder, volume_ruang_bakar):
        self.volume_silinder = volume_silinder
        self.volume_ruang_bakar = volume_ruang_bakar

    def hitung_kompresi(self):
        rasio = (self.volume_silinder + self.volume_ruang_bakar) / self.volume_ruang_bakar
        print(f"Rasio Kompresi: {rasio:.2f}")
        return rasio

# Kelas untuk memberikan informasi merek
class InfoMerek:
    def __init__(self):
        self.kelebihan = {
            "Yamaha": "Performa tinggi dan keandalan mesin.",
            "Honda": "Efisiensi bahan bakar dan kenyamanan berkendara.",
            "Suzuki": "Harga terjangkau dan biaya perawatan rendah.",
            "Kawasaki": "Desain sporty dan teknologi canggih.",
            "Scooter": "Mudah digunakan, efisiensi bahan bakar, dan kenyamanan berkendara."
        }
        self.kekurangan = {
            "Yamaha": "Biaya suku cadang mungkin lebih tinggi.",
            "Honda": "Kurang responsif dalam performa sport.",
            "Suzuki": "Kualitas material kadang kurang dibandingkan kompetitor.",
            "Kawasaki": "Perawatan mungkin lebih mahal.",
            "Scooter": "Performa mungkin tidak setinggi motor sport atau bebek."
        }

    def tampilkan_info(self, merek):
        merek = merek.capitalize()
        if merek in self.kelebihan:
            print(f"\nInformasi Merek {merek}:")
            print(f"Kelebihan: {self.kelebihan[merek]}")
            print(f"Kekurangan: {self.kekurangan[merek]}")
        else:
            print(f"\nInformasi tentang merek {merek} tidak tersedia.")

# Kelas untuk kalkulasi kecepatan piston
class KecepatanPiston:
    @staticmethod
    def hitung_kecepatan(rpm, langkah):
        kecepatan = (langkah / 1000) * (rpm / 60) * 2  # Kecepatan dalam m/s
        print(f"Kecepatan Piston: {kecepatan:.2f} m/s")
        return kecepatan

# Kelas untuk penyesuaian karburator
class PenyesuaianKarburator:
    @staticmethod
    def rekomendasi(volume_silinder):
        if volume_silinder > 200:
            print("Rekomendasi: Gunakan karburator dengan diameter lebih besar untuk meningkatkan aliran udara.")
        else:
            print("Rekomendasi: Karburator standar cukup untuk performa mesin ini.")

# Kelas untuk rekomendasi knalpot
class RekomendasiKnalpot:
    @staticmethod
    def rekomendasi(volume_silinder):
        if volume_silinder > 250:
            print("Rekomendasi: Gunakan knalpot racing untuk meningkatkan performa.")
        else:
            print("Rekomendasi: Knalpot standar sudah memadai untuk mesin ini.")

# Kelas untuk kalkulator mesin 4-tak
class Kalkulator4Tak:
    @staticmethod
    def fitur():
        print("\n=== Fitur Kalkulator 4 Tak ===")
        print("Pilih fitur yang ingin dihitung:")
        print("1. Volume mesin")
        print("2. Durasi dan LSA")
        print("3. Porting Polish, klep, lift, dan diameter")
        print("4. Pemilihan shim, rasio kompresi, piston speed")
        print("5. Batas aman RPM, ukuran ideal venturi, reamer")
        print("6. Akselerasi, potensi top speed, rasio final gear")

        while True:
            try:
                pilihan = int(input("Masukkan pilihan (1-6): "))
                if 1 <= pilihan <= 6:
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1-6.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

        if pilihan == 1:
            volume = float(input("Masukkan volume mesin (cc): "))
            print(f"Volume mesin: {volume:.2f} cc")
        elif pilihan == 2:
            durasi = float(input("Masukkan durasi (derajat): "))
            lsa = float(input("Masukkan LSA (derajat): "))
            print(f"Durasi: {durasi:.2f} derajat, LSA: {lsa:.2f} derajat")
        elif pilihan == 3:
            lift = float(input("Masukkan lift klep (mm): "))
            diameter = float(input("Masukkan diameter port (mm): "))
            print(f"Lift: {lift:.2f} mm, Diameter port: {diameter:.2f} mm")
        elif pilihan == 4:
            shim = float(input("Masukkan ukuran shim (mm): "))
            rasio_kompresi = float(input("Masukkan rasio kompresi: "))
            piston_speed = float(input("Masukkan kecepatan piston (m/s): "))
            print(f"Shim: {shim:.2f} mm, Rasio kompresi: {rasio_kompresi:.2f}, Kecepatan piston: {piston_speed:.2f} m/s")
        elif pilihan == 5:
            batas_rpm = float(input("Masukkan batas RPM: "))
            venturi_size = float(input("Masukkan ukuran venturi (mm): "))
            print(f"Batas aman RPM: {batas_rpm:.2f}, Ukuran venturi: {venturi_size:.2f} mm")
        elif pilihan == 6:
            akselerasi = float(input("Masukkan akselerasi (m/s²): "))
            top_speed = float(input("Masukkan potensi top speed (km/jam): "))
            rasio_final_gear = float(input("Masukkan rasio final gear: "))
            print(f"Akselerasi: {akselerasi:.2f} m/s², Potensi top speed: {top_speed:.2f} km/jam, Rasio final gear: {rasio_final_gear:.2f}")

# Kelas untuk kalkulator mesin 2-tak
class Kalkulator2Tak:
    @staticmethod
    def fitur():
        print("\n=== Fitur Kalkulator 2 Tak ===")
        print("Pilih fitur yang ingin dihitung:")
        print("1. Kapasitas volume mesin")
        print("2. Rasio kompresi dinamis")
        print("3. Clearance dan gap ring piston")
        print("4. Durasi mesin dan porting")
        print("5. Ukuran karburator dan akselerasi")

        while True:
            try:
                pilihan = int(input("Masukkan pilihan (1-5): "))
                if 1 <= pilihan <= 5:
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1-5.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")

        if pilihan == 1:
            volume_mesin = float(input("Masukkan volume mesin (cc): "))
            print(f"Kapasitas volume mesin: {volume_mesin:.2f} cc")
        elif pilihan == 2:
            rasio_kompresi_dinamis = float(input("Masukkan rasio kompresi dinamis: "))
            print(f"Rasio kompresi dinamis: {rasio_kompresi_dinamis:.2f}")
        elif pilihan == 3:
            clearance = float(input("Masukkan clearance (mm): "))
            gap_ring = float(input("Masukkan gap ring piston (mm): "))
            print(f"Clearance: {clearance:.2f} mm, Gap ring piston: {gap_ring:.2f} mm")
        elif pilihan == 4:
            durasi = float(input("Masukkan durasi (derajat): "))
            porting = float(input("Masukkan ukuran porting (mm): "))
            print(f"Durasi: {durasi:.2f} derajat, Ukuran porting: {porting:.2f} mm")
        elif pilihan == 5:
            ukuran_karburator = float(input("Masukkan ukuran karburator (mm): "))
            akselerasi = float(input("Masukkan akselerasi (m/s²): "))
            print(f"Ukuran karburator: {ukuran_karburator:.2f} mm, Akselerasi: {akselerasi:.2f} m/s²")

# Kelas untuk prediksi performa mesin menggunakan Machine Learning
class PrediksiPerformaMesin:
    def __init__(self, data_training):
        self.model = LinearRegression()
        self.data_training = data_training
        self.model.fit(data_training[['rpm', 'volume', 'kompresi']], data_training['performa'])

    def prediksi(self, rpm, volume, kompresi):
        fitur = np.array([[rpm, volume, kompresi]])
        prediksi_performa = self.model.predict(fitur)
        print(f"Prediksi Performa Mesin: {prediksi_performa[0]:.2f} HP")
        return prediksi_performa[0]

# Kelas untuk visualisasi performa mesin
class VisualisasiPerforma:
    def __init__(self, konfigurasi):
        self.konfigurasi = konfigurasi

    def plot_performa(self, rpm_range):
        rpm_values = np.linspace(rpm_range[0], rpm_range[1], 100)
        performa_values = [(rpm / 1000) * self.konfigurasi.volume_silinder for rpm in rpm_values]  # Dummy function
        plt.plot(rpm_values, performa_values, label="Performa Mesin")
        plt.xlabel("RPM")
        plt.ylabel("Performa (HP)")
        plt.title("Simulasi Performa Mesin Berdasarkan RPM")
        plt.legend()
        plt.grid()
        plt.show()

# Menjalankan sistem perhitungan
def main():
    banner()
    
    while True:
        print("Pilih opsi:")
        print("1. Dapatkan Saran untuk Meningkatkan Performa Mesin")
        print("2. Gunakan Alat Perhitungan Mesin")
        print("3. Kalkulator Mesin 2 Tak dan 4 Tak")
        print("4. Keluar")
        
        opsi = input("Masukkan pilihan (1, 2, 3, atau 4): ").strip()
        
        if opsi == "1":
            # Saran untuk meningkatkan performa mesin
            print("\nSaran untuk Meningkatkan Performa Mesin:")
            print("1. Tingkatkan rasio kompresi.")
            print("2. Sesuaikan karburator.")
            print("3. Ganti knalpot dengan knalpot racing.")
            print("4. Periksa dan sesuaikan camshaft.")
            print("5. Pertimbangkan penggunaan bahan bakar berkualitas tinggi.")
            print("6. Rutin lakukan perawatan mesin.")
            continue  # Kembali ke menu utama
        elif opsi == "2":
            while True:
                try:
                    diameter_piston = float(input("Masukkan diameter piston (mm): "))
                    langkah_piston = float(input("Masukkan panjang langkah piston (mm): "))
                    break
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")

            # Membuat objek konfigurasi mesin
            konfigurasi = KonfigurasiMesin(diameter_piston, langkah_piston)

            # Menampilkan informasi mesin
            print(f"\nVolume Silinder: {konfigurasi.volume_silinder:.2f} cc")

            # Input merek motor
            merek = input("Masukkan merek motor: ").strip()
            info_merek = InfoMerek()
            info_merek.tampilkan_info(merek)

            # Hitung kecepatan piston
            while True:
                try:
                    rpm = float(input("Masukkan RPM untuk menghitung kecepatan piston: "))
                    break
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")

            kecepatan_piston = KecepatanPiston.hitung_kecepatan(rpm, langkah_piston)

            # Penyesuaian karburator
            PenyesuaianKarburator.rekomendasi(konfigurasi.volume_silinder)

            # Rekomendasi knalpot
            RekomendasiKnalpot.rekomendasi(konfigurasi.volume_silinder)

            # Data training untuk model prediksi performa
            data_training = pd.DataFrame({
                'rpm': [5000, 6000, 7000, 8000, 9000],
                'volume': [konfigurasi.volume_silinder] * 5,
                'kompresi': [10, 10.5, 11, 11.5, 12],
                'performa': [20, 25, 27, 30, 32]
            })
            prediksi_performa = PrediksiPerformaMesin(data_training)

            # Input untuk prediksi performa
            while True:
                try:
                    rpm_prediksi = float(input("Masukkan RPM untuk prediksi performa: "))
                    kompresi = float(input("Masukkan rasio kompresi: "))
                    break
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")

            prediksi_performa.prediksi(rpm_prediksi, konfigurasi.volume_silinder, kompresi)

            # Visualisasi performa
            visualisasi = VisualisasiPerforma(konfigurasi)
            visualisasi.plot_performa((5000, 9000))
            continue  # Kembali ke menu utama
        elif opsi == "3":
            while True:
                jenis_mesin_input = input("Masukkan jenis mesin (2 tak/4 tak atau 2/4): ").strip().lower()
                
                if jenis_mesin_input in ["4 tak", "4"]:
                    Kalkulator4Tak.fitur()
                    break
                elif jenis_mesin_input in ["2 tak", "2"]:
                    Kalkulator2Tak.fitur()
                    break
                else:
                    print("Jenis mesin tidak valid. Pilih antara '2 tak', '4 tak', '2', atau '4'.")
            continue  # Kembali ke menu utama
        elif opsi == "4":
            print("Terima kasih telah menggunakan sistem ini!")
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

class EnerjiVerimliligiSimulatoru:
    def __init__(self):
        self.mevcut_tuketim = 0
        self.tasarruf_secenekleri = {
            "LED Ampuller": 0.6,
            "Akıllı Termostat": 0.15,
            "Yalıtım İyileştirmesi": 0.2,
            "Enerji Verimli Aletler": 0.25,
            "Güneş Panelleri": 0.4
        }
        self.secilen_secenekler = []

    def mevcut_tuketimi_al(self):
        while True:
            try:
                self.mevcut_tuketim = float(input("Mevcut aylık enerji tüketiminizi kWh cinsinden girin: "))
                if self.mevcut_tuketim <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Lütfen geçerli bir pozitif sayı girin.")

    def secenekleri_goster(self):
        print("\nEnerji Verimliliği Seçenekleri:")
        for i, (secenek, tasarruf) in enumerate(self.tasarruf_secenekleri.items(), 1):
            print(f"{i}. {secenek} (Tahmini Tasarruf: %{tasarruf*100:.0f})")

    def secenek_sec(self):
        while True:
            try:
                secim = int(input("\nBir seçenek numarası girin (veya çıkmak için 0): "))
                if secim == 0:
                    return False
                elif 1 <= secim <= len(self.tasarruf_secenekleri):
                    secenek = list(self.tasarruf_secenekleri.keys())[secim-1]
                    if secenek not in self.secilen_secenekler:
                        self.secilen_secenekler.append(secenek)
                        print(f"{secenek} seçeneği eklendi.")
                    else:
                        print("Bu seçenek zaten eklenmiş.")
                    return True
                else:
                    print("Geçersiz seçim. Lütfen tekrar deneyin.")
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

    def tasarrufu_hesapla(self):
        toplam_tasarruf_orani = sum(self.tasarruf_secenekleri[secenek] for secenek in self.secilen_secenekler)
        tasarruf_miktari = self.mevcut_tuketim * toplam_tasarruf_orani
        yeni_tuketim = self.mevcut_tuketim - tasarruf_miktari
        return tasarruf_miktari, yeni_tuketim, toplam_tasarruf_orani

    def sonuclari_goster(self):
        if not self.secilen_secenekler:
            print("\nHenüz hiçbir enerji verimliliği seçeneği seçilmedi.")
            return

        tasarruf_miktari, yeni_tuketim, toplam_tasarruf_orani = self.tasarrufu_hesapla()
        
        print("\n--- Simülasyon Sonuçları ---")
        print(f"Mevcut Aylık Tüketim: {self.mevcut_tuketim:.2f} kWh")
        print(f"Tahmini Yeni Aylık Tüketim: {yeni_tuketim:.2f} kWh")
        print(f"Aylık Enerji Tasarrufu: {tasarruf_miktari:.2f} kWh")
        print(f"Toplam Tasarruf Oranı: %{toplam_tasarruf_orani*100:.2f}")
        print("\nSeçilen Enerji Verimliliği Önlemleri:")
        for secenek in self.secilen_secenekler:
            print(f"- {secenek}")

    def calistir(self):
        print("Enerji Verimliliği Simülatörüne Hoş Geldiniz!")
        self.mevcut_tuketimi_al()
        
        while True:
            self.secenekleri_goster()
            if not self.secenek_sec():
                break
            self.sonuclari_goster()

        print("\nSimülasyon tamamlandı. Teşekkür ederiz!")

if __name__ == "__main__":
    simulator = EnerjiVerimliligiSimulatoru()
    simulator.calistir()
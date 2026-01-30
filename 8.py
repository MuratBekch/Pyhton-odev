class Question:
    """Soru kalıbını oluşturan sınıf"""
    def __init__(self, text, choices, answer):
        self.text = text        # Sorunun metni
        self.choices = choices  # Şıklar (liste)
        self.answer = answer    # Doğru cevap metni
        
    def cevapKontrolu(self, answer):
        """Kullanıcının verdiği cevabı doğru cevapla karşılaştırır"""
        return self.answer == answer

class Quiz:
    """Quiz akışını ve skor tablosunu yöneten sınıf"""
    def __init__(self, questions):
        self.questions = questions      # Soru nesnelerinden oluşan liste
        self.score = 0                  # Başlangıç skoru
        self.questionIndex = 0          # Kaçıncı soruda olduğumuzu tutar

    def soruGetir(self):
        """Aktif olan soru nesnesini döndürür"""
        return self.questions[self.questionIndex]

    def soruGoster(self):
        """Soruyu ekrana yazdırır ve kullanıcıdan girdi alır"""
        question = self.soruGetir()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for choice in question.choices:
            print("- " + choice) # Şıkları listeler
            
        cevap = input("Cevabınız: ")
        self.tahmin(cevap)
        self.soruYukle()

    def tahmin(self, answer):
        """Cevabı kontrol eder, skoru ve indexi günceller"""
        question = self.soruGetir()
        
        if question.cevapKontrolu(answer):
            self.score += 1
            print("Doğru!")
        else:
            print(f"Yanlış! Doğru cevap: {question.answer}")
            
        self.questionIndex += 1 # Bir sonraki soruya geç

    def soruYukle(self):
        """Soruların bitip bitmediğini kontrol eder"""
        if len(self.questions) == self.questionIndex:
            self.ilerlemeGoster()
            self.showScore()
        else:
            self.soruGoster()
    
    def showScore(self):
        """Final skorunu yazdırır"""
        print(f"Quiz Bitti! Toplam Puan: {self.score}")

    def ilerlemeGoster(self):
        """İlerleme durumunu görsel olarak belirtir"""
        print(" Sonuçlar Hesaplanıyor ".center(50, "*"))

# --- Uygulama Bölümü ---
s1 = Question("Dünyanın en güçlü ülkesi hangisidir?", ["ABD", "İngiltere", "Rusya", "Türkiye"], "ABD")
s2 = Question("İstanbul hangi bölgededir?", ["Doğu Anadolu", "Marmara Bölgesi", "Ege"], "Marmara Bölgesi")
s3 = Question("Elektrik ile en çok hangi mühendislik uğraşır?", ["Elektrik mühendisliği", "Jeoloji", "Makine"], "Elektrik mühendisliği")

soru_listesi = [s1, s2, s3]
quiz = Quiz(soru_listesi)

# Quizi başlat
quiz.soruGoster()
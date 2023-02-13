import random

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Girilen cevap şıklar arasında yok!")
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex = 0
        self.score = 0
        
    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)
        
        answer = input("Cevap: ")
        if (question.checkAnswer(answer)):
            self.score += 1
            print("Tebrikler! Doğru cevap")
        else:
            print(f"'{answer}' yanlış cevap")
        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            # print(f"Quizi tamamladınız. Skorunuz: {self.score}")
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayScore(self):
        print("Test özetiniz".center(100,"*"))
        point = 100 / len(self.questions)
        totalPoint = round(self.score * point)
        print(f"Toplam {len(self.questions)} sorunun {self.score} tanesini doğru cevapladınız")
        print(f"Quizi tamamladınız. Skorunuz: {totalPoint}")
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız. K.G".center(100,"*"))

q1 = Question("'Beni öldürmeyen acı güçlendirir' hangi ünlü düşünürün sözüdür?",["freud","marx","nietzsche"],"nietzsche")

q2 = Question("'Açlık' kitabının yazarı ünlü romancı kimdir?",["gabriel garcia marquez","knut hamsun","jose saramago"],"knut hamsun")

q3 = Question("'AK-47' olarak da bilinen silahı kim bulmuştur?",["mikhail kalashnikov","svetoslav todorov","mihail gorbaçov"],"mikhail kalashnikov")

q4 = Question("'Aspirin' ilk kez hangi yılda satışa çıkmıştır?",["1937","1899","1915"],"1899")

q5 = Question("'Calamity Jane' karakteri hangi çizgi romanda geçer?",["tentenin maceraları","red kit","mister no"],"red kit")

q6 = Question("'Davut Yıldızı' hangi dinin sembolüdür?",["budizm","hristiyanlık","musevilik"],"musevilik")

q7 = Question("24 yaşında hayatını kaybeden James Dean'in ölüm sebebi nedir?",["Trafik Kazası","Suikast","Kalp Krizi"],"Trafik Kazası")

q8 = Question("4 hafta kaç gün eder?",["16","28","25"],"28")

q9 = Question("50 Amerikan Doları'nın üzerinde kimin resmi bulunur?",["Ulysses S. Grant","Alexander Hamilton","Thomas Jefferson"],"Ulysses S. Grant")

q10 = Question("AB standartlarına göre IBAN numarasında en fazla kaç adet rakam olabilir?",["34","22","16"],"34")

q11 = Question("AB üyeliği kabul edilen, nüfusunun çoğunluğu Müslüman olan toprak hangisidir?",["Lübnan","Mayotte Adası","Türkiye"],"Mayotte Adası")

q12 = Question("Antik Yunan'da kadın ve erkeklerin vazgeçilmez kıyafeti neydi?",["Kazakh","Khiton","Kashmir"],"Khiton")

q13 = Question("Arap alfabesi hangi yönde okunur?",["Sağdan Sola","Soldan Sağa","Ortadan Yukarı"],"Sağdan Sola")

q14 = Question("Arjantin bayrağında hangi figür bulunmaktadır?",["Güneş","Kılıç","Kilise"],"Güneş")

q15 = Question("Bir tiyatro oyununda, kişilerden birinin kendi kendine yaptığı konuşmaya ne denir?",["Diyalog","Monolog","Sohbet"],"Monolog")

q16 = Question("Bir ülkenin para biriminin diğer dövizler karşısında değerinin düşürülmesine ne denir?",["Reasürans","Devalüasyon","Deflasyon"],"Devalüasyon")

q17 = Question("Bir yılda kaç ay 30 günden oluşmaktadır?",["5","4","6"],"4")

q18 = Question("Dünya'nın 7 Harikası'ndan biri olan 'Halikarnas Mozolesi' nerededir?",["İtalya","Türkiye","Mısır"],"Türkiye")

q19 = Question("Dünyanın en büyük elmaslarından biri olan 'Star of Sierra Leone' kaç karattır?",["802.5","968.9","552.3"],"968.9")

q20 = Question("Dünyanın en büyük gölü hangisidir?",["Hazar","Lut","Malavi"],"Hazar")

q21 = Question("Dünyanın en büyük patates üreticisi hangi ülkedir?",["Paraguay","Bolivya","Çin"],"Çin")

q22 = Question("Geminin en önde kalan baş kısmına ne ad verilir?",["Bandıra","Küpeşte","Pruva"],"Pruva")

q23 = Question("Genç yaşta milyarder olan girişimci Evan Spiegel hangi uygulamanın sahibidir?",["Instagram","Facebook","Snapchat"],"Snapchat")

q24 = Question("Genellikle ağaçtan yapılan ve bebekleri sallayarak uyutmaya yarayan küçük yatak hangisidir?",["Yürüteç","Beşik","Ana kucağı"],"Beşik")

q25 = Question("Gerçekte olmuş gibi kuşaktan kuşağa aktarılan sözlü ya da yazılı anlatılara ne ad verilir?",["Roman","Efsane","Drama"],"Efsane")

q26 = Question("Hangi filozof modern felsefenin babası olarak kabul edilir?",["René Descartes","Karl Marx","Immanuel Kant"],"René Descartes")

q27 = Question("Hangi geometrik şeklin daha fazla kenarı vardır?",["Heptagon","Üçgen","Beşgen"],"Heptagon")

q28 = Question("Hangi giyim markası diğerlerinden daha önce kurulmuştur.",["Zara","Marks and Spencer","Mango"],"Marks and Spencer")

q29 = Question("Hangi havayolu şirketinin filosunda dünyanın en büyük yolcu uçağı olan Airbus A380 yoktur?",["Turkish Airlines","China Southern","Lufthansa"],"Turkish Airlines")

q30 = Question("Bir yolun kıvrıldığı yere ne denir?",["Geçit","Viraj","Varil"],"Viraj")

questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30]

quiz = Quiz(questions)

quiz.loadQuestion()

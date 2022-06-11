import random

# result = dir(random)
# result = help(random)

# 100 e kadar olan sayılardan rastgele küsüratlı bir sayı üretir
result = random.random() * 100

# 100 e kadar olan sayılardan rastgele küsüratsız bir sayı üretir
result = int(random.uniform(10,100))

names = ["ali","yağmur","deniz","cenk","ahmet","efe"]
greeting = "hello there"

# names listesinden sayıya göre rastgele bir isim seçer
result = names[random.randint(0,len(names)-1)]

# names listesinden rastgele bir isim seçer
result = random.choice(names)

# greeting listesindeki yazının harflerini tek tek gösterir
result = random.choice(greeting)

# 0 dan 10 a kadar rastgele bir sayı üretir
liste = list(range(10))
random.shuffle(liste)
result = liste


liste = range(100)

# 0 dan 100 e kadar rastgele 3 sayı üretir
result = random.sample(liste,3)

# names listesinden rastgele 2 ismi seçer
result = random.sample(names,2)



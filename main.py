import string
lista=[]

liczba_dokumentow = int(input())
dokumenty = []

for dok in range(liczba_dokumentow):
  dok = input()
  dokumenty.append(dok)

zapytania = []
liczba_zapytan = int(input())
for zap in range(liczba_zapytan):
  zap = input()
  zapytania.append(zap)

for zapytanie in zapytania: 
  interpunkcje = string.punctuation
  wynik=[]
  s={}
  for num,dok in enumerate(dokumenty):
    for i in interpunkcje:
      dok=dok.replace(i, "")

    dok=dok.replace(" ", " ")
    tokeny=dok.lower().strip().split()
    if zapytanie in tokeny: 
      s[num]=tokeny.count(zapytanie)

  for w in sorted(s, key=s.get, reverse=True):
    wynik.append(w)

  print(wynik)

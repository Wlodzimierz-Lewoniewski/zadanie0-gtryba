import string

liczba_dokumentow = int(input())
dokumenty = []

for dok in range(liczba_dokumentow):
  dokument = input().strip()
  dokumenty.append(dokument)

zapytania = []
liczba_zapytan = int(input())
for zap in range(liczba_zapytan):
  zapyt = input().strip()
  zapytania.append(zapyt)

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

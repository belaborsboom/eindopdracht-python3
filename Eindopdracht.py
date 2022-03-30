totale_prijs = 0
prijsboodschap = 0
lijst = ()
lijst2 = ()

def aanmaken(dic):
  print("als jij een boodschappenlijstje maakt met de prijzen erbij reken ik uit hoeveel het kost")
  keuze1 = int(input("hoeveel dingen zitten er op het lijstje? "))
  for i in range(keuze1):
    a = i + 1
    keuze2 = input("wat is het " + str(a) + "e boodschap? (graag niet een boodschap herhalen) ")
    keuze3 = input("en wat is de prijs? ")
    dic[keuze2] = keuze3

def zien(dic):
  global totale_prijs
  vraag = input("wil je zien wat er in je boodschappenlijstje zit? ").lower()
  if vraag == "ja":
    print(dic)
  elif vraag == "nee":
    print("ok dan niet")
  else:
    print("dat is geen antwoord")

  values = dic.values()
  lijst = list(values)
  for i in range(len(lijst)):
    totale_prijs = totale_prijs + int(lijst[i])
  vraag2 = input("wil je ook weten wat de totale prijs is? ").lower()
  if vraag2 == "ja":
    print(totale_prijs, "euro")
  elif vraag2 == "nee":
    print("ok dan niet")
  else:
    print("dat is geen antwoord")

def toevoegen(dic):
  vraag3 = input("wil je een boodschap toevoegen? ").lower()
  if vraag3 == "ja":
    print("dit is je boodschappenlijstje nu: ")
    print(dic)
    keuze4 = input("zeg nu de volgende boodschap (niet eentje herhalen) ")
    keuze5 = input("en wat is de prijs? ")
    dic[keuze4] = keuze5
    print("dit is je boodschappenlijstje nu:")
    print(dic)
  elif vraag3 == "nee":
    print("ok dan niet")
  else:
    print("dat is geen antwoord")

def boodschappen(dic, dic2):
  global prijsboodschap
  print("Ik laat nu zien wat er allemaal op je lijstje staat en moet je kiezen welke je koopt en dan laat ik zien hoeveel dat kost")
  print(dic)
  vraag6 = input("Zeg nu de nummers van de boodschappen die je wil kopen.(voorbeeld als je de eerste en de twede wil kopen typ je 12) ")
  for i in range(len(vraag6)):
    nummer = int(vraag6[i]) - 1
    key1 = list(dic)[nummer]
    value123 = list(dic.values())[nummer]
    dic2[key1] = value123
  values2 = dic2.values()
  lijst2 = list(values2)
  for i in range(len(lijst2)):
    prijsboodschap = prijsboodschap + int(lijst2[i])
    print(lijst2[i])
    print(prijsboodschap)
  print("De prijs voor de boodschappen die jij hebt gekozen is " + str(prijsboodschap))

def wijzigen(dic):
  print(dic)
  vraag7 = input("Welke wil je veranderen? (als je de eerste wil veranderen dat typ je 1 etc.) ")
  number = int(vraag7) - 1
  key2 = str(list(dic)[number])
  vraag8 = input("Wil je het product veranderen of de prijs? ")
  if vraag8 == "product":
    vraag9 = input("Wat wordt de nieuwe naam")
    dic[vraag9] = dic[key2]
  elif vraag8 == "prijs":
    vraag10 = input("Wat wordt de nieuwe prijs? ")
    dic[key2] = vraag10
  else:
    print("Wtf is dat voor antwoord je moet product of prijs invullen")

def echt_stoppen():
  vraag4 = input("wil je stoppen? ").lower()
  if vraag4 == "ja":
    print("ok ik stop hem")
  elif vraag4 == "nee":
    return False
  else:
    print("dat was geen antwoord, ik stop het zelf wel")

  return True

def menu():
  done = False
  dic = {}
  dic2 = {}
  while done == False:
    # boodschappen()
    print("wat wil je doen?")
    if not dic == {}:
      keuzes = "zien, toevoegen, boodschappen, wijzigen of stop "
    elif dic == {}:
      keuzes = "aanmaken of stop "
    vraag5 = input("je kan kiezen uit, " + keuzes).lower()
    if vraag5 == "aanmaken":
      aanmaken(dic)
    elif vraag5 == "zien":
      zien(dic)
    elif vraag5 == "stop":
      if echt_stoppen():
        done = True
    elif vraag5 == "toevoegen":
      toevoegen(dic)
    elif vraag5 == "boodschappen":
      boodschappen(dic, dic2)
    elif vraag5 == "wijzigen":
      wijzigen(dic)


menu()

totale_prijs = 0
prijsboodschap = 0
lijst = ()
lijst2 = ()
dic = {}
dic2 = {}

def aanmaken(dict):
  global dic
  print("Normaal zou ik nu alle boodschappen die je kan kopen laten zien maar je kan ook zelf een assortiment aan boodschappen maken.")
  keuze0 = input("Wil je zelf een assortiment maken? ").lower()
  if keuze0 == "ja":
    keuze1 = int(input("hoeveel dingen zitten er op het lijstje? "))
    if not keuze1 == "":
      for i in range(keuze1):
        a = i + 1
        keuze2 = input("wat is het " + str(a) + "e boodschap? (graag niet een boodschap herhalen) ")
        keuze3 = input("en wat is de prijs? ")
        dict[keuze2] = keuze3
    else:
      print("Ik vroeg hoeveel dingen er op zaten")
  elif keuze0 == "nee":
    dic = {"brood": 2, "water": 1, "sap": 3}
    print("Ok dan is je assortiment nu dit: " + str(dic))
  else:
    print("Dat is geen antwoord")

def zien(dic):
  global totale_prijs
  vraag = input("wil je zien wat er in je boodschappenlijstje zit? ").lower()
  if vraag == "ja":
    print(dic)
  elif vraag == "nee":
    print("Wat, waarom heb je anders zien ingetypt? ")
    print("Om te weten wat de toale prijs is? ")
  else:
    print("Wat doe je nou weer? Dat is geen antwoord! ")

  values = dic.values()
  lijst = list(values)
  for i in range(len(lijst)):
    totale_prijs = totale_prijs + int(lijst[i])
  vraag2 = input("Wil je dan weten wat de totale prijs is? ").lower()
  if vraag2 == "ja":
    print("de totale prijs is " + str(totale_prijs) + " euro")
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
    print("Als je wil weten wat je boodschappenlijstje nu is, kan je gewoon zien doen. ")
  elif vraag3 == "nee":
    print("ok dan niet")
  else:
    print("dat is geen antwoord")

def boodschappen(dic, dic2):
  global prijsboodschap
  print("Ik laat nu zien wat er allemaal op je lijstje staat en moet je kiezen welke je koopt en dan laat ik zien hoeveel dat kost")
  print(dic)
  vraag7 = input("Hoeveel verschillende boodschappen wil je kopen? ")
  for i in range(int(vraag7)):
    vraag6 = input("Zeg nu de naam van de " + str(i+1) + "e die je wil kopen. ")
    vraag8 = int(input("En hoeveel wil je ervan kopen? "))
    value123 = int(dic[vraag6])
    prijs = value123 * vraag8
    dic2[vraag6] = prijs
  values2 = dic2.values()
  lijst2 = list(values2)
  for i in range(len(lijst2)):
    prijsboodschap = prijsboodschap + int(lijst2[i])
  print("De prijs voor de boodschappen die jij hebt gekozen is " + str(prijsboodschap) + " euro")

def wijzigen(dic):
  print(dic)
  vraag7 = input("Welke wil je veranderen? (als je de eerste wil veranderen dat typ je 1 etc.) ")
  number = int(vraag7) - 1
  key2 = str(list(dic)[number])
  vraag8 = input("Wil je het product veranderen of de prijs? ").lower()
  if vraag8 == "product":
    vraag9 = input("Wat wordt de nieuwe naam")
    dic[vraag9] = dic[key2]
    del dic[key2]
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
    print("Toch nog bedacht? ")
    return False
  else:
    print("dat was geen antwoord, ik stop het zelf wel")

  return True

def menu():
  done = False
  while done == False:
    print("wat wil je doen?")
    if not dic == {}:
      keuzes = "zien, toevoegen, boodschappen, wijzigen of stop "
    elif dic == {}:
      keuzes = "aanmaken of stop "
    vraag5 = input("je kan kiezen uit " + keuzes).lower()
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

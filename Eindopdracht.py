def aanmaken(boodschappen):
  print("Normaal zou ik nu alle boodschappen die je kan kopen laten zien maar je kan ook zelf een assortiment aan boodschappen maken.")
  zelf_assortiment_vraag = input("Wil je zelf een assortiment maken? ").lower()
  if zelf_assortiment_vraag == "ja":
    hoeveel_op_lijst_vraag = int(input("hoeveel dingen zitten er op het lijstje? "))
    if not hoeveel_op_lijst_vraag == "":
      for i in range(hoeveel_op_lijst_vraag):
        product_vraag = input("wat is het " + str(i+1) + "e boodschap? (graag niet een boodschap herhalen) ")
        prijs_vraag = input("en wat is de prijs? ")
        boodschappen[product_vraag] = prijs_vraag
    else:
      print("Ik vroeg hoeveel dingen er op zaten")
  elif zelf_assortiment_vraag == "nee":
    boodschappen["brood"] = 2
    boodschappen["water"] = 1
    boodschappen["sap"] = 3
    print("Ok dan is je assortiment nu dit: " + str(boodschappen))
  else:
    print("Dat is geen antwoord")

def zien(boodschappen):
  totale_prijs = 0
  in_boodschappenlijst_vraag = input("wil je zien wat er in je boodschappenlijstje zit? ").lower()
  if in_boodschappenlijst_vraag == "ja":
    print(boodschappen)
  elif in_boodschappenlijst_vraag == "nee":
    print("Wat, waarom heb je anders zien ingetypt? ")
    print("Om te weten wat de toale prijs is? ")
  else:
    print("Wat doe je nou weer? Dat is geen antwoord! ")

  for val in boodschappen.values():
      totale_prijs = totale_prijs + val
  totale_prijs_vraag = input("Wil je dan weten wat de totale prijs is? ").lower()
  if totale_prijs_vraag == "ja":
    print("de totale prijs is " + str(totale_prijs) + " euro")
  elif totale_prijs_vraag == "nee":
    print("ok dan niet")
  else:
    print("dat is geen antwoord")

def toevoegen(boodschappen):
  boodschappen_toevoegen_vraag = input("wil je een boodschap toevoegen? ").lower()
  if boodschappen_toevoegen_vraag == "ja":
    print("dit is je boodschappenlijstje nu: ")
    print(boodschappen)
    product = input("zeg nu de volgende boodschap (niet eentje herhalen) ")
    prijs = int(input("en wat is de prijs? "))
    boodschappen[product] = prijs
    print("Als je wil weten wat je boodschappenlijstje nu is, kan je gewoon zien doen. ")
  elif boodschappen_toevoegen_vraag == "nee":
    print("ok dan niet")
  else:
    print("dat is geen antwoord")

def boodschappendoen(boodschappen):
  prijsboodschap = 0
  lijst_van_aankopen = {}
  print("Ik laat nu zien wat er allemaal op je lijstje staat en moet je kiezen welke je koopt en dan laat ik zien hoeveel dat kost")
  print(boodschappen)
  aantal_producten = int(input("Hoeveel verschillende boodschappen wil je kopen? "))
  for i in range(aantal_producten):
    product = input("Zeg nu de naam van de " + str(i+1) + "e die je wil kopen. ")
    aantal = int(input("En hoeveel wil je ervan kopen? "))
    prijs = boodschappen[product] * aantal
    lijst_van_aankopen[product] = prijs
  for val in lijst_van_aankopen.values():
    prijsboodschap = prijsboodschap + val
  print("De prijs voor de boodschappen die jij hebt gekozen is " + str(prijsboodschap) + " euro")

def wijzigen(boodschappen):
  print(boodschappen)
  welk_veranderen_vraag = int(input("Welke wil je veranderen? (als je de eerste wil veranderen dat typ je 1 etc.) ")) - 1
  wijzig_product = str(list(boodschappen)[welk_veranderen_vraag])
  product_of_prijs = input("Wil je het product veranderen of de prijs? ").lower()
  if product_of_prijs == "product":
    nieuw_product = input("Wat wordt de nieuwe naam")
    boodschappen[nieuw_product] = boodschappen[wijzig_product]
    del boodschappen[wijzig_product]
  elif product_of_prijs == "prijs":
    nieuw_prijs = input("Wat wordt de nieuwe prijs? ")
    boodschappen[wijzig_product] = nieuw_prijs
  else:
    print("Wtf is dat voor antwoord je moet product of prijs invullen")

def echt_stoppen():
  wil_stoppen = input("wil je stoppen? ").lower()
  if wil_stoppen == "ja":
    print("ok ik stop hem")
    return "stop"
  elif wil_stoppen == "nee":
    print("Toch nog bedacht? ")
    return ""
  else:
    print("dat was geen antwoord, ik stop het zelf wel")
    return "stop"

def main():
  boodschappen = {}
  stoppen = ""


  keuzes = keuzes_check(boodschappen)
  while stoppen != "stop":
    keuzes = keuzes_check(boodschappen)
    wat_te_doen_vraag = vragen_wat_te_doen(boodschappen, keuzes)
    if wat_te_doen_vraag == "aanmaken":
      aanmaken(boodschappen)
    elif wat_te_doen_vraag == "zien":
      zien(boodschappen)
    elif wat_te_doen_vraag == "stop":
      stoppen = echt_stoppen()
    elif wat_te_doen_vraag == "toevoegen":
      toevoegen(boodschappen)
    elif wat_te_doen_vraag == "boodschappen":
      boodschappendoen(boodschappen)
    elif wat_te_doen_vraag == "wijzigen":
      wijzigen(boodschappen)
    else:
      print("wat typte je nou?")
      stoppen = echt_stoppen()

def keuzes_check(boodschappen):
  if boodschappen == {}:
    return "aanmaken of stop "
  else:
    return "zien, toevoegen, boodschappen, wijzigen of stop "

def vragen_wat_te_doen(boodschaooen, keuzes):
  print("wat wil je doen?")
  return input("je kan kiezen uit " + keuzes).lower()

main()

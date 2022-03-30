def max_van_3(een, twee, drie):
  if een < twee:
    if twee < drie:
      return drie
    elif twee > drie:
      return twee
  elif een > twee:
    if een > drie:
      return een
    elif een < drie:
      return drie
print(max_van_3(4, 6, 1))
def reverse_string(string):
  diction = []
  for i in range(len(string)):
    diction += string[i]
  string2 = ""
  for i in range(len(diction)):
    b = i + 1
    lengte = (len(string) - b)
    string2 += diction[lengte]
  return string2
revers = input("schrijf iets en ik zet het omgekeerd: ")
print(reverse_string(revers))
def is_priemgetal(getal):
  einde = True
  for deler in range(2, getal):
    if getal % deler == 0:
      einde = False
  return einde
cjfer = int(input("noem een cijfer en ik zeg of het een priemgetal is of niet: "))
print(is_priemgetal(cjfer))
def is_palindroom(abc):
  omgekeerd = reverse_string(abc)
  if omgekeerd == abc:
    return True
  else:
    return False
palindroom = str(input("noem een woord en ik zeg of het een palindroom is of niet: "))
print(is_palindroom(palindroom))

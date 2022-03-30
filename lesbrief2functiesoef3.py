def reverse(arry):
  array1 = ["hallo", "doei", "hello"]
  array2 = ["", "", ""]
  for i in range(len(array1)):
    b = i + 1
    c = len(array1) - b
    array2[i] = array1[c]
  return array2
print(reverse("hello"))
def leng():
  array3 = ["asdf", "asdf", "asdf"]
  teller = 0
  for item in array3:
    teller += 1
  return teller
print(leng())
lijst = ["bla", "hallo"]
def toevoegen(lijst, el):
  lijst += lijst, el
  print(lijst)
toevoegen(lijst, "hallo")
lijst2 = ["bla", "hallo"]
def veranderen(lijst, el):
  lijst[1] = el
  print(lijst)
veranderen(lijst2, "hoi")
lijst3 = ["blabla", "Bla"]
def laatsteverwijder(lijst):
  b = len(lijst) - 1
  del lijst[b]
  print(lijst)
laatsteverwijder(lijst3)
lijst4 = ["hallo", "doei", "goedemorgen"]
def gegevenverwijder(lijst, el):
  if el in lijst:
    if el == lijst[0]:
      del lijst[0]
    elif el == lijst[1]:
      del lijst[1]
    elif el == lijst[2]:
      del lijst[2]
  print(lijst)
gegevenverwijder(lijst4, "hallo")

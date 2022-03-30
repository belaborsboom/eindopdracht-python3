def dictionaryadd(n):
  global dic
  dic = {}
  for i in range(n):
    n2 = i + 1
    n3 = n2**2
    dic[n2] = n3
  print(dic)
dictionaryadd(50)

def isitindic(j):
  if j in dic:
    print("True")
  else:
    print("False")
isitindic(2000)

def valueoptel(dictionary):
  b = 0
  for i in range(len(dictionary)):
    c = i + 1
    b += dictionary[c]
  print(b)
valueoptel(dic)

def keyverwijder(dictionary, verwijder):
  del dictionary[verwijder]
  print(dictionary)
keyverwijder(dic, 2)

def maxmin(dictionary):
  print(dictionary[1])
  leng = len(dictionary) + 1
  print(dictionary[leng])
maxmin(dic)

def kopie(dictionary):
  x = dictionary.copy()
  print(x)
kopie(dic)

dic2 = {}
def is_empty(dictionary):
  if dictionary == {}:
    print(True)
  else:
    print(False)
is_empty(dic2)

dic3 = {"1":["a", "b", "c"], "2":["d", "e", "f"]}
def combi(dictionary):
  print(len(dictionary))
  values = dictionary.values()
  op = list(values)[0]
  op2 = list(values)[1]
  for i in range(len(op)):
    qr = op[i]
#    nummer = len(list(dictionary)[i]) * 2
#    print(len(op))
#    print(nummer)
    for j in range(len(op2)):
      values2 = dictionary.values()
      st = list(values2)[1]
      uv = st[j]
      g = qr + uv
      print(g)
combi(dic3)

str2 = "hallo"
def to_dict(string):
  a = {}
  for i in range(len(string)):
    a[string[i]] = string.count(string[i])
  print(a)
to_dict(str2)

dic4 = {1: 5, 2: 6, 3: 7}
def som(dictionary):
  dic5 = {}
  values = dictionary.values()
  for i in range(len(dictionary)):
    op = list(values)[i]
    a = i + 1
    dic5[a] = op + a
  print(dic5)
som(dic4)

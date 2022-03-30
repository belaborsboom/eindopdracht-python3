codetalen = {"HTML": "div", "Linux": "cd"}
codetalen["Python"] = "print"
del codetalen["HTML"]
for key, value in codetalen.items():
  print(key, value)
invkey = input("vul een woord in en ik zeg of die een key is of niet: ")
if invkey in codetalen:
  print("ja die zit erin!")
else:
  print("nee...")

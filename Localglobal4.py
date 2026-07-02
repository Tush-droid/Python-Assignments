no=11 #global variable

def Display():
  global no
  no=21
  print("from display",no)

print("b4",no)
Display()
print("after",no)

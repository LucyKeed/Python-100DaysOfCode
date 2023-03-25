DoB = int(input("What year were you born in?: "))
if DoB >= 1925 and DoB <= 1946:
  print ("You're a Traditionalist")
elif DoB >= 1947 and DoB <= 1964:
  print ("You're a Baby Boomer")
elif DoB >= 1965 and DoB <= 1981:
  print ("You're Generation X")
elif DoB >= 1982 and DoB <= 1995:
  print ("You're a Millenial")
elif DoB >= 1996 and DoB <= 2015:
  print ("You're Generation Z")
else:
  print ("you're not old enough to be here!")


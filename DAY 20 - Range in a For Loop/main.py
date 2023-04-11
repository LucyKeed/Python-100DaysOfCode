#colour preset for purple text
pp = "\033[35m"

#user input range generator
print ("*~* OMG, its a Range List Generator! *~*")
print()
print ("(but only whole numbers for now please!...i ain't that skilled yet!)")
print ()
x = int(input("Starting number: "))
y = int(input("End number before: "))
z = int(input("In increments values of: "))
print ()
for i in range (x,y,z):
  print (pp,i,)
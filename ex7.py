nb=int(input("entre nombre : "))
def fonction(nb):
  s=0
  for i in range(1,nb+1):
    s+=(i**2)
  print(s)
fonction(nb)
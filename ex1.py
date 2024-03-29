print("saise les trois notes :")
n1 = float(input("1er note:"))
n2 = float(input("2eme note:"))
n3 = float(input("3eme note:"))
def my_function(a,b,c):
    moyenne=(a+b+c)/3
    if(moyenne>=16):
      print("note = ",moyenne,"tres bien")
    elif(moyenne<16 and moyenne>=14):
      print("note = ",moyenne,"bien")
    elif(moyenne<14 and moyenne>=12):
      print("note = ",moyenne,"asser bien")
    elif(moyenne<12 and moyenne>=10):
      print("note = ",moyenne,"passable")
    else:
      print("note = ",moyenne,"insuffisant")
if(n1>20 or n1<0 or n2>20 or n2<0 or n3>20 or n3<0):
  print("les notes incorect")
else:
  my_function(n1,n2,n3)
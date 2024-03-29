T = int(input("saise un temps en second:"))
def my_temps(T):
  h=int(T/3600)
  min=int((T%3600)/60)
  s=int((T%360)%60)
  print(" T= ",T,"second = ",h,"heures ",min," minutes",s," second ")
my_temps(T)
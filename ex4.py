age=int(input("entre l'age de L'habitant  :"))
sexe=input("entre  sexe de L'habitant (h for hommes / f for femmes) :")
def paientImpot(age,sexe):
  if (sexe == "h" and age > 20) or (sexe == "f" and 18 <= age <= 35):
    print( "L'habitant doit payer l'impôt.")
  else:
    print("L'habitant est exempté de l'impôt.")
    
paientImpot(age,sexe)
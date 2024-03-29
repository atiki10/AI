nb1=int(input("entre 1ere nomber :"))
nb2=int(input("entre 2eme nomber :"))
operateur=input("entre operateur ( + or - or * or / ) : ")
def operation(nb1,nb2,operateur):
  if(operateur=="+"):
    nb=nb1+nb2
    print(nb1,operateur,nb2,"=",nb)
  elif(operateur=="-"):
    nb=nb1-nb2
    print(nb1,operateur,nb2,"=",nb)
  elif(operateur=="*"):
    nb=nb1*nb2
    print(nb1,operateur,nb2,"=",nb)
  elif(operateur=="/"):
    nb=nb1/nb2
    print(nb1,operateur,nb2,"=",nb)
operation(nb1,nb2,operateur)
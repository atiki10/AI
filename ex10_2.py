N = int(input("Entrez la taille des vecteurs : "))
a = [float(input(f"Entrez l'élément {i+1} du vecteur a : ")) for i in range(N)]
b = [float(input(f"Entrez l'élément {i+1} du vecteur b : ")) for i in range(N)]

produit_scalaire = sum(a[i] * b[i] for i in range(N))
print("Le produit scalaire de a et b est :", produit_scalaire)
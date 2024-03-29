Tab = [int(input(f"Entrez l'élément {i+1} du tableau : ")) for i in range(10)]
est_trie = True

for i in range(1, len(Tab)):
    if Tab[i] < Tab[i-1]:
        est_trie = False
        break

if est_trie:
    print("Le tableau est trié dans l'ordre croissant.")
else:
    print("Le tableau n'est pas trié dans l'ordre croissant.")
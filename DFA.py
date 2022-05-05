fin=open("input", "r")
fisier=fin.readlines()
numar_noduri=int(fisier[0].split()[0])
numar_tranzitii=int(fisier[0].split()[1])

linie_input=1
automat = [[] for x in range(numar_noduri)] # lista pentru generarea automatului

# aceasta parte din algorim genereaza automatul, pe scurt in lista avem
# traseul pentru fiecare nod, adica unde duce acesta
while linie_input <= numar_tranzitii:
    capat_stanga = int(fisier[linie_input].split()[0])
    capat_dreapta = int(fisier[linie_input].split()[1])
    litera=fisier[linie_input].split()[2]
    automat.extend([])
    automat[capat_stanga].append(capat_dreapta)
    automat[capat_stanga].append(litera)
    linie_input += 1


stare_initiala = int(fisier[linie_input].split()[0]) #aici salvam starea initiala
linie_input += 1
starile_finale = fisier[linie_input].split()

nf = int(starile_finale[0])

stari_finale = [] # in aceasta lista salvam starile finale

for j in starile_finale[1:]:
    stari_finale.append(int(j))


linie_input += 1
nr_stringuri = int(fisier[linie_input].split()[0])

for x in range(1, nr_stringuri+1): # acest for parcurge fiecare traseu din input
    linie_input += 1
    raspuns = [] #lista in care salvam traseul
    traseu = fisier[linie_input].strip() #traseul dat ca input
    litera = traseu[0]
    lungime_traseu = len(traseu)


    if litera in automat[stare_initiala]:
        pozitie = automat[stare_initiala].index(litera) #verificam cum vrea automatul sa tranzitioneze din starea initiala
        indice = int(automat[stare_initiala][pozitie-1]) #aici salvam urmatorul nod
        raspuns.append(stare_initiala)


    for litera in traseu[1:]:
        if litera in automat[indice]:
            raspuns.append(indice)
            indice_curent = indice
            pozitie = automat[indice].index(litera)
            indice = int(automat[indice_curent][pozitie-1])

    raspuns.append(indice) #facem append pentru a salva si ultima stare
    stare_finala = indice
    lungime_raspuns = len(raspuns)


    if lungime_raspuns == lungime_traseu + 1 and stare_finala in stari_finale: #aici verificam daca ultima stare
                                                                            #este si stare finala
        print("DA")
        print(*raspuns)
    else:
        print("NU")








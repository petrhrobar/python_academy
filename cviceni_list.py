list_cisel = [20, 40, 60, 23, 50, 10]

print(list_cisel)

print(len(list_cisel))

for cislo in list_cisel:
    print(cislo)

list_cisel.append('Dneska je streda')
print(list_cisel)

# Ukaze mi to funkce, ktere mohu na list zavolat napr list.append
# print(dir(list_cisel))

novy_list = []
print(novy_list)

novy_list.append('prvni item v listu!!!')
novy_list.append('prvni item v listu!!!')
novy_list.append('prvni item v listu!!!')
novy_list.append('prvni item v listu!!!')
novy_list.append('prvni item v listu!!!')
print(len(novy_list))
print(novy_list)

list_sude = []

# Cislo od 0 do 20 (pouze suda)

for cislo in range(0, 21):
    if cislo % 2 == 0:
        list_sude.append(cislo)
        
print(list_sude)

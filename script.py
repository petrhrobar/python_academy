# +
from pomocne_fce import obsah_ctverce, obvod_ctverce, obvod_z_cm_na_palce

def wrapper(strana):
    # Pro jistotu prevadim na cislo
    c_strana = int(strana)
    
    # spocitame obsah v cm2
    obsah_vysledek = obsah_ctverce(c_strana)
    
    # spocimate obvod v cm
    obvod_vysledek = obvod_ctverce(c_strana)
    
    # prevod obvodu na palce
    obvod_palce_vysledek = obvod_z_cm_na_palce(obvod_vysledek)
    
    print('obsah ctverce je')
    print(obsah_vysledek)

    print('obvod ctverce je (v cm)')
    print(obvod_vysledek)

    print('obvod ctverce je (v palce)')
    print(obvod_palce_vysledek)


# -

list_stran = [10, 12.5, 22.5, 15, 8]

for cislo in list_stran:
    wrapper(cislo)



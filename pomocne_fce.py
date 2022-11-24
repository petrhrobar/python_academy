def obsah_ctverce(strana):
    # pro jistotu prevadim na cele cislo
    strana_cisla = int(strana)
    # obsah ctverce jako delka x sirka
    obsah = strana_cisla * strana_cisla
    return obsah

def obvod_ctverce(strana):
    #str to int
    c_strana = int(strana)
    #vzorec na obvod ctverce
    obvod = c_strana * 4
    return(obvod)

def obvod_z_cm_na_palce(obvod):
    
    # pro jistotu prevod na int
    c_obvod = int(obvod)
    
    # 1palec = 2.53 cm
    palce = 2.53
    
    prevod = c_obvod/palce
    
    return prevod


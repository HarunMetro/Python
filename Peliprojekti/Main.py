from Class import *
from Function import *

pelaaja = luo_pelaaja()
komento = aloita_peli(pelaaja)

while komento != "quit":
    if not pelaaja.matka_alkanut and komento == "walking":
        reitti_kävely1(pelaaja)
        tapahtuma_kävely_roska(pelaaja, pieni_valikko)
        tapahtuma_kävely_kyssäri(pelaaja, pieni_valikko)
        tapahtuma_kävely_ystävä(pelaaja, pieni_valikko)
        tapahtuma_kävely_reitti_koulu(pelaaja)
        pelaaja.matka_alkanut = True


    elif not pelaaja.matka_alkanut and komento == "bicycle":
        reitti_pyörä1(pelaaja)
        tapahtuma_pyörä_mäki(pelaaja, pieni_valikko)
        tapahtuma_pyörä_koira(pelaaja, pieni_valikko)
        tapahtuma_pyörä_kivi(pelaaja, pieni_valikko)
        tapahtuma_pyörä_reitti_koulu(pelaaja)
        pelaaja.matka_alkanut = True


    elif not pelaaja.matka_alkanut and komento == "bus":
        reitti_bussi1(pelaaja)
        tapahtuma_bussi_myöhässä(pelaaja, pieni_valikko)
        tapahtuma_bussi_lippu(pelaaja, pieni_valikko)
        tapahtuma_bussi_penkki(pelaaja, pieni_valikko)
        tapahtuma_bussi_pysäkki_ohi(pelaaja, pieni_valikko)
        tapahtuma_bussi_reitti_koulu(pelaaja)
        pelaaja.matka_alkanut = True
    
    
    elif not pelaaja.matka_alkanut and komento == "car":
        reitti_auto1(pelaaja)
        tapahtuma_auto_unohdettu(pelaaja, pieni_valikko)
        tapahtuma_auto_liikenne(pelaaja, pieni_valikko)
        tapahtuma_auto_pysäköinti(pelaaja, pieni_valikko)
        tapahtuma_auto_reitti_koulu(pelaaja)
        pelaaja.matka_alkanut = True

    elif komento == "backpack":
        pelaaja.näytä_reppu()

    elif komento == "location":
        pelaaja.näytä_sijainti()

    else:
        print("\nUnknown command. Please try again.")

    if pelaaja.matka_alkanut:
        tulosta_valikko(pieni_valikko, "Small Menu")
    else:
        tulosta_valikko(pää_valikko, "How would you like to travel to school today?")

    komento = input("Enter command: ").lower()

print(f"\nThank you for playing, {pelaaja.käyttäjätunnus}! See you never.")
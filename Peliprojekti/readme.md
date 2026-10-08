## One Morning, Many Choices

## Haroon Hashemi

Tekstiseikkailupeli, jossa pelaaja valitsee miten pääsee kouluun
(kävely, pyörä, bussi tai auto) ja tekee valintoja matkan varrella.

## Käynnistys

Aja `Main.py` Peliprojekti-kansiosta:

    python Main.py

## Tiedostorakenne

| Tiedosto         | Sisältö                                                        |
|------------------|----------------------------------------------------------------|
| `Main.py`        | Pelin käynnistys ja pääsilmukka: luo pelaajan, näyttää intron ja kutsuu valitun reitin tapahtumat |
| `Class.py`       | Luokat `Pelaaja`, `Esine` ja `Paikka`, reittikartta sekä `luo_pelaaja()` |
| `Function.py`    | Valikot, kysymysfunktiot ja kaikki reittien tapahtumat (kävely, pyörä, bussi auto) |
| `Intro.txt`      | Pelin tarinateksti, luetaan tiedostosta pelin alussa           |
| `Instructions.txt` | Pelin ohjeet                                                 |
| `readme.md`      | Tämä tiedosto                                                  |

## Oliorakenne

- `Pelaaja`: nimi, ikä, reppu (lista `Esine`-olioita), sijainti (`Paikka`), tunteet
- `Esine`: nimi ja paino
- `Paikka`: nimi

Pelaajalla on metodit repun ja sijainnin näyttämiseen sekä esineen lisäämiseen reppuun.
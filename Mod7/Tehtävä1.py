import random 

def heittää_noppa():
    return random.randint(1,6)

numero = heittää_noppa()
print(f"Heitit: {numero}")

while numero != 6:
    numero = heittää_noppa()
    print(f"Heitit: {numero}")

print("Sait kuutosen!")

## tai tapa 2

# def heitä_noppa():
#     numero = random.randint(1,6)
#     heitto_määrä = 1

#     while numero != 6:
#         numero = random.randint(1,6)    
#         heitto_määrä += 1

#     return numero, heitto_määrä

# tulos, heitä_määrä = heitä_noppa()
# print(f"Sait kuutosen {tulos}. heitolla {heitä_määrä}!")
tuuma = float(input("Anna tuuma: "))

while tuuma >= 0:
    senttimetri = tuuma * 2.54
    print(f"{tuuma} tuumaa on {senttimetri:.2f} senttimetriä.")
    tuuma = float(input("Anna tuuma: "))
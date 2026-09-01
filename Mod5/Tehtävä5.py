yritykset = 0

käyttäjätunnnus = input("Anna käyttäjätunnus:\n")
salasana = input("Anna salasana\n")

while käyttäjätunnnus != "python" or salasana != "rules":
    yritykset = yritykset + 1
    if yritykset == 5:
        print("Pääsy evätty.")
        break
    käyttäjätunnnus = input("Anna käyttäjätunnus:\n")
    salasana = input("Anna salasana\n")
else:
    print("Tervetuloa!")

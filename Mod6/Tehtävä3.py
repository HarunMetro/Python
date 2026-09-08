
alkuluku = int(input("Anna alkuluku: "))

if alkuluku < 2:
    print(f"{alkuluku} ei ole alkuluku.")
else:
    for i in range(2, alkuluku):
        if alkuluku % i == 0:
            print(f"{alkuluku} ei ole alkuluku.")
            break
    else:
        print(f"{alkuluku} on alkuluku.")
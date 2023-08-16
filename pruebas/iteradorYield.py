def multiplo(limite):
    num = 1
    listnum = []

    while num <= limite:
        listnum.append(num * 7)
        num = num + 1
    return listnum


print(f"multiplo  : {multiplo(5)}")


def multiplo5(limite):
    num = 1
    while num <= limite:
        yield num * 7
        num = num + 1


obtenermultiplo = multiplo5(5)

for n in obtenermultiplo:
    print(f"Numero : {n}")

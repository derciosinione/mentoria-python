# nome = "Cassia"
# frutas = ["Banana", "Manga", "Laranja"]
# perifericos = ["Computador", "Tablet", "Iphone"]

# shopList = []

# shopList.append(nome)
# shopList.append(frutas)
# shopList.append(perifericos)


def pegarList(array: list, index):
    return array[index]

def pegarSegundaLista(array: list) -> list:
    return array[1][3]

frutas = ["Banana", "Manga", "Laranja", [2022, 2023, 2024]]
shopList = ["Cassia", frutas, ["Computador", "Tablet", "Iphone"]]

print(pegarList(shopList[1], 1))

print(pegarSegundaLista(shopList)[0])

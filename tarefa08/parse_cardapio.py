from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName("prato")

print("--- MENU DO RESTAURANTE ---")
for prato in pratos:
    id_val = prato.getAttribute("id")
    nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f"{id_val} - {nome}")

escolha = input("\nDigite o ID do prato: ")

for prato in pratos:
    if prato.getAttribute("id") == escolha:
        
        nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        desc = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
        preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue
        moeda = prato.getElementsByTagName("preco")[0].getAttribute("moeda")
        cal = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
        tempo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue
        
        ingredientes = prato.getElementsByTagName("ingrediente")

        print(f"\nNome: {nome}")
        print(f"Descrição: {desc}")
        print("Ingredientes:")
        for ing in ingredientes:
            print("-", ing.firstChild.nodeValue)
        
        print(f"Preço: {moeda} {preco}")
        print(f"Calorias: {cal} kcal")
        print(f"Tempo de preparo: {tempo}")
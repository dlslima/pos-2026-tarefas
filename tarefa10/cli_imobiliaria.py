import json

with open("imobiliaria.json", "r", encoding="utf-8") as arquivo:
    imoveis = json.load(arquivo)

print("--- IMOBILIÁRIA ---")
for i in range(len(imoveis)):
    print(f"{i + 1} - {imoveis[i]['descricao']}")

opcao = int(input("\nDigite o ID do imóvel: "))

if 1 <= opcao <= len(imoveis):
    imovel = imoveis[opcao - 1]

    print("\n=== DETALHES DO IMÓVEL ===")
    print("Descrição:", imovel["descricao"])

    print("\nProprietário:")
    print("Nome:", imovel["proprietario"]["nome"])

    print("Telefones:")
    for t in imovel["proprietario"]["telefones"]:
        print("-", t)

    print("Emails:")
    for e in imovel["proprietario"]["emails"]:
        print("-", e)

    print("\nEndereço:")
    print("Rua:", imovel["endereco"]["rua"])
    print("Número:", imovel["endereco"]["numero"])
    print("Bairro:", imovel["endereco"]["bairro"])
    print("Cidade:", imovel["endereco"]["cidade"])

    print("\nCaracterísticas:")
    print("Tamanho:", imovel["caracteristicas"]["tamanho"])
    print("Quartos:", imovel["caracteristicas"]["numQuartos"])
    print("Banheiros:", imovel["caracteristicas"]["numBanheiros"])

    print("\nValor:", imovel["valor"])

else:
    print("ID inválido.")
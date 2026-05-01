from xml.dom.minidom import parse
import json

dom = parse("imobiliaria.xml")
raiz = dom.documentElement

imoveis = raiz.getElementsByTagName("imovel")

lista = []

for imovel in imoveis:

    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue

    proprietario = imovel.getElementsByTagName("proprietario")[0]
    nome = proprietario.getElementsByTagName("nome")[0].firstChild.nodeValue

    telefones = proprietario.getElementsByTagName("telefone")
    lista_telefones = [t.firstChild.nodeValue for t in telefones]

    emails = proprietario.getElementsByTagName("email")
    lista_emails = [e.firstChild.nodeValue for e in emails]

    endereco = imovel.getElementsByTagName("endereco")[0]
    rua = endereco.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = endereco.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = endereco.getElementsByTagName("cidade")[0].firstChild.nodeValue

    numero_tag = endereco.getElementsByTagName("numero")
    numero = numero_tag[0].firstChild.nodeValue if numero_tag else None

    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]
    tamanho = caracteristicas.getElementsByTagName("tamanho")[0].firstChild.nodeValue
    quartos = caracteristicas.getElementsByTagName("numQuartos")[0].firstChild.nodeValue
    banheiros = caracteristicas.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue

    valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue

    imovel_dict = {
        "descricao": descricao,
        "proprietario": {
            "nome": nome,
            "telefones": lista_telefones,
            "emails": lista_emails
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": quartos,
            "numBanheiros": banheiros
        },
        "valor": valor
    }

    lista.append(imovel_dict)

with open("imobiliaria.json", "w", encoding="utf-8") as f:
    json.dump(lista, f, indent=4, ensure_ascii=False)

print("Arquivo imobiliaria.json criado com sucesso!")
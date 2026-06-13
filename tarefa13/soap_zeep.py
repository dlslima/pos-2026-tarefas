import zeep

# define a URL do WSDL
wsdl_url = "http://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"


client = zeep.Client(wsdl=wsdl_url)


numero = input("Digite o número que deseja converter: ")

# faz a chamada do serviço
result = client.service.NumberToWords(
	ubiNum=numero
)

print(f"{result}")
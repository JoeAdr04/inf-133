from zeep import Client
## https://www.dataaccess.com/webservicesserver/NumberConversion.wso.?WSDL

client = Client(

)
result = client.service.NumberToWords(5)
print (result)
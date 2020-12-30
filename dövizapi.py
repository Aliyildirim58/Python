import requests 
import json

api_url="https://api.exchangeratesapi.io/latest?base="
print("TRY,USD,EUR,vb kısaltmalar")
bozulan_döviz=input('Bozulan Döviz cinsi: ')
alınan_döviz=input('Alınan Döviz cinsi: ')
miktar = int(input(f"Ne kadar {bozulan_döviz} bozdurmak istiyorsunuz: "))
result=requests.get(api_url+bozulan_döviz)
result=json.loads(result.text)
print("1 {0} = {1} {2}".format(bozulan_döviz, result["rates"][alınan_döviz], alınan_döviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_döviz, miktar * result["rates"][alınan_döviz],alınan_döviz))

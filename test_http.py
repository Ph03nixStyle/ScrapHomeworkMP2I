from test_json import sites_info
import requests

URL = sites_info["laessie"]["url"]

COOKIES = {
	"_snow_id.174f":"25e94c48-bf70-4106-852a-f068ed9fba59.1630704353.2.1630707430.1630704353.8ac644d8-e201-4b28-80d9-c249f588f0dc",
	"WeeblySiteLogin":"weeblylogin:623b1c9793f68c635af15fb8354a620d3b630bf37f3e2b652b16384dfecca157"
}

r=requests.get(URL, cookies=COOKIES)
print(r.content)
import requests
import json



url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"

querystring = {"league":"39","season":"2022t"}

headers = {
	"X-RapidAPI-Key": "3ae49bd480msh5a2534d4142299ep1d1970jsn9bdcd8eb72ba",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
#transformer la réponse en json
#récuperer que les 4000 premier caractères de la réponse et les afficher en string
#print(response.text)
#mettre la réponse dans un fichier json
def get_json(response):
    return response

json_string = json.dumps(response)
print(response)

with open('data.json', 'w') as f:
    f.write(json_string)
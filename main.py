import requests

def gen():
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
        'accept': '*/*',
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
    }
    data = {
        'partnerUserId': '4dabc1faaaca81728b4d8ed1ab0d4c3fe249ef77627411b7229cbc81e8fe86cd'
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()  
        return response_json.get('token', '')  
    else:
        return f"Erreur {response.status_code} : La requête a échoué"

def affichage():
    result_gen = gen()
    if result_gen:
        print("https://discord.com/billing/partner-promotions/1180231712274387115/" + result_gen)
    else:
        print("La fonction gen() n'a pas renvoyé de résultat valide.")

affichage()

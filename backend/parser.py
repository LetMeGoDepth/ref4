import requests


def get_vacancys(pars):
    url = 'https://api.hh.ru/vacancys'
    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    pars_vacancys = []
    for j in range(0, 20):
        pars.page = j
        response = requests.get(url, params=pars, headers=headers)
        if response.status_code == 200:
            vacancys = response.json().get('items', [])
            for vacancy in vacancys:
                pars_vacancys.append({'vacancys_id': vacancy.get('id'),
                                        'url': vacancy.get('alternate_url'),
                                        'professional_roles': vacancy.get('professional_roles')[0].get('name') if vacancy.get('professional_roles') else None,
                                        'name': vacancy.get('name'),
                                        'vacancys_type': vacancy.get('type').get('name') if vacancy.get('type') else None,
                                        'company_name': vacancy.get('employer').get('name') if vacancy.get('employer') else None,
                                        'snippet_requirement': vacancy.get('snippet').get('requirement'),
                                        'snippet_responsibility': vacancy.get('snippet').get('responsibility'),
                                        'experience': vacancy.get('experience').get('name') if vacancy.get('experience') else None,
                                        'salary': vacancy.get('salary') if vacancy.get('salary') else None})
        else:
            print(f"Ошибка запроса: {response.status_code}")
        return None
    
    return pars_vacancys
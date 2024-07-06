import requests
def get_vacancies(pars):
    url = 'https://api.hh.ru/vacancies'
    headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    prs_vacs = []
    for j in range(0, 20):
        pars.page = j
        response = requests.get(url, params=pars, headers=headers)
        if response.status_code == 200:
            vacancies = response.json().get('items', [])
            for vacancie in vacancies:
                prs_vacs.append({ 'vacancies_id': vacancie.get('id'),
                                        'url': vacancie.get('alternate_url'),
                                        'professional_roles': vacancie.get('professional_roles')[0].get('name'),
                                        'name': vacancie.get('name'),
                                        'vacancies_type': vacancie.get('type').get('name'),
                                        'company_name': vacancie.get('employer').get('name'),
                                        'snippet_requirement': vacancie.get('snippet').get('requirement'),
                                        'snippet_responsibility': vacancie.get('snippet').get('responsibility'),
                                        'experience': vacancie.get('experience').get('name'),
                                        'salary': str(vacancie.get('salary'))})
    return prs_vacs




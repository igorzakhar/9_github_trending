from datetime import date, timedelta

import requests


BASE_URL = 'https://api.github.com/search/repositories'
TOP_SIZE = 20
RECENT_DAYS = 1


def get_date(recent_days):
    return date.today() - timedelta(days=recent_days)


def get_trending_repositories(top_size, ):
    query_params = {'q': 'created'.format(recent_days),
                    'sort': 'stars',
                    'per_page': top_size}

    


def get_open_issues_amount(repo_owner, repo_name):
    pass

if __name__ == '__main__':
    query_params = {'q': 'created:>={}'.format(get_date(RECENT_DAYS)),
                    'sort': 'stars',
                    'per_page': TOP_SIZE}
    response = requests.get(BASE_URL, params=query_params)
    #print(get_date(RECENT_DAYS))
    print(response.url)
    response_dict = response.json()
    resp_dicts = response_dict['items']
    for resp_dict in resp_dicts[:20]:
        print(resp_dict['name'])





from datetime import date, timedelta

import requests


BASE_URL = 'https://api.github.com'
TOP_SIZE = 20
RECENT_DAYS = 7


def get_date(recent_days):
    return date.today() - timedelta(days=recent_days)


def get_trending_repositories(top_size):
    url = BASE_URL +'/search/repositories'
    query_params = {'q': 'created:>={}'.format(get_date(RECENT_DAYS)),
                    'sort': 'stars',
                    'per_page': top_size}
    response = requests.get(url, params=query_params)
    response_dict = response.json()
    repositories_dict = response_dict['items']
    return repositories_dict
    

def get_open_issues_amount(repo_owner, repo_name):
    url = BASE_URL + '/repos/{}/{}/issues'.format(repo_owner, repo_name)
    response = requests.get(url)
    response_dict = response.json()
    open_issues = len(response_dict)
    return open_issues, response.headers['X-RateLimit-Remaining']


def pretty_print_output(repositories):
    header_string = '{0:^30} | {1:^5} | {2:^11} | {3:<45}'
    format_string = '{0:<30} | {1:^5} | {2:^11} | {3:<45}'
    separator_string = '-' * 103
    print(separator_string)
    print(header_string.format('Name', 'Stars', 'Open issues', 'URL'))
    print(separator_string)
    for repo in repositories:
        open_issues, rate_limit = get_open_issues_amount(
                                          repo['owner']['login'], repo['name'])
        if rate_limit == '0':
            open_issues = repo['open_issues']
        print(format_string.format(repo['name'], repo['stargazers_count'],
                                   open_issues,
                                   repo['html_url']))
        print(separator_string)


if __name__ == '__main__':
    trending_repositories = get_trending_repositories(TOP_SIZE)
    pretty_print_output(trending_repositories)


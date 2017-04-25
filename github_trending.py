from datetime import date, timedelta

import requests


def get_date(recent_days):
    return date.today() - timedelta(days=recent_days)


def get_trending_repositories(top_size, recent_days):
    url = 'https://api.github.com/search/repositories'
    query_params = {'q': 'created:>={}'.format(recent_days),
                    'sort': 'stars',
                    'per_page': top_size}
    response = requests.get(url, params=query_params)
    response_dict = response.json()
    repositories_dict = response_dict['items']
    return repositories_dict
    

def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name)
    response = requests.get(url)
    response_dict = response.json()
    open_issues = len(response_dict)
    return open_issues, response.headers['X-RateLimit-Remaining']


def pretty_print_output(repositories):
    header_string = '{0:^30} | {1:^5} | {2:^11} | {3:^45}'
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
    TOP_SIZE = 20
    days_count = get_date(recent_days)
    trending_repositories = get_trending_repositories(TOP_SIZE, days_count)
    pretty_print_output(trending_repositories)


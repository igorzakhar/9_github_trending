import argparse
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
    open_issues_urls = [issue['url'] for issue in response_dict]
    return open_issues_urls


def output_results(repositories, verbose):
    format_string = ('Name: {0:<25} | Stars\u2605 : {1:^5} |'
                    'Open issues: {2:^5} | URL {3:<45}')
    separator_string = '-' * 103
    for repo in repositories:
        print(format_string.format(repo['name'], repo['stargazers_count'],
                                   repo['open_issues'],
                                   repo['html_url']))
        if verbose:
            open_issues = get_open_issues_amount(repo['owner']['login'], 
                                                 repo['name'])
            print('Open issues urls:')
            for issue in open_issues:
                print(issue)
        print(separator_string)


def process_args():
    parser = argparse.ArgumentParser(description='Most starred repos find')
    parser.add_argument('-t', '--top_size',  default=20, 
                        help='Number of repositories for search. Default = 20')
    parser.add_argument('-d', '--recent_days', default=7,
                        help='Number of days repos being created. Default = 7')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='output issues urls')
    return  parser.parse_args()


if __name__ == '__main__':
    args = process_args()
    days_count = get_date(args.recent_days)
    trending_repos = get_trending_repositories(args.top_size, days_count)
    output_results(trending_repos, args.verbose)
                                                

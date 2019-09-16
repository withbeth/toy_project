import github_api as gh_api
from typing import List


def get_repos_and_commits() -> List[tuple]:
    # repos array -> repo dict -> collect all repo names to a list
    seq = []
    for repo in gh_api.get_repositories():
        repo_name = repo['name']
        commits = gh_api.get_commits(repo_name)
        seq.append((repo_name, commits))
    return seq


def has_any_update_on_repositories(date: str) -> bool:
    """
    TODO
    :param date: a date you need to check (format: yyyy/mm/dd)
    :return:
    """
    return False


def get_last_updated_date_from_all_repositories() -> str:
    """
    Getting last updated date from all repositories.
    :return: last updated date string (e.g: '2019-08-15T09:41:32Z')
    """
    return gh_api.get_repositories()[0]['updated_at']


def get_last_committed_date(repo_name : str) -> str:
    """
    Getting last commit date of given repository.
    :param repo_name: repository name
    :return: last committed date string (e.g,: ''2019-05-12T16:48:27Z')
    """
    return gh_api.get_commits(repo_name)[0]['commit']['committer']['date']


import github_api as gh_api
from typing import List, Dict, Tuple


def get_all_repositories_names() -> iter:
    return map(lambda repo: repo['name'] if repo else '', gh_api.get_repositories())


def get_last_commit_payload(repo_name: str) -> Tuple[str, str, str, str]:
    last_commit = gh_api.get_commits(repo_name)[0]
    # Return empty tuple when last_commit is empty
    if not last_commit:
        return '', '', '', ''
    return (
        last_commit['sha'],
        last_commit['commit']['committer']['date'],
        last_commit['commit']['committer']['name'],
        last_commit['commit']['message']
    )


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


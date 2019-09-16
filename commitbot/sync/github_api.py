from typing import List
import requests
import os
from colorama import Fore

# GitHub REST API info
ROOT_ENDPOINT = os.getenv("GH_ROOT_ENDPOINT")
ACCESS_TOKEN = os.getenv("GH_ACCESS_TOKEN")
OWNER = os.getenv("GH_USERNAME")
USERNAME = os.getenv("GH_USERNAME")


def get_repositories() -> List[str]:
    """
    Getting repositories
    :return: repositories json

    Specifications:
    https://developer.github.com/v3/repos/#list-your-repositories
    """
    end_point = f"/users/{USERNAME}/repos"
    payload = {
        "sort": "updated",
        "direction": "desc"
    }
    return request(end_point, payload)


def get_commits(repo_name: str) -> List[str]:
    """
    Getting commits of given repository.
    :param repo_name: repository name
    :return: commits json

    Specifications :
    https://developer.github.com/v3/repos/commits/#list-branches-for-head-commit
    """
    end_point = f"/repos/{OWNER}/{repo_name}/commits"
    return request(end_point)


def request(url: str, payload=None) -> List[str]:
    """
    Sending GET request to given github endpoint.
    :param url: github end point
    :param payload: parameters dict
    :return: response json
    Specifications :
    https://developer.github.com/v3/
    https://developer.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/
    https://2.python-requests.org/en/master/
    """
    print(Fore.YELLOW + f"GET {url}", flush=True)

    '''
    Adding auth token in incoming http request and response to un-limit to the amount of requests
    than can be made per hour from single IP address.
    you can specify Token Authentication that you're using
    e.g, headers = { "Authorization": "Bearer " + os.getenv("GH_ACCESS_TOKEN")}

    Providing a custom media type in the Accept Header for your requests.
    e.g, application/vnd.github.machine-man-preview+json
    '''
    headers = {
        "Authorization": "token" + ACCESS_TOKEN,
        "Accept": "application/vnd.github.v3+json"
    }
    resp = requests.get(f"{ROOT_ENDPOINT}{url}", headers=headers, params=payload)

    if resp.status_code == 200:
        print(Fore.GREEN + f"OK {resp.status_code}", flush=True)
        return resp.json()

    print(Fore.LIGHTMAGENTA_EX + f"FAIL {resp.status_code} {resp.reason}", flush=True)
    return ['']





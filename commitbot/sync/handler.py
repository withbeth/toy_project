import datetime
import service
from colorama import Fore


# TODO : CRON
def run_last_commit_watcher():
    t0 = datetime.datetime.now()

    # TODO : Executor count
    print(Fore.WHITE + "LastCommitWatcher started.", flush=True)

    # TODO : GET My own repos, not forked one..
    # TODO : ASYNC
    for repo_name in service.get_all_repositories_names():
        last_commit_payload = service.get_last_commit_payload(repo_name)
        print(Fore.CYAN + f"Repo: {repo_name} - Last Commit: {last_commit_payload}")


    # TODO : Check if there is any commit of yesterday
    # TODO : Alert if there

    # last_date = datetime.date(last_date_str[0:4], last_date_str[5:7], last_date_str[8:10])
    # if so, tell them your are working
    # else, tell them you need to commit

    dt = datetime.datetime.now() - t0
    print(Fore.WHITE + "LastCommitWatcher end, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


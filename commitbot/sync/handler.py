import datetime
from colorama import Fore


def invoke():
    t0 = datetime.datetime.now()
    print(Fore.WHITE + "App started.", flush=True)

    # TODO : Check if there is any commit of yesterday
    # last_date = datetime.date(last_date_str[0:4], last_date_str[5:7], last_date_str[8:10])
    # if so, tell them your are working
    # else, tell them you need to commit

    dt = datetime.datetime.now() - t0
    print(Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(dt.total_seconds()), flush=True)


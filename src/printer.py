'''
Change the formating for prints in other files
'''
from datetime import datetime


def printer(text:str) -> None:
    """
        Send a log with date + msg to the console
    Parameters
    ----------
        text : str
            Message to send to the console logs
    Returns
    ----------
        None
    """
    now = str(datetime.now())
    time = f'[{now[0:4]}-{now[5:7]}-{now[8:10]} {now[11:13]}:{now[14:16]}:{now[17:19]}]'
    print("{} {}".format(time, text))
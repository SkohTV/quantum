'''
Change the formating for prints in other files
'''

from datetime import datetime

def F(text):
    now = datetime.now()
    time = f'[{now.day}-{now.month}-{now.year} {now.hour}:{now.minute}:{now.second}]'
    return "{} {}".format(time, text)
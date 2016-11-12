from bs4 import BeautifulSoup
import requests
from datetime import datetime
import matplotlib.pyplot as plt

likes=[]
time=[]
time2=[]

r = requests.get('https://www.reddit.com/top/?sort=top&t=day')
soup = BeautifulSoup(r.content, "html.parser")
#print(soup)

x= soup.find_all("div", {"class": "score unvoted"})

for item in range(len(x)):
   try:
      likes.append(int(x[item].text))
   except:
      pass
   
y= soup.find_all("div", {"class": "entry unvoted"})

for item in y:
    try:
        print item.contents[1].find_all("a")[1].text
    except:
        pass
    
for i in soup.find_all('time'):
    time.append(i['datetime'])

likes1=likes[:]
time = [e.replace('+00:00', '') for e in time]
for uni in range(len(time)):
    time2.append(datetime.strptime(time[uni], '%Y-%m-%dT%H:%M:%S'))
print(time2)
print(len(time2))
print(len(likes1))
plt.plot(time2, likes)
plt.show()

    
 

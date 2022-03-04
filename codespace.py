from bs4 import BeautifulSoup
import requests
import json

source = requests.get("http://www.mnit.ac.in/news/newsall.php?type=latest").text

soup = BeautifulSoup(source, 'lxml')

li = soup.find('div', {'class': 'tabcontent','id':'latestD'})
children = li.findChildren('a')
temp_list = []
for child in children:
	temp_list.append(child.text)
data = {
	"news": temp_list,
}
jsson = json.dumps(data)
print(jsson)
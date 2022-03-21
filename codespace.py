from bs4 import BeautifulSoup
import requests
import json

source = requests.get("http://www.mnit.ac.in/news/newsall.php?type=latest").text

soup = BeautifulSoup(source, 'lxml')

li = soup.find('div', {'class': 'tabcontent','id':'latestD'})
children = li.findChildren('a', href=True)
temp_list = []
temp_list2 = []
for child in children:
	temp_list.append(child.text)
for child in children:
	temp_list2.append('http://www.mnit.ac.in/news/'+child['href'])
data = {
	"news": temp_list,
	"newsLink": temp_list2
}
jsson = json.dumps(data)
print(jsson)
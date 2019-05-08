from urllib.request import urlopen
import urllib
import self
from bs4 import BeautifulSoup

url = input("Please input the URL of which you would like to grab images from:\n")
html = urlopen(url)
features = "lxml"

soup = BeautifulSoup(html, features)


for res in soup.findAll('jpg'):
    print(res.get('src'))
    list_var = url.split('/')
    resource = urlopen(list_var[0] + '//' + list_var[2] + res.get('src'))
    output = open(res.get('src').split('/')[-1], 'wb')
    output.write(resource.read())
    output.close()

images = self.driver.find_elements_by_tag_name('img')
for image in images:
    src = image.get_attribute("src")
    if src:
        urllib.urlretrieve(src)


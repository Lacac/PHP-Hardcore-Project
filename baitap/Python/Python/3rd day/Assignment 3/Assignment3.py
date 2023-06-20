import requests
from bs4 import BeautifulSoup as bs
import json
import xml.etree.ElementTree as ET
import codecs

def get_requests(URL):
    data = requests.get(URL)
    return data

def get_content(URL):
    data = get_requests(URL)
    soup = bs(data.content, 'html.parser')
    content = str()
    contents = soup.find('article', attrs = {'class':'singular-container'})
    try:
        for row in contents.findAll('p'):
            content += row.text
    except:
        pass
    return content

def create_xml(list_articles):
        Articles = ET.Element("Articles")
  
        Articles = ET.SubElement(Articles, "Articles")
        count = 1
        for article in range(len(list_articles)):
            article = ET.SubElement(Articles, "article"+str(count))
            
            content =ET.SubElement(article, "Title")
            content.text = str(list_articles[count - 1]['title'])

            content =ET.SubElement(article, "Artical")
            content.text = str(list_articles[count - 1]['article_link'])

            content =ET.SubElement(article, "Picture")
            content.text = str(list_articles[count - 1]['picture_link'])

            content =ET.SubElement(article, "Content")
            content.text = str(list_articles[count - 1]['content'])

            count += 1

        tree = ET.ElementTree(Articles)

        # write the tree into an XML file
        tree.write("out.xml", encoding ='utf-8', xml_declaration = True)

BaseURL = "https://dantri.com.vn"
URL = "https://dantri.com.vn/kinh-doanh/tai-chinh.htm"
soup = bs(get_requests(URL).content, "html.parser")

articles = []

table = soup.find('article', attrs={'class':'article column'})

for row in table.findAll('article', attrs={'class':'article-item', 'data-content-name':'category-highlights'}):
    article = {}
    article['title'] = row.img['alt']
    article['article_link'] = BaseURL + row.a['href']
    article['picture_link'] = row.img['src']
    article['content'] = get_content(BaseURL + row.a['href'])

    articles.append(article)

# write json to the file
with codecs.open('out.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=4, sort_keys=False, ensure_ascii=False)

# write xml to the file
create_xml(articles)

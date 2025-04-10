# html code
# html_doc = """<html><head><title>Welcome to geeksforgeeks</title></head>
# <body>
# <p class="title"><b>Geeks</b></p>


# <p class="body">geeksforgeeks a computer science portal for geeks
# <p class="body">geeksforgeeks a computer science portal for geeks
# </body>
# """

# # import module
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(html_doc, "lxml")
# print(soup)
# print("\n")

# classes = soup.find(class_ = "body")  # finding by class



# ---------------------------------------------- Get all the classes in the whole html doc ----------------------------------------------
# from bs4 import BeautifulSoup
# import requests as rq

# URL = "https://www.geeksforgeeks.org/"

# class_list = set()

# page = rq.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")

# tags = set()

# for tag in soup.find_all():
#     tags.add(tag.name)


# for tag in tags:
#     for t in soup.find_all(tag):
#         if t.has_attr("class"):
#             class_list.add(" ".join(t["class"]))

# print(class_list)


# ---------------------------------------------- Searching By Text ----------------------------------------------
# from bs4 import BeautifulSoup
# import requests as rq

# URL = "https://www.geeksforgeeks.org/caching-page-tables/"

# page = rq.get(URL)

# soup = BeautifulSoup(page.content, "lxml")

# text = "page table base register (PTBR)"

# Method 1
# child_soup = soup.find_all("strong")

# for strong in child_soup:
#     if strong.string == text:
#         print(strong)

# Method2
# child_soup = soup.find_all("strong", string=text)
# for child in child_soup:
#     print(child)
    
# Method3
# gfg = soup.find_all(lambda tag: tag.name == "strong" and text in tag.text)
# print(gfg)


# from bs4 import BeautifulSoup
# import requests as rq

# URL = "https://www.geeksforgeeks.org/caching-page-tables/"
# result_set = rq.get(URL)

# soup = BeautifulSoup(result_set.text,"html.parser")

# h3s = soup.find_all("h3")
# for h3 in h3s:
#     print(h3.text)
#     print(h3.string)
#     print(h3.getText())

# URL = "https://www.windy.com/-Waves-waves?waves,22.431,79.750,6"
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# result_set = rq.get(URL, headers=headers)
# soup = BeautifulSoup(result_set.content,"html.parser")
# print(soup.prettify())

# weather = soup.find(class_="sw-wrapper svelte-152pmjt")
# print(weather)


# -------------------- Getting Tag name ----------------------------
# from bs4 import BeautifulSoup 
  
# # Initialize the object with a XML 
# soup = BeautifulSoup(''' 
#     <root> 
#         <name_of_tag>the first strong tag</name_of_tag> 
#     </root> 
#     ''', "lxml")

# tag = soup.name_of_tag
# print(tag)
# print(tag.name)
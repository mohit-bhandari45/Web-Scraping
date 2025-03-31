import requests as rq
from bs4 import BeautifulSoup

with open("sample.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, "html.parser")

print(soup.title)

# for link in soup.find_all("a"):
#     print(link.get("href"))
#     print(link.get_text())

# print(soup.select("div.italic"))
# print(soup.select("span#italic"))
# print(soup.span.get("class"))

# print(soup.find(class_="italic"))

# for child in soup.find(class_="container").children:
#     print(child)

# i = 0
# for parent in soup.find(class_="box").parents:
#     i+=1
#     print(parent)
#     if(i==3):
#         break

# cont = soup.find(class_="container")
# cont.name = "span"
# cont["class"] = "myclass class3"
# cont.string = "I am Evil"
# print(cont)

# ulTag = soup.new_tag("ul")

# liTag = soup.new_tag("li")
# liTag.string = "Hey Home"
# ulTag.append(liTag)

# liTag = soup.new_tag("li")
# liTag.string = "Hey About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)
# with open("modified.html", 'w') as f:
#     f.write(str(soup))


# cont = soup.find(class_="container")
# print(cont.has_attr("editable"))

def has_class_but_not_id(tag):
    return not tag.has_attr("class") and not tag.has_attr("id")

def has_content(tag):
    return tag.has_attr("content")

result = soup.find_all(has_content)
print(result)
# for result in results:
#     print(result, "\n\n")
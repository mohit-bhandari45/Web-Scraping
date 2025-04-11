from bs4 import BeautifulSoup
from collections import defaultdict
import requests as rq

res = rq.get("https://elementor.com/products/hello-theme/")

soup = BeautifulSoup(res.content, "lxml")

el = soup.select(".elementor-cta")
# print(el[0].contents)  ## like a childnodes in html dom

# childs = el[0].children
# for child in childs:
    # print(child)  ## like a .children in html dom

# print(el[0].next_sibling)  like .nextSibling in htmldom
# nexts = el[0].next_siblings
# for sib in nexts:
#     print(sib)

# print(el[0].previous_sibling)
# prevs = el[0].previous_siblings
# for sib in prevs:
    # print(sib)

# print(el[0].getText())   # similar to innerHTML

# desc = el[0].descendants  ## like this .querySelector("*")
# for d in desc:
#     print(d)

# strs= el[0].stripped_strings  # removing spaces
# for str in strs:
#     print(str)

# print(el[0].parent)   # like a .parentElement

# parents = el[0].parents
# for parent in parents:
#     print(parent)
#     print("\n")


descs = el[0].descendants
for desc in descs:
    print(desc)
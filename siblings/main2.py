from bs4 import BeautifulSoup

html_doc = """
  
<html><head><title>Geeks For Geeks</title></head>
  
<body>
  
<p class="title"><b>most viewed courses in GFG,its all free</b></p>
 
 
  
  
  

<p class ="prog">Top 5 Popular Programming Languages</p>
 
 
  
  
  
  
<a href="https://www.geeksforgeeks.org/java-programming-examples/" \
class="prog" id="link1">Java</a>
<a href="https://www.geeksforgeeks.org/cc-programs/" class="prog" \
id="link2">c/c++</a>
<a href="https://www.geeksforgeeks.org/python-programming-examples/"\
class="prog" id="link3">Python</a>
<a href="https://https://www.geeksforgeeks.org/introduction-to-javascript/"\
class="prog" id="link4">Javascript</a>
<a href="https://www.geeksforgeeks.org/ruby-programming-language/" \
class="prog" id="link5">Ruby</a>
  
  
  
  
 
 
<p>according to an online survey. </p>
 
 
  
  
  
  
<p class="prog"> Programming Languages</p>
 
 
  
  
  
  
</body></html>
  
"""

soup = BeautifulSoup(html_doc, "lxml")

# these are unique tags and will be present only one in the entire doc
# print(soup.html)
# print(soup.head)
# print(soup.title)
# print(soup.body)

# getting any other tag- These will only fetch the first tag among all present
# print(soup.b)
# print(soup.find("b"))
# the above two will give the same output(give the first of there name)

# all_a = soup.find_all("a")
# for a in all_a:
    # print(a)

# b = soup.head
# print(b.contents)
# childs = b.children
# for child in childs:
#     print(child)

# descendents
# descs = b.descendants
# print(descs)
# for desc in descs:
    # print(desc)


# print(soup.title.string)
# print(soup.title.parent)


# parents = soup.title.parents
# for parent in parents:
#     print(parent)
#     print("\n")
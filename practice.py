from bs4 import BeautifulSoup

with open("./sample.html", "r") as f:
    content = f.read()
    # There are 4 objects in BeautifulSoup
    # 1. Soup Object(The whole parsed html file)
    # soup = BeautifulSoup(content, "html.parser")
    # print(soup)

    # 2. Tag similar to html tag, but returns the first tag from the entire doc
    # tag = BeautifulSoup(content, "html.parser")
    
    # manipulating tag.name
    # t = tag.div  # give the first div tag
    # print(t)
    # print(t.name)
    # print(type(t))
    # t.name = "a"  # changing the name of the tag
    # print(t)

    # manipulating tag.attributes
    # print(t)
    # print(t.attrs)
    # print(t["class"])
    # t["class"] = "Sex"
    # print(t)
    # del t["class"]
    # print(t)

    # 3. Navigable String
    # st = BeautifulSoup(content, "html.parser")
    # d = st.div
    # print(d.string)
    # print(type(d.string))
    # print(d.getText())
    # print(type(d.getText()))

    # 4. Comment Object
    st = BeautifulSoup(content, "html.parser")
    d = st.div
    comment = d.string
    print(type(comment))
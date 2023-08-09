from bs4 import BeautifulSoup
import os
from sys import argv

FILE = "homepage.html"
OUT_FILE = "out.html"

def get_types():
    links = get_links();
    types = [];
    for link in links:
        exists=False
        link_type = link.get("content_type")
        for con_type in types:
            if link_type == con_type:
                exists=True
                break
        if exists == False:
            types.append(link_type)
    return types

def get_links():
    soup = get_soup()
    links = soup.find_all("a")
    return links

def show_links():
    links = get_links()
    for link in links:
        print(f"{link.get('index')}:\
[{link.get('content_type')}]\
{link.text}")

def get_soup():
    file = open(FILE, 'r')
    html = file.read()
    file.close()
    soup = BeautifulSoup(html, 'lxml')
    return soup 

def get_link(link_id):
    soup = get_soup()
    links = soup.find_all(index=link_id)
    for link in links:
        return link.text
    return None

def add_link(link, name, content_type):
    cout = len(get_links())+1
    file = open(FILE, "r")
    lines = file.readlines()
    file.close()
    file_out = open(OUT_FILE, "a+");
    for line in lines:
        if line != "</body>\n":
            file_out.write(line)
        else:
            file_out.write(f"<p>{content_type}: <a index='{cout}'\
content_type='{content_type}'\
href='{link}'>{name}</a></p>\n\
</body>\n</html>\n")
            break
    file_out.close()
    remove_file()


def remove_file():
    if os.path.isfile(FILE):
        os.remove(FILE)
        os.rename(OUT_FILE, FILE) 
    else:
        return None

def delete_link(index):
    if get_link(index) != None:
        file = open(FILE, "r")
        lines = file.readlines()
        file.close()
        file_out = open(OUT_FILE, "a+")
        for line in lines:
            if line.find("<a") !=-1 and line.find(f"index='{index}'") !=-1:
                continue
            file_out.write(line)
        file_out.close()
        remove_file()

def sort():
    types = get_types()
    file = open(FILE, 'r')
    lines = file.readlines()
    file.close()
    out = open(OUT_FILE, 'a+')
    header=[]
    for line in lines:
        out.write(line)
        if line.find("<body") != -1:
            break
    for c_type in types:
        for line in lines:
            if line.find(c_type) != -1:
                out.write(line)
    out.write("</body>\n</html>\n")
    out.close()
    remove_file()

def main():
    if (len(argv) == 2):
        if (argv[1] == "show"):
            show_links()
        elif (argv[1] == "sort"):
            sort()
        else:
            _, index = argv
            delete_link(index)
    elif (len(argv) == 4):
        _, link, name, content_type = argv
        add_link(link, name, content_type)

if __name__ == "__main__":
    main()

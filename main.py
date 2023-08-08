from bs4 import BeautifulSoup
import os
from sys import argv

FILE = "homepage.html"
OUT_FILE = "out.html"

def get_links():
    soup = get_soup()
    links = soup.find_all("a")
    return links

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

def add_link(link, name):
    cout = len(get_links())+1
    file = open(FILE, "r")
    lines = file.readlines()
    file.close()
    file_out = open(OUT_FILE, "a+");
    for line in lines:
        if line != "</body>\n":
            file_out.write(line)
        else:
            file_out.write(f"<a index='{cout}' href='{link}'>{name}</a>\n</body>\n</html>\n")
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
            if line[1] == "a" and line[10] == index:
                    continue
            else:
                file_out.write(line)
        file_out.close()
        remove_file()

def main():
    if (len(argv) == 2):
        _, index = argv
        delete_link(index)
    elif (len(argv) == 3):
        _, link, name = argv
        add_link(link, name)

if __name__ == "__main__":
    main()

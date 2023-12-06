import requests
from bs4 import BeautifulSoup

def main():
    url = "https://en.wikipedia.org/wiki/Tesco"
    responce = requests.get(url)
    soup = BeautifulSoup(responce.content, "html.parser")
    elements = soup.find_all(string="Clubcard")
    print(f"elements {len(elements)}")
    #print(responce.content)
    print(f"scraping: {url}")
    #print(responce)

if __name__ == "__main__":
    main()


"""print(len(elements))
    print(responce.content)"""
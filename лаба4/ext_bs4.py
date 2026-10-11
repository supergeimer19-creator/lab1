from bs4 import BeautifulSoup

def test_bs4():
    html = "<h1>Привіт, світ!</h1>"
    soup = BeautifulSoup(html, "html.parser")
    print(f"beautifulsoup4: Знайдений текст -> {soup.h1.text}")
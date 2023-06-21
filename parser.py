import requests
from bs4 import BeautifulSoup


links = (
    "https://internetowykantor.pl/kursy-walut/",
    "https://www.walutomat.pl/",
    "https://ekantor.pl/kursy-walut/"
)


def parser_1(currency: str):
    response = requests.get(url=links[0])
    soup = BeautifulSoup(response.text, "lxml")

    table = soup.find("table")

    row = table.find("tbody").find("tr", attrs={"data-currency-id": f"{currency}_PLN"})

    buy = row.find("span", attrs={"data-rates-direction": "buy"}).text
    sell = row.find("span", attrs={"data-rates-direction": "sell"}).text

    return f"[link]({response.url})", buy, sell


def parser_2(currency: str):

    buy = None
    sell = None

    response = requests.get(url=links[1])
    soup = BeautifulSoup(response.text, "lxml")

    section = soup.find("section", attrs={"class": "exchange-rates-section"})
    exchange_container = section.find("div")
    rows = exchange_container.find("div", attrs={"class": "row exchange-rates-row"})

    values = rows.find_all("a")

    for i in values:
        if i.find("span").text == currency:
            buy = i.find("span", attrs={"class": "buy"}).text
            sell = i.find("span", attrs={"class": "sell"}).text
            break
    return f"[link]({response.url})", buy, sell


def parser_3(currency: str):
    buy = None
    sell = None

    response = requests.get(url=links[2])
    soup = BeautifulSoup(response.text, "lxml")

    exchanges = soup.find("table").find_all("tr")[1:]

    for i in exchanges:
        if i.find("td").find("span", attrs={"class": "currency"}).text == currency:
            sell = i.find("td", attrs={"class": "cell-sell"}).text
            buy = i.find("td", attrs={"class": "cell-buy"}).text
            break
    return f"[link]({response.url})", *buy.split(), *sell.split()



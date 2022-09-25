import requests
from bs4 import BeautifulSoup
import csv


def crawling_check(enter: dict) -> csv:
    href = list()
    site = list()

    values = list(enter.values())

    for url in values:
        try:
            res = requests.get(url, timeout=9.0).text
        except:
            continue
        soup = BeautifulSoup(res, "html.parser")
        links = soup.find_all("a")
        for link in links:
            a = link.get("href")
            # aタグが空の場合はスキップ
            if a is None:
                continue
            # URLが同一のサイト内の場合に追加
            if a.startswith(url[:-1]):
                href.append(a)
        # URLが見つからなかった場合はスキップ
        if len(href) == 0:
            continue
        site.append(href)
        href = list()

    return site

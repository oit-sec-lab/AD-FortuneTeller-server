import csv
import json

import requests
import tldextract
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.url = None
        self.href = list()
        self.site = list()

    def clawring_check(self, enter: dict) -> csv:
        for url in enter.values():
            self.url = url
            self.href.append(url)

            try:
                headers = {"User-Agent": "Mozilla/5.0"}
                res = requests.get(url, timeout=9.0, headers=headers).text
            except:
                print("clawring error: ", url)
            else:
                soup = BeautifulSoup(res, "html.parser")
                links = soup.find_all("a")
                self.href.append(self.extract(links))
            finally:
                self.site.append(self.href)
                self.href = list()

        return self.site

    def extract(self, links: list[str]) -> None:
        for link in links:
            # aタグの取得
            a = link.get("href")

            # aタグが空の場合はスキップ
            if a is None:
                continue

            # httpから始まらない場合はスキップ
            if not a.startswith("http"):
                continue

            # .pdfはスキップ
            if a.endswith(".pdf"):
                continue

            # urlから\r\nを削除
            a = a.replace("\r", "").replace("\n", "")

            # ドメインを取得
            # 例: https://www.google.com/ -> google.com
            url_domain = ".".join(tldextract.extract(self.url)[1:])
            a_domain = ".".join(tldextract.extract(a)[1:])

            # ドメインが同じ場合のみリストに追加
            if url_domain == a_domain:
                self.href.append(a)

            # href内の重複を削除
            self.href = list(dict.fromkeys(self.href))


if __name__ == "__main__":
    # TODO: read json
    with open("ok.json", "r") as f:
        enter = json.load(f)

    site = Crawler().clawring_check(enter)

    # TODO: output
    with open("url_test.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(site)

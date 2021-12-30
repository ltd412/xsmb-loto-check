import requests
from bs4 import BeautifulSoup
import argparse
from typing import List
from collections import Counter
from datetime import datetime, timedelta


def getLottery():
    prize = []
    url = "http://ketqua1.net"
    ses = requests.Session()
    resp = ses.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, features="html.parser")

    for tag in soup.select("div[id]"):
        if "rs" in tag["id"]:
            prize.append(tag.text)
    return prize


def lotteryResult(lst: List[str]) -> str:
    timeline = datetime.now()
    if timeline < timeline.replace(hour=18, minute=35):
        timeline = timeline - timedelta(days=1)
    else:
        timeline

    lottery ="""
    KẾT QUẢ SỔ XỐ MIỀN BẮC NGÀY {}
    kÝ HIỆU:    {}
    Giải ĐB: \t {}
    Giải nhất: \t {}
    Giải nhì: \t {} - {}
    Giải ba: \t {} - {} - {}
    \t\t {} - {} - {}
    Giải bốn: \t {} - {} - {} - {}
    Giải năm:\t {} - {} - {}
    \t\t {} - {} - {}
    Giải sáu: \t {} - {} - {}
    Giải bảy: \t {} - {} - {} - {}
    """.format(timeline.strftime("%d - %m - %Y"), *lst)
    return lottery


def solve(numbers, daily_prize):
    last_2_digit = [number[-2:] for number in daily_prize]
    win_number = []
    for number in last_2_digit:
        if number in str(numbers):
            win_number.append(number)
    win_number.sort()

    if win_number:
        list_prizes = {key: f"{value} nháy" for key, value in Counter(win_number).items()}
        print("Trúng lô", list_prizes)
    else:
        print("CÒN THỞ CÒN GỠ")
        print(lotteryResult(daily_prize))
 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="*")
    args = parser.parse_args()
    prize = getLottery()
    solve(args.numbers, prize)


if __name__ == '__main__':
    main()

import os
import sys
from datetime import date

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

cookies = {"session": os.environ.get("AOC_COOKIE")}
today = date.today()

if len(sys.argv) == 1:
    url = f"https://adventofcode.com/{today.year}/day/{today.day}"

elif len(sys.argv) == 2:
    url = f"https://adventofcode.com/{today.year}/day/{sys.argv[1]}"

else:
    raise Exception("Need date argument. Or none for today's date.")

r = requests.get(url, cookies=cookies)
soup = BeautifulSoup(r.content, "html.parser")

codes = soup.find_all("code")
max_len = 0
test_code = ""

for code in codes:
    if len(code.text) > max_len:
        max_len = len(code.text)
        test_code = code.text

print(test_code.rstrip())

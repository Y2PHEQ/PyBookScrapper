<p align="center">
  <a href="https://github.com/sintxcs">
    <img src="https://raw.githubusercontent.com/sintxcs/PyBookScrapper/main/assets/PyBookScrapper.jpg" alt="Logo">
  </a>
  <p align="center">
    A Python module that can scrape the name and the year of a Facebook account. Friends and followers count using Facebook tokens.<b>
</p>

## Terminal Installation
```ruby
pip3 install PyBookScrapper
```

## Importing the module in your script
```python
try:
    import PyBookScrapper
except ModuleNotFoundError:
    os.system("pip3 install PyBookScrapper")
    import PyBookScrapper
```

## Year Scrapper
```python
from PyBookScrapper import Scrape_Year

Input Example:
uid = "61553865513324"
print(f"ACCOUNT YEAR: {Scrape_Year(uid)}")

Output Example:
Account Year: 2023
```

## Followers Scrapper
```python
from PyBookScrapper import Scrape_Followers

Input Example:
token = "EAADmFOBtT9aM0******VD3MBKYOrzIg2Bd4nzlhstptx554******4c9PVGsx4R9JU89a7iy0GybnUZBLrIUy0wIEsIhuh2k2XNvTYOfZAGnY4Hp*******CxknZBq1L8427X2aBIDpbntW5XGXzqNzPBwNElztX5qF*****ZA68vrx1NQZDZD"

print(f"Followers: {Scrape_Followers(token)}")

Output Example:
Followers: 50
```

## Friends Scrapper
```python
from PyBookScrapper import Scrape_Friends

Input Example:
token = "EAADmFOBtT9aM0******VD3MBKYOrzIg2Bd4nzlhstptx554******4c9PVGsx4R9JU89a7iy0GybnUZBLrIUy0wIEsIhuh2k2XNvTYOfZAGnY4Hp*******CxknZBq1L8427X2aBIDpbntW5XGXzqNzPBwNElztX5qF*****ZA68vrx1NQZDZD"

print(f"Friends: {Scrape_Friends(token)}")

Output Example:
Friends: 25
```

## Name Scrapper
```python
from PyBookScrapper import Scrape_Name

Input Example:
token = "EAADmFOBtT9aM0******VD3MBKYOrzIg2Bd4nzlhstptx554******4c9PVGsx4R9JU89a7iy0GybnUZBLrIUy0wIEsIhuh2k2XNvTYOfZAGnY4Hp*******CxknZBq1L8427X2aBIDpbntW5XGXzqNzPBwNElztX5qF*****ZA68vrx1NQZDZD"

print(f"Name: {Scrape_Name(token)}")

Output Example:
Name: sintacs.
```

## Social Links
[Facebook](https://facebook.com/sintxcs) • [Telegram](https://t.me/syntxcs)

![Image](https://raw.githubusercontent.com/sintxcs/Facebook_scrapper/main/assets/facebook_scrapper.jpg)

## Terminal Installation
```ruby
pip3 install facebook_scrapper
```

## Importing the module in your script
```python
try:
    import facebook_scrapper
except ModuleNotFoundError:
    os.system("pip3 install facebook_scrapper")
    import facebook_scrapper
```

## Year Scrapper
```python
from facebook_scrapper import scrape_year

Input Example:
uid = "61553865513324"
print(f"ACCOUNT YEAR: {scrape_year(uid)}")

Output Example:
ACCOUNT YEAR: 2023
```

## Followers Scrapper
```python
from facebook_scrapper import scrape_followers

Input Example:
token = "EAADmFOBtT9aM0******VD3MBKYOrzIg2Bd4nzlhstptx554******4c9PVGsx4R9JU89a7iy0GybnUZBLrIUy0wIEsIhuh2k2XNvTYOfZAGnY4Hp*******CxknZBq1L8427X2aBIDpbntW5XGXzqNzPBwNElztX5qF*****ZA68vrx1NQZDZD"

print(f"FOLLOWERS: {scrape_followers(token)}")

Output Example:
FOLLOWERS: 50
```

## Friends Scrapper
```python
from facebook_scrapper import scrape_friends

Input Example:
token = "EAADmFOBtT9aM0******VD3MBKYOrzIg2Bd4nzlhstptx554******4c9PVGsx4R9JU89a7iy0GybnUZBLrIUy0wIEsIhuh2k2XNvTYOfZAGnY4Hp*******CxknZBq1L8427X2aBIDpbntW5XGXzqNzPBwNElztX5qF*****ZA68vrx1NQZDZD"

print(f"FRIENDS: {scrape_friends(token)}")

Output Example:
FOLLOWERS: 25
```

## Social Links
[Facebook](https://facebook.com/sintxcs) • [Telegram](https://t.me/syntxcs)

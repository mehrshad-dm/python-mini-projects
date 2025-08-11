import requests
import bs4

main_link = requests.get("https://realpython.com/")
data = main_link.text

regular_data = bs4.BeautifulSoup(data, "html.parser")
web_title = regular_data.select_one("title").text.strip()
print(web_title)

web_list = regular_data.select(".h2")
for item in web_list:
    print(item.text)

picture = regular_data.select(
    ".h-100 > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
)

for pic in picture:
    print(pic["src"])

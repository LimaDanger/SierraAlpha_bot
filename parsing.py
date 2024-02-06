import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}

for count in range(1, 8):
		sleep(3)
		url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

		response = requests.get(url, headers=headers)

		soup = BeautifulSoup(response.text, "lxml") 
		data = soup.findAll("div", class_="w-full rounded border")

		for i in data:
				card_url = "https://scrapingclub.com" + i.find("a").get("href")
				list_card_url.append(card_url)


for card_url in list_card_url:

	response = requests.get(card_url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml") 
	card_url = soup.find("div", class_="my-8 w-full rounded border")
	name = card_url.find("h3").text
	price = card_url.find("h4").text
	description = card_url.find("p").text
	image_url = "	https://scrapingclub.com" + card_url.find("img", class_="card-img-top").get("src")
	print(f"\n\n{name}\n{price}\n{description}\n{image_url}\n\n")


"""
name = i.find("h4").find("a").text.replace("\n", "")
				price = i.find("h5").text
				image_url = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")    #	https://scrapingclub.com/static/img/90008-E.jpg

				print(f"\n\n{name}\n{price}\n{image_url}\n\n")
"""





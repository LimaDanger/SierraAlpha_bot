import requests
from bs4 import BeautifulSoup
from time import sleep



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}

def install_image(url):
	resp = requests.get(url, stream=True)
	r = open("C:\\Users\\Foxtrot\\Documents\\SierraAlpha_bot\\image\\" + url.split("/")[-1] , "wb")
	for value in resp.iter_content(102400):
		r.write(value)
	r.close()




# "функция генератор принимает текст со страниц сайта в lxml формате"
def get_url():

	# "цикл for считывает инфу с каждой страницы в промежутке от 1-7 включительно"
	for count in range(1, 8):
			url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

			response = requests.get(url, headers=headers)

			soup = BeautifulSoup(response.text, "lxml") 
			data = soup.findAll("div", class_="w-full rounded border")

			# "цикл for вытягивает ссылку на изображение в карточке товара и доплняет относительную ссылку для получения глобальной ссылки"
			for i in data:
					card_url = "https://scrapingclub.com" + i.find("a").get("href")
					yield card_url

  # "функция обращается в функцию-генератор (get_url) для получения lxml текста со страниц сайта чтобы вытянуть из него нужные данные и записать в переменные"
def fuction_get():
	for card_url in get_url():

		response = requests.get(card_url, headers=headers)
		sleep(1.5)
		soup = BeautifulSoup(response.text, "lxml") 
		card_url = soup.find("div", class_="my-8 w-full rounded border")
		name = card_url.find("h3").text
		price = card_url.find("h4").text
		description = card_url.find("p").text
		image_url = "	https://scrapingclub.com" + card_url.find("img", class_="card-img-top").get("src")
		install_image(image_url)
		yield name, price, description, image_url






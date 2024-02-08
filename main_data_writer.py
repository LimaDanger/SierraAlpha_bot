#"Это основной исполняемый файл, запускаем его!"

import xlsxwriter
from Parsing_function import fuction_get


def writer(parametr):
	book = xlsxwriter.Workbook(r"C:\Users\Foxtrot\Documents\SierraAlpha_bot\data.xlsx")
	page = book.add_worksheet("товар")


	row = 0
	column = 0

	page.set_column("A:A", 20)
	page.set_column("B:B", 20)
	page.set_column("C:C", 20)
	page.set_column("D:D", 20)

	for item in parametr:
		page.write(row, column, item[0])
		page.write(row, column+1, item[1])
		page.write(row, column+2, item[2])
		page.write(row, column+3, item[3])
		row += 1

	book.close()

# "запускает функцию get запроса (array) на получение данных с парсера"
	
array = fuction_get()
writer(array)

print("Скрипт успешно выполнен.")
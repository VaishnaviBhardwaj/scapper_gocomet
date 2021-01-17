from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def Scrapping(str):

	PATH ="C:\Program Files (x86)\chromedriver.exe"

	driver =webdriver.Chrome(PATH)

	driver.get("https://medium.com/search?q="+str) 
	elements=driver.find_elements_by_class_name("graf--title")
	output=[]

	for element in elements:
		output.append(element.text)

	return output
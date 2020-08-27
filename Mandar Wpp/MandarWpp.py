import datetime
import socket
from time import sleep
from webbrowser import get

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

no_of_message = 1

def element_presence(by, xpath, time,driver):
	element_present = EC.presence_of_element_located((By.XPATH, xpath))
	WebDriverWait(driver, time).until(element_present)


def is_connected():
	try:
		# conectarse al host: nos dice si el host es en realidad
		# accesible
		socket.create_connection(("www.google.com", 80))
		return True
	except:
		is_connected()


def send_whatsapp_msg(phone_no, text,driver):
	driver.get(
		"https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
	try:
		driver.switch_to_alert().accept()
	except Exception as e:
		pass

	try:
		element_presence(
			By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30, driver)
		txt_box = driver.find_element(
			By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		global no_of_message
		for x in range(no_of_message):
			txt_box.send_keys(text)
			txt_box.send_keys("\n")

	except Exception as e:
		print("invailid phone no :"+str(phone_no))


def main():

	moblie_no_list = [543512461390]
	horaDeEnvio = 00	
	minutoDeEnvio = 42
	print("{:02d}:{:02d}".format(horaDeEnvio,minutoDeEnvio))
	horasEspera = 0
	minutosEspera = 0
	
	while(True):
	
		if (horaDeEnvio == datetime.datetime.now().hour):
			if(minutoDeEnvio >= datetime.datetime.now().minute):
				horasEspera = 0
				minutosEspera = minutoDeEnvio - datetime.datetime.now().minute
			else:
				horasEspera = 23
				minutosEspera = 60 + minutoDeEnvio - datetime.datetime.now().minute
	
		elif (horaDeEnvio > datetime.datetime.now().hour):
			if(minutoDeEnvio >= datetime.datetime.now().minute):
				horasEspera = horaDeEnvio - datetime.datetime.now().hour
				minutosEspera = minutoDeEnvio - datetime.datetime.now().minute
			else:
				horasEspera = horaDeEnvio - datetime.datetime.now().hour - 1
				minutosEspera = 60 + minutoDeEnvio - datetime.datetime.now().minute

		elif (horaDeEnvio < datetime.datetime.now().hour):
			if(minutoDeEnvio >= datetime.datetime.now().minute):
				horasEspera = 24 + horaDeEnvio - datetime.datetime.now().hour
				minutosEspera = minutoDeEnvio - datetime.datetime.now().minute
			else:
				horasEspera = 24 + horaDeEnvio - datetime.datetime.now().hour - 1
				minutosEspera = 60 + minutoDeEnvio - datetime.datetime.now().minute
	
		print ("Esperar %d horas y %d minutos"%(horasEspera,minutosEspera))
		sleep(horasEspera*3600 + minutosEspera*60)

		driver = webdriver.Chrome(executable_path="chromedriver.exe", port=1)
		driver.get("http://web.whatsapp.com")
		sleep(10)
		cambios = open("Cambios.txt", 'r')
		for moblie_no in moblie_no_list:        
			try:
				send_whatsapp_msg(moblie_no, cambios.read(),driver)
			except Exception as e:
				sleep(10)
				is_connected()
		driver.quit()
		cambios.close()

if __name__ == '__main__':
	main()

import requests, os, time, signal
from colorama import *

Main_Colour = Fore.LIGHTGREEN_EX
Secondary_Colour = Fore.WHITE

class Discord_Webhook():

	def Quit_Program(sig, frame):
		print(Secondary_Colour+"["+Main_Colour +"Hades/Discord"+Secondary_Colour+"]: Exiting Program")
		os._exit(0)

	def Send(Webhook_Url, Contents, Text):
		Discord_Request = requests.post(Webhook_Url, data=Contents) # sends data to webhook
		try:
			print(Secondary_Colour+"["+Main_Colour +"Hades/Discord"+Secondary_Colour+"]: Getting Rate Limited, Waiting " + str(Discord_Request.json()["retry_after"]) + " ms Before Rertying")
			time.sleep(Discord_Request.json()["retry_after"]/1000)
		except:
			print(Secondary_Colour+"["+Main_Colour +"Hades/Discord"+Secondary_Colour+"]: Successfully Sent")

	def Main():
		Webhook_Url = input("Enter Webhook Url: ")
		Text = input("Enter Text To Send ")
		Bot_Name = input("Enter Word To Set Bot Name To: ")
		Bot_Image = input("Enter Url To Set Bot Image To: ")

		Contents = {
    		"content": Text,
    		"username": Bot_Name,
  		"avatar_url": Bot_Image
		}
		while True:
			Discord_Webhook.Send(Webhook_Url, Contents, Text)


signal.signal(signal.SIGINT, Discord_Webhook.Quit_Program)
Discord_Webhook.Main()


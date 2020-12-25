import requests, os, time, signal
from colorama import *

Main_Colour = Fore.LIGHTGREEN_EX
Secondary_Colour = Fore.WHITE

class Discord_Webhook_Spammer():

	def Quit_Program(sig, frame):
		print(Secondary_Colour+"["+Main_Colour +"Hades/Discord"+Secondary_Colour+"]: Exiting Program")
		os._exit(0)

	def Spam(Webhook_Url, Contents, Spamed_Text):
		Discord_Request = requests.post(Webhook_Url, data=Contents) # sends data to webhook
		try:
			print(Secondary_Colour+"["+Main_Colour +"Hades/Discord"+Secondary_Colour+"]: Getting Rate Limited, Waiting " + str(Discord_Request.json()["retry_after"]) + " ms Before Rertying")
			time.sleep(Discord_Request.json()["retry_after"]/1000)
		except:
			print(Secondary_Colour+"["+Main_Colour +"Hades/Discord"+Secondary_Colour+"]: Successfully Sent")

	def Main():
		Webhook_Url = input("Enter Webhook Url: ")
		Spamed_Text = input("Enter Text To Spam ")
		Bot_Name = input("Enter Word To Set Bot Name To: ")
		Bot_Image = input("Enter Url To Set Bot Image To: ")

		Contents = {
    		"content": Spamed_Text,
    		"username": Bot_Name,
  		"avatar_url": Bot_Image
		}
		while True:
			Discord_Webhook_Spammer.Spam(Webhook_Url, Contents, Spamed_Text)


signal.signal(signal.SIGINT, Discord_Webhook_Spammer.Quit_Program)
Discord_Webhook_Spammer.Main()


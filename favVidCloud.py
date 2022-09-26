#!/usr/bin/python3
import os
from enum import Enum

#use file io to permantly store items later
#	for now just use a dictionary

class UserChoice(Enum):
	URL = 1
	FAV = 2
	MANAGE = 3
	QUIT = 4

favs = {"cat": "meows"}

def printMenu():
	print("Would you like to: ")
	print("1: Play Video by URL")
	print("2: Play Favourite Video")
	print("3: Manage Favourites")
	print("4: Quit")	

def printManageMenu():
	print("Which management function would you like")
	print("1: List Videos")
	print("2: Add Video")
	print("3: Remove Video")

def processManageChoice(choice):
	if choice == str(1):
		return listVideos(favs)
	return 

def manageVideos():
	return menu(1)

def menu(menuLevel):
	if(menuLevel) == 0:
		printMenu()
	else:
		printManageMenu()
	return parseInput(input("Choice: "))

#assuming properly formatted	
def parseInput(option):
	return option
		
def listVideos(videos):
	print("##Video Favourites##")
	for video in videos:
		print(video + ": " + videos[video])
	print("##End Favourites##")
	return
def playOnlineVideo(app, url):
	userCommand = app + " " + url
	os.system(userCommand)
	return
def playFavouriteVideo(app, url):
	return
def playVideo():
	return
def addVideo(url):
	return

playerChoice = "mpv"
while True:
	selection = menu(0)
	if selection == str(UserChoice.URL.value):
		playOnlineVideo(playerChoice, input("URL: "))
	elif selection == str(UserChoice.FAV.value):
		break
	#need to add a secondary menu to the one below (manage) 
	# currently will bypass it and just list for testing
	elif selection == str(UserChoice.MANAGE.value):
		#listVideos(favs)
		processManageChoice(manageVideos())
	elif selection == str(UserChoice.QUIT.value):
		break	
	

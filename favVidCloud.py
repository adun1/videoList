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

favs = {"cat": "meows", "Lipo Song": "https://www.youtube.com/watch?v=jYdaQJzcAcw"}

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
	elif choice == str(2):
		addVideo(input("Video Name: "), input("URL: "))
	elif choice == str(3):
		removeVideo(input("Video to be Removed: "))
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
def addVideo(name, url):
	favs[name] = url
	return

def removeVideo(name):
	del favs[name]
playerChoice = "mpv"
while True:
	selection = menu(0)
	if selection == str(UserChoice.URL.value):
		playOnlineVideo(playerChoice, input("URL: "))
	elif selection == str(UserChoice.FAV.value):
		listVideos(favs)
		playOnlineVideo(playerChoice, favs[input("Choice: ")])
	elif selection == str(UserChoice.MANAGE.value):
		processManageChoice(manageVideos())
	elif selection == str(UserChoice.QUIT.value):
		break	
	

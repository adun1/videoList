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

favs = {}

def printMenu():
	print("Would you like to: ")
	print("1: Play Video by URL")
	print("2: Play Favourite Video")
	print("3: Manage Favourites")
	print("4: Quit")	

def menu():
	printMenu()
	return parseInput(input("Choice: "))

#assuming properly formatted	
def parseInput(option):
	return option
		
def listVideos():
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
	selection = menu()
	if selection == str(UserChoice.URL.value):
		playOnlineVideo(playerChoice, input("URL: "))
	elif selection == str(UserChoice.QUIT.value):
		break	

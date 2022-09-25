#!/usr/bin/python3

#use file io to permantly store items later
#	for now just use a dictionary

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
	if selection == "4":
		break	

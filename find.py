import requests, re, os, platform
from platform import system
# clear
if system() == 'Linux':
	os.system('clear')
elif system() == 'Windows':
	os.system('cls')
# banner
print ("""
  _____ _           _      _    _ _   _     _       _
 |  ___(_)_ __   __| |    / \  | | | | |   (_)_ __ | | __
 | |_  | | '_ \ / _` |   / _ \ | | | | |   | | '_ \| |/ /
 |  _| | | | | | (_| |  / ___ \| | | | |___| | | | |   <
 |_|   |_|_| |_|\__,_| /_/   \_\_|_| |_____|_|_| |_|_|\_\

                   (c) Evil Twin
""")
# get url
url = input('Enter a URL (with http): ')
# connect to the url
website = requests.get(url)
# read html
html = website.text
# use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
# output links
for link in links:
    print("[*]", link[0])

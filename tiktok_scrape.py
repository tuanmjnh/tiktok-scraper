import argparse
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
from urllib.request import urlopen

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {
        # Please get this data from the console network activity tool
        # This is explained in the video :)
    }

    headers = {
        # Please get this data from the console network activity tool
        # This is explained in the video :)
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': '', # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
    }
    
    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"videos/{id}-{videoTitle}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break

# Help --help
# if(sys.argv[1]=="--help" or sys.argv[1]=="-h"):
    # print("Help Tools get all video from tiktok")
    # print("--url url channel")
    # print("--class class name from video")
    # print("--file write to file")
    # print("--delay delay scroll")
    # print("--help or -h show help tool")
    # sys.exit()

# parser input argument
parser = argparse.ArgumentParser()
parser.add_argument('--url', dest='url', type=str, help='url channel')
parser.add_argument('--class', dest='className', type=str, help='class name content')
parser.add_argument('--file', dest='file', type=int, help='write to file')
parser.add_argument('--delay', dest='delay', type=int, help='delay scroll')
args = parser.parse_args()

# Fix argument write file
if(args.file==None): args.file=0
# check input link channel
# if(args.url==None):
#     print("Please input link channel")
#     sys.exit()

# get channel key
regex = re.search(r'(?<=@)\w+', args.url)
channelName = regex.group(0)

# remove text links if exist
if os.path.exists(f"{channelName}.txt"):
  os.remove(f"{channelName}.txt")
#   os.rmdir(f"{channelName}.txt")

# print("STEP 1: Open Chrome browser")
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)
# Change the tiktok link
# driver.get("https://www.tiktok.com/@vantoan___")
driver.get(args.url)

# IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
# to 60 seconds, just enough time for you to complete the captcha yourself.
time.sleep(1)

# scroll_pause_time = 5
if(args.delay==None): args.delay=1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

# print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(args.delay)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

# this class may change, so make sure to inspect the page and find the correct class
className = "tiktok-vi46v1-DivDesContainer eih2qak4"
if(args.className!=None):
    className = args.className

script = "let l = [];"
script += r"let regex = /(^|.*)https:\/\/www.tiktok.com\/@(.*)\/video\/(.*|$)/;"
script += "document.getElementsByClassName(\""
script += className
# script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
script += "\").forEach(i=>{"
script += "var a = i.querySelector('a').href;"
script += "if(regex.test(a)) l.push(a);"
script += "});"
script += "return l;"

urlsToDownload = driver.execute_script(script)

# print(f"STEP 3: Time to download {len(urlsToDownload)} videos")
for index, url in enumerate(urlsToDownload):
    if(args.file>0):
        f = open(f"{channelName}.txt", "a") # a append, w overwrite 
        if(index==len(urlsToDownload)-1): f.write(f"{url}") 
        else: f.write(f"{url}|")
        f.close()
    print(url)
    # print(f"Downloading video: {index}: {url}")
    # downloadVideo(url, index)
    # time.sleep(10)
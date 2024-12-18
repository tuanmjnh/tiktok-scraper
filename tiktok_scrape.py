import argparse
import re
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
from urllib.request import urlopen
import csv
from datetime import datetime
import numpy as np

urlsFile = 'urls.txt'
linksFolder = 'links'


def pause(msg="Press the any key to continue..."): input(msg)


def stop(msg="Stop Application."): sys.exit(msg)


def ignore_exception(IgnoreException=Exception, DefaultVal=None):
    """ Decorator for ignoring exception from a function
    e.g.   @ignore_exception(DivideByZero)
    e.g.2. ignore_exception(DivideByZero)(Divide)(2/0)
    """
    def dec(function):
        def _dec(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except IgnoreException:
                return DefaultVal
        return _dec
    return dec


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
        'tt': '',  # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
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


def writeTextFile(args):
    f = open(args.output, "a")  # a append, w overwrite
    for i, u in enumerate(args.urlsToDownload):
        if args.count > -1 and i >= args.count:
            break
        if (i == len(args.urlsToDownload)-1):
            f.write(f"{u}") if args.multipe > 0 else f.write(f"{args.channelName}\t{u}")
        else:
            f.write(f"{u}{args.split}") if args.multipe > 0 else f.write(f"{args.channelName}\t{u}{args.split}")
    f.close()


def writeCSVFile(args):
    with open(args.output, 'a', newline='') as csvfile:
        fieldnames = ['No.', 'Channel', 'Url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if args.index == 1:
            writer.writeheader()
        for i, u in enumerate(args.urlsToDownload):
            if args.count > -1 and i >= args.count:
                break
            writer.writerow({'No.': i+1, 'Channel': args.channelName, 'Url': u})


def writeCSVFile2(args):
    with open(args.output, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        arr = np.array(args.urlsToDownload)
        csvFile = arr[:args.count] if args.count > -1 else arr
        csvFile = [f'https://www.tiktok.com/@{args.channelName}'] + csvFile.tolist()
        spamwriter.writerow(csvFile)


def getLink(args):
    # get channel key
    regex = re.search(r'(?<=@)\w+', args.url)
    args.channelName = regex.group(0)

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

    # Count scroll
    if hasattr(args, 'count') == False or args.count == None:
        args.count = -1

    # Index
    if hasattr(args, 'index') == False or args.index == None:
        args.index = 1

    # scroll_pause_time = 5
    if (args.delay == None):
        args.delay = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 0

    # print("STEP 2: Scrolling page")
    while i > args.count:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        time.sleep(1)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        time.sleep(args.delay)
        # print(screen_height * i, ' - ', scroll_height)
        i += 1
        if (screen_height * i) > scroll_height:
            break

    # this class may change, so make sure to inspect the page and find the correct class
    if (args.className == None):
        args.className = "css-1uqux2o-DivItemContainerV2"

    script = "let l = [];"
    script += r"let regex = /(^|.*)https:\/\/www.tiktok.com\/@(.*)\/video\/(.*|$)/;"
    script += "Array.from(document.getElementsByClassName(\""
    script += args.className
    # script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
    script += "\")).forEach(i=>{"
    script += "var a = i.querySelector('a').href;"
    script += "if(regex.test(a)) l.push(a);"
    script += "});"
    script += "return l;"

    args.urlsToDownload = driver.execute_script(script)

    if args.file > 0 and args.csv == 0:
        writeTextFile(args)
    elif args.file > 0 and args.csv == 1:
        writeCSVFile(args)
    elif args.file > 0 and args.csv > 1:
        writeCSVFile2(args)
    else:
        print(u)
        # print(f"Downloading video: {index}: {url}")
        # downloadVideo(url, index)
        # time.sleep(10)
    # Close browser
    driver.close()


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
parser.add_argument('--count', dest='count', type=int, help='number of link to get')
parser.add_argument('--csv', dest='csv', type=int, help='export to csv file')
parser.add_argument('--multipe', dest='multipe', type=int, help='Each channel is a file')
parser.add_argument('--split', dest='split', type=str, help='split character')
args = parser.parse_args()

# Fix arguments
if (args.file == None):
    args.file = 0
if (args.csv == None):
    args.csv = 0
if (args.multipe == None):
    args.multipe = 0
now = datetime.now()  # current date and time
args.output = now.strftime("%Y-%m-%d-%H-%M-%S-%f")

if args.multipe > 0:
    args.output = f"{linksFolder}/{args.index}.{args.channelName}"
else:
    args.output = f"{linksFolder}/{args.output}"
if args.csv > 0:
    args.output = f"{args.output}.csv"
else:
    args.output = f"{args.output}.txt"


# remove file links if exist
if os.path.exists(args.output):
    os.remove(args.output)

if (args.split == None):
    args.split = '\n'
# check input link channel
# if(args.url==None):
#     print("Please input link channel")
#     sys.exit()

# Make folder links
if os.path.exists(linksFolder) == False:
    os.mkdir(linksFolder)


# If exist argument url
if args.url != None:
    getLink(args)
    pause("Successful! Press the any key to close...")
    stop()
else:
    # Check File urls
    if os.path.exists(urlsFile) == False:
        print("No exist file 'urls.txt'")
        pause()
        stop()

    # Get File urls
    txt = open(urlsFile, "r")
    urls = txt.read().split('\n')
    # urlsOpts = []
    sint = ignore_exception(ValueError)(int)
    for i, u in enumerate(urls):
        # urlsOpts.append(url)
        opts = u.split()  # re.split(r'\t+', u)
        if (len(opts) > 1):
            opts[1] = sint(opts[1])
            # opts[1] = -1 if opts[1] == None else opts[1]
            time.sleep(3)
            args.url = opts[0]
            args.count = opts[1]
            args.index = i+1
            getLink(args)
        # urlsOpts.append(opts)
    # print(urlsOpts)

    pause("Successful! Press the any key to close...")
    stop()

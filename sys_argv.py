import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument('--url', dest='url', type=str, help='url channel')
parser.add_argument('--class', dest='className', type=str, help='class name content')
parser.add_argument('--file', dest='file', type=int, help='write to file')
args = parser.parse_args()
# print(args)
print ("Number of arguments:", len(vars(args)), "arguments.")
for i, arg in enumerate(vars(args)):
    print ("Index ",i,": ", arg)

print (args.className!=None)

# link = "https://www.tiktok.com/@vantoan___"
# m = re.search('(tiktok.*)\/(@.*)\/(video)\/(.*?((?=[&#?])|$))|(tiktok.*)\/(@.*)', link)
m = re.search(r'(?<=@)\w+', args.url)
print (m.group(0))

buggy_name = 'GeekflareE'
name = buggy_name[:-1]
print(name)
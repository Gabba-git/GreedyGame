import json,urllib2
import requests
from pprint import pprint
import sys
# sys.setdefaultencoding() does not exist, here!
# Script to exteact locations from ips 

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8') 

location = []
url = "http://freegeoip.net/json/"
file = open("ip.txt","r")
data = file.read()
data = data.split("\n")
file2 = open("ip2loc.txt","a")
j = 0;
for i in range(44002,len(data)):
	r = urllib2.Request(url+data[i].split(",")[0])
	r = urllib2.urlopen(r)
	r = r.read()
	r = json.loads(r)
	print i
	#print str(r["latitude"])+":"+str(r["longitude"]))
	location.append(str(r["latitude"])+":"+str(r["longitude"])+","+str(r["region_name"]))
	file2.write(str(data[i].split(",")[1].split(".")[0])+","+location[j]+"\n");
	j+=1

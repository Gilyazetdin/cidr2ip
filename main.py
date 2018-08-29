import requests
lines = open("ip.txt", "r").read().split("\n")

import re
ips = []

for i in range(len(lines)):
    ip = lines[i].split(".")
    r = requests.post("http://magic-cookie.co.uk/cgi-bin/iplist-cgi.pl", data = {
        "ipw" : ip[0],
        "ipx" : ip[1],
        "ipy" : ip[2],
        "ipz" : ip[3],
        "mask" : ip[4]
    })
    txt = r.text
    ips.append(re.findall(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", txt))
    
f = open("rez.txt", "w")
for i in ips:
    for j in i:
        count = 0
        for x in j:
            if count < 3:
                f.write(str(x) + ".")
                count += 1
            else:
                f.write(str(x))
        f.write("\n")
f.close()
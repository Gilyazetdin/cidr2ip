import os
import sys
import re
import requests

if(len(sys.argv) != 3):
    print("Usage: main.py <CIDRs> <Output file>")
    os._exit(-0)

API_ENDPOINT = "http://magic-cookie.co.uk/cgi-bin/iplist-cgi.pl"

cidrs  = open(sys.argv[1], "r").read().split("\n")[:-1] # Sorry, file should have newline at end :(
output = open(sys.argv[2], "w")
ips    = []

def CIDRToRequest(cidr):
    cidr = cidr.split(".")
    cidr.append(cidr[3].split("/")[1])
    cidr[3] = cidr[3].split("/")[0]
    return {
        "ipw":  cidr[0],
        "ipx":  cidr[1],
        "ipy":  cidr[2],
        "ipz":  cidr[3],
        "mask": cidr[4]
    }



def resolveCIDR(cidr):
    response = requests.post(API_ENDPOINT, CIDRToRequest(cidr)).text
    return re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", response)[2:]
    
for cidr in cidrs:
    print("Resolving {0}...".format(cidr))
    ips += resolveCIDR(cidr)

for ip in ips:
    output.write("{0}\n".format(ip))
output.close()

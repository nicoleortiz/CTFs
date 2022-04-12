import sys
import hashlib

ips = []
h = []

with open("quick.txt") as f:
	f = f.readlines()
	
	for l in f:
		l = l.split()
		i = l[-1].replace("\n","")
		if i not in ips:
			ips.append(i)
		
for ip in ips:
	hashit = hashlib.sha256(ip.encode('utf-8')).hexdigest()
	h.append(hashit)
	
f = open('all.txt', 'a')
for x in range(0, len(ips)):
	f.write(ips[x] + " " + h[x] + "\n")
f.close()
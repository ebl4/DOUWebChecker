import sys, re, os

if len(sys.argv) < 2:
	print ("Usage: "+sys.argv[0]+" [nmap_file.gnmap]")
	sys.exit(0)

with open(sys.argv[1], 'r') as nmap_file:
	found = False
	for line in nmap_file:
		if 'open' in line:
			if re.search("443/open".format(), line): # other cases could be implemented
				print ("https://" +line.split()[1])

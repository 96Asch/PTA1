#!/usr/bin/python
import GeoIP
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
out = open("../temp/landcodes.txt", "w")
with open("../temp/ipaddress.txt","r") as f:
    for line in f:
	line = line.rstrip('\n')
        land = gi.country_code_by_addr(line)
	temp = str(land)
	out.write(temp+'\n')
f.close()
out.close()

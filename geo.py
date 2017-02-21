#!/usr/bin/python
import GeoIP
file=open("p1.txt","r")
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
for line in file:
	test1 = gi.country_code_by_addr(line)
	print line
file.close()

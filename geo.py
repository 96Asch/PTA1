#!/usr/bin/python
import GeoIP
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
with open("p1.txt","r") as f:
    for line in f:
        test1 = gi.country_code_by_addr(line)
	test1 = test1.rstrip('\n')
	print(line)


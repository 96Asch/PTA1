#!/usr/bin/python
import GeoIP
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
out = open("landcodes", "w")
with open("ipaddress","r") as f:
    for line in f:
		line = line.rstrip('\n')
        land = gi.country_code_by_addr(line)
		out.write(land)
		print land


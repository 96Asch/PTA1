#!/usr/bin/python

import GeoIP
import sys
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

for line in sys.stdin:
	line = line.rstrip()
	print(gi.country_code_by_addr(line))


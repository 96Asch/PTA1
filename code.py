Filter 200

bzcat wc_day6_1.out.bz2 | grep -v " 200 "


Get land

bzcat wc_day6_1.out.bz2 | cut -f1 -d"-"

#!/usr/bin/python
#-*- coding. utf-8 -*-

from progress.bar import Bar

bar = Bar ('Crawling Web' ,max=100, suffix='%(percent)d%%')
for i in range(100):
	for i in range (100000):
		continue
	bar.next()
bar.finish()

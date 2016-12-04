#!/usr/bin/python
#-*- coding. utf-8 -*-

import csv     # imports the csv module
import sys


def main ():	
	
	tracker_name=[]
	tracker_url=[]
	tracker_type=[]

	reader = csv.reader (open ('trackers.csv','rb'), delimiter=";")
	for t_name, t_url, t_type in reader:
		
		tracker_name.append(str (t_name))
		tracker_url.append(str (t_url))
		tracker_type.append(str (t_type))
	
	print tracker_name[0] + ': ' + str(tracker_name[1:])
	print tracker_url[0] + ': ' + str(tracker_url[1:])
	print tracker_type[0] + ': '+ str(tracker_type[1:])

if  __name__ == '__main__':
	main()


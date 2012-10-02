# -*- coding: utf-8 -*-
#!/usr/bin/env python


from devotionals.models import Devotional
import csv
import sys


def print_help():
	"""Prints a helps message
	
	"""
	
	print "Usage: csvimport <file path>"


if __name__ == '__main__':
	
	num_arguments = len(sys.argv) - 1
	if num_arguments == 1:
	
		imported = 0 
		devotionals_reader = csv.reader(open(sys.argv[1], 'rb'), delimiter=',', quotechar='"')
		for row in devotionals_reader:
			try:
				Devotional.objects.create(title=row[0],
										month = row[1],
										day = row[2],
										body = row[3])
			except Exception, ex:
				print "Error importing row..."
			else:
				imported += 1
				
		print "%s rows imported ..." % imported
			
	else:
		print_help()
	

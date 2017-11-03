#! /usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
from pandas import ExcelWriter
from openpyxl import load_workbook
from openpyxl import __version__
import codecs,os,sys


###########################################################################################################################################

def remove_log(logfile):
	if os.path.isfile(logfile):
		os.remove(logfile)
		
remove_log('log.txt')
remove_log('done.txt')
	
file = codecs.open('log.txt','w',encoding="utf-8")

if not os.path.isfile('input.txt'):
	print ""
	print ""
	print "input.txt Not found"
	file.write("input.txt Not found" + '\n' + '\n')
	print ""
	print ""
	print "Please keep input.txt with tool"
	file.write("Please keep input.txt with tool" + '\n' + '\n' + "and try again ....")
	print ""
	print ""
	sys.exit()
elif not os.path.isfile('tables.xlsx'):
	print ""
	print ""
	print "tables.xlsx Not found"
	file.write("tables.xlsx Not found" + '\n' + '\n')
	print ""
	print ""
	print "Please keep tables.xlsx with tool"
	file.write("Please keep tables.xlsx with tool" + '\n' + '\n' + "and try again ....")
	print ""
	print ""
	sys.exit()


Xvals=[]; Yvals=[]
i = open('input.txt','r')

for line in i:
	    
	 x, y = line.split('=', 1)
	 Xvals.append(str(x)) 
	 Yvals.append(str(y))

#read html link

htmllink = Yvals[0]
htmllink = htmllink.rstrip()
htmllink = htmllink.lstrip()
htmllink = htmllink.lstrip('\n')


try:
	df = pd.read_html(htmllink)

except:
	file.write("Tool could not open the link. Something went wrong !!!. Please check the link passed in the input.txt. Please make sure webpage has html Tables to extract !!!" + '\n' + '\n')
	sys.exit()

file_2 = codecs.open('done.txt','w',encoding="utf-8")

def pd_html_excel():

	book = load_workbook('tables.xlsx')
	writer = ExcelWriter('tables.xlsx', engine='openpyxl') 	
	writer.book = book
	writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

	for x in range(0,len(df)):

		df[x].to_excel(writer,sheet_name="table_" + str(x))
	
	writer.save()

	file_2.write("Success !!! Please check tables.xlsx for extracted tables from the webpage." + '\n' + '\n')


pd_html_excel()

file.close()
remove_log('log.txt')

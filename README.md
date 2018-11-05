# python_based_webtable_scraping

Task : Automating task of downloading html web tables from webpages.

Purpose : 
This Python pandas based script is for extracting html table information from webpage into an xlsx file with ease. 
Please use this tool for ethical web scraping only. 
Any possible tool error will be logged in the log.txt file.

USAGE:
1) Please keep webtable_extractor.py and tables.xlsx in any permissible path of your Linux directory.
2) Upadte input.txt with URL having html tables and save the file. 
3) URL updated in the input.txt should be valid.
4) Run as python webtable_extractor.py command OR ./webtable_extractor.py
5) Webtables will be extracted in the tables.xlsx file. Ignore the 1st sheet.

Python Dependencies OR Requirement [Linux users can use pip and windows users can sue pip.exe ]:

pandas
openpyxl
lxml
html5lib
codecs
sys
os



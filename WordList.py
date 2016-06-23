#!/usr/bin/env  python
# coding: utf-8

import os
import sys 
import json
import urllib2
import argparse
from pprint  import pprint
from colorama import init
from colorama import Fore, Back, Style
from collections import deque

init()
filepath = "./word.md"
f        = open(filepath,"a+")
baseurl  = 'https://api.shanbay.com/bdc/search/?word='


def GetDefinitonFromShanBay(word):
	url  = baseurl+word
	u    = urllib2.urlopen(url)
	#resp = json.loads(u.read().decode('utf-8'),object_hook=JSONObject)
	resp = json.loads(u.read().decode('utf-8'))
	if resp.get('data',0) == {}:  # resp is empty
		print 
		print(Fore.RED + "Cannot get the definition\nPlease check out your word:"+Fore.GREEN+"%s") %(word)
		print(Style.RESET_ALL)
		sys.exit(0)
	return resp

def WriteWordIntoFile(word):
	resp       = GetDefinitonFromShanBay(word)
	s          = resp["data"]["definition"].encode('utf-8').strip('\n')
	definition = " ".join(s.split())
	print >> f, "%-20s\t%s" %(word, definition)
	print(Style.BRIGHT)
	print(Fore.GREEN + "Add Word Sussess!")
	print(Style.RESET_ALL)

def	CheckOutWord(word):
	for line in f:
		if line.find(word) != -1:
			print(Style.BRIGHT)
			print(Fore.YELLOW+"The word you have inserted before, see:\n"+Fore.GREEN+" %s") %(line.strip())
			print(Style.RESET_ALL)
			return 1 #means the word exsit
	return 0   #means the word not exsit

def CheckFileIsEmpty():
	if os.stat(filepath).st_size == 0:
		return 1
	else:
		return 0

def InsertWord(word):
	# get word
	#word = sys.argv[1].encode('utf-8').strip()
	# check file
	ret = CheckFileIsEmpty()
	#if the file is not empty, so we need to 
	# check whether the word exsited.if exsited
	# just print the word and the definition
	if ret == 0: 
		IsExsit = CheckOutWord(word)
		if IsExsit == 1:
			sys.exit(0)
	WriteWordIntoFile(word)

def	ParseCommandLinePara():
	parser = argparse.ArgumentParser()

	parser.add_argument('-s',action='store',dest='s_word',
			help='search a word and get the definition')

	parser.add_argument('-a',action='store',dest='a_word',
			help='append a word into the word list')

	parser.add_argument('-p',action='store',default=False,
			dest='print_lately',type=int,nargs='?',
			help='print n lately words')

	parser.add_argument('-e',action='store_true',default=False,
			dest='export_excel',
			help='export word list into excel file')
	
	parser.add_argument('-i',action='store_true',default=False,
			dest="InsertWord",
			help="Insert word into list when use -s")

	results = parser.parse_args()
	return results

#def GetExampleFromShanBay(w_id):
#	ExampleUrl = 'https://api.shanbay.com/bdc/example/?vocabulary_id='+str(w_id)+'&type=sys'
#	u    = urllib2.urlopen(ExampleUrl)
#	resp = json.loads(u.read().decode('utf-8'))
#	if resp.get('data',0) == {}:  # resp is empty
#		return (None,None,0)
#	example   = resp["data"][0]["annotation"]
#	translate = resp["data"][0]["translation"]
#	return (example,translate,1)

def ShowWordDef(word):
	resp          = GetDefinitonFromShanBay(word)
	hasEn         = 0
	s             = resp["data"]["definition"].encode('utf-8').strip('\n')
	definition_cn = " ".join(s.split())
	if resp["data"]["en_definition"] != {}:
		s     = resp["data"]["en_definition"]["defn"].encode('utf-8').strip('\n')
		hasEn = 1 
		definition_en = " ".join(s.split())
	#word_id       = resp["data"]["id"]
	#example,translate,Ishave= GetExampleFromShanBay(word_id)
	print(Style.BRIGHT)
	print(Fore.RED + word + '\n')
	if hasEn == 1:
		print(Fore.GREEN + "[En Def]:\n" +"  " + definition_en)
		
	print(Fore.GREEN + "[Cn Def]:\n" +"  " + definition_cn)
	#if Ishave == 1:
	#	print(Fore.YELLOW + "Example:\n" + "\t- " + Fore.Green + example)
	#	print("\t- " + translate)
	print(Style.RESET_ALL)


def ShowLately(n=10):
	while True:
		print(Style.BRIGHT)
		for lines in list(deque(f,n)):
			line_list = lines.split('\t')
			print(Fore.MAGENTA +  "%-20s" + '\t' + 
					Fore.CYAN + line_list[1].strip('\n')) %(line_list[0])
		break
	print(Style.RESET_ALL)
	

def ExportList():
	pass


def main():
	#CheckCommandLine()
	res = ParseCommandLinePara()
	if res.a_word:
		InsertWord(res.a_word)
	elif res.s_word:
		ShowWordDef(res.s_word)
		if res.InsertWord:
			InsertWord(res.s_word)
	elif res.print_lately:
		ShowLately(res.print_lately)
	elif res.print_lately == None:
		ShowLately()
	elif res.export_excel:
		ExportList()

if __name__ == '__main__':
	sys.exit(main())



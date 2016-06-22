#!/usr/bin/env  python
# coding: utf-8

import os
import sys 
import json
import urllib2
from pprint import pprint

filepath = "./word.md"
f        = open(filepath,"a+")
baseurl  = 'https://api.shanbay.com/bdc/search/?word='

class JSONObject:
	def __init__(self,d):
		self.__dict__ = d

def CheckCommandLine():
	if len(sys.argv) == 1:
		ShowHelp()
		sys.exit(0)

def ShowHelp():
	print "Usage: python %s word" %(sys.argv[0])

def GetDefinitonFromShanBay(word):
	url  = baseurl+word
	u    = urllib2.urlopen(url)
	#resp = json.loads(u.read().decode('utf-8'),object_hook=JSONObject)
	resp = json.loads(u.read().decode('utf-8'))
	if resp.get('data',0) == {}:  # resp is empty
		print "Cannot get the definition,Please check out your word"
		sys.exit(0)
	s    = resp.data.definition.encode('utf-8').strip('\n')
	definition = " ".join(s.split())
	return definition

def WriteWordIntoFile(word):
	definition = GetDefinitonFromShanBay(word)
	print >> f, "%-20s\t%s" %(word, definition)

def	CheckOutWord(word):
	for line in f:
		if line.find(word) != -1:
			print "The word you have inserted before, see:\n %s" %(line.strip())
			return 1 #means the word exsit
	return 0   #means the word not exsit

def CheckFileIsEmpty():
	if os.stat(filepath).st_size == 0:
		return 1
	else:
		return 0

def InsertWord():
	CheckCommandLine()
	# get word
	word = sys.argv[1].encode('utf-8').strip()
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


InsertWord()



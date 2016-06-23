#!/usr/bin/env  bash

if [ -e word.md ];then
	cp word.md word.md.bak
	rm word.md
fi

if [ -d coverage_html ];then
	rm -rf coverage_html
fi

coverage run -a WordList.py -s "hello"  >/dev/null
coverage run -a WordList.py -s "hellooo">/dev/null
coverage run -a WordList.py -a "hello" >/dev/null
coverage run -a WordList.py -a "hello" >/dev/null
coverage run -a WordList.py -s "world" -i  >/dev/null
coverage run -a WordList.py -p 1       >/dev/null
coverage run -a WordList.py -p         >/dev/null
coverage report                        
coverage html -d coverage_html

if [ -e word.md.bak ]; then
	mv word.md.bak word.md
fi


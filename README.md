## Introduction

`WordList` is a command line tool, You can use it to search a word definition, and save it
into a local file. And then when you want review it, you can show all the word you have searched
and Inserted. Last, you can export the file into excel, so you can do more extra about the that.


## Install
Before you use this tool, you need to install two package:

```
	pip install colorama
	pip install shanbay
```

When you install them correctly, you can try some examples below

## Example

Here I will show you some example. Every time you can use `WordList -h` to get help, like: 

```
usage: WordList.py [-h] [-s S_WORD] [-a A_WORD] [-p [PRINT_LATELY]] [-e] [-i]

optional arguments:
  -h, --help         show this help message and exit
  -s S_WORD          search a word and get the definition
  -a A_WORD          append a word into the word list
  -p [PRINT_LATELY]  print n lately words
  -e                 export word list into excel file
  -i                 Insert word into list when use -s
```

Now, you can use:

+ WordList -s word       search and show the definition of the `word`
+ WordList -s word -i    search and show the definition of the `word` and insert it into file
+ WordList -a word       append the word into file
+ WordList -p            show recently 10 items(default)
+ WordList -p  n         show recently n  items
+ WordList -e            export wordlist into excel


Notice:  the export cannot work now, comming soon~

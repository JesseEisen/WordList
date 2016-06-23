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

+ WordList -s word       
  search and show the definition of the `word`
+ WordList -s word -i    
  search and show the definition of the `word` and insert it into file
+ WordList -a word       
  append the word into file
+ WordList -p            
  show recently 10 items(default)
+ WordList -p  n         
  show recently n  items
+ WordList -e            
  export wordlist into excel


Notice:  the export cannot work now, comming soon~

## License 

The MIT License (MIT)

Copyright (c) 2016 LinKang Chen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

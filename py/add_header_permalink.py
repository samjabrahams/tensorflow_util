# Copyright (c) 2015 Sam Abrahams (sam [at] samabrahams.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy of 
# this software and associated documentation files (the "Software"), to deal in the 
# Software without restriction, including without limitation the rights to use, 
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or 
# substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

### add_header_permalink.py takes all markdown files in a directory (or set of directories, 
### using the glob library's pattern matching capabilities) and adds self-referential links 
### to header lines that include an #id in braces
### 
### Basically, it takes a line that looks like this:
### 	'### Some Kind of Awesome Header {#awesome-header}'
###
### and replaces it with this:
### 	'### [Some Kind of Awesome Header](#awesome-header) {#awesome-header}'

# Module for finding pathnames
# https://docs.python.org/2/library/glob.html
import glob

# Module for regular expressions
# https://docs.python.org/2/library/re.html
import re

# Module for operating system functionality
# https://docs.python.org/2/library/os.html
import os

# Directory or Directories to look for markdown files
INPUT_DIRECTORY = '../../tensorflow/tensorflow/g3doc/api_docs/*/'
# Directory to output to
OUTPUT_DIRECTORY = '../out/add_header_permalink_test'

# Switch this to True if you want to simply overwrite the existing files
OVERWRITE = False

# Given a string path to a file, returns the file name plus extension
def get_file_name_from_path(path):
	return path[path.rfind('/') + 1:]

# Given a directory path, returns the path string, making sure it ends with a forward slash '/'
def end_path_in_slash(path):
	if path[-1] != '/':
		return path + '/'
	else:
		return path

def strip_relative_directories(path):
	index = path.rfind('./')
	return path[index+2:]

# RegEx pattern for matching markdown headers (starts with one or more '#' symbols followed by a space, then any number of characters)
ph = re.compile('^#+ .*')

# RegEx pattern for matching it contains the markdown id syntax '{#SOMESETOFCHARACTERS}'
pb = re.compile(r".*\{#.+\}.*")


# Ensure that input/output direcories are properly formatted
INPUT_DIRECTORY = end_path_in_slash(INPUT_DIRECTORY)
OUTPUT_DIRECTORY = end_path_in_slash(OUTPUT_DIRECTORY)

##
##	GO THROUGH EACH MD FILE IN THE INPUT DIRECTORY
##

for filePath in glob.glob(INPUT_DIRECTORY + '*.md'):
	# Define a string to hold modified text
	text = "" 

	# Open a file object using the file name, with read/write capabilities
	f = open(filePath, 'r')

	for line in f:
		if ph.match(line) and pb.match(line):
			# Is a header with an id!
			# Replace the line with a modified line
			
			# Index of the start of the header, after the '#' characters
			startIndex = line.find('# ') + 2
			# Index of the open brace character indicating an id
			openBraceIndex = line.rfind('{')
			closeBraceIndex  = line.rfind('}')

			# Check to see if startIndex exists, if not, print to console, print the regular line, and continue
			if startIndex == -1 or openBraceIndex == -1 or closeBraceIndex == -1:
				print "Something weird going on in " + filePath + ":\r\n\t" + line 
				text += line
				continue

			# Add markdown link syntax pointing to its own #id
			text += line[0: startIndex] + "[" 
			text += line[startIndex:openBraceIndex-1] + "](" + line[openBraceIndex+1:closeBraceIndex] + ")"
			text += line[openBraceIndex-1:]

		else:
			# Is not a header with an id
			# Keep the line the same
			text += line


	f.close()

	# DANGER, WILL ROBINSON! This will delete all the current data if not careful
	if OVERWRITE:
		f = open(filePath, 'w')	
	else:
		# DANGER, WILL ROBINSON! This will delete all the current data if not careful
		finalDestination = OUTPUT_DIRECTORY + strip_relative_directories(filePath)
		if not os.path.exists(os.path.dirname(finalDestination)):
			os.makedirs(os.path.dirname(finalDestination))
		f = open(finalDestination, 'w')

	# Write the modified text to the file
	f.write(text)

	f.close()
	
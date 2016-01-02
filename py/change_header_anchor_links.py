#!/usr/bin/python

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
### using the glob library's pattern matching capabilities) and modifies self-referential
### links via #anchor-tags to conform to the Github/Tensorflow.org website auto-generation
### pattern. It also removes unneccesary {#anchor} notation.
### 

# Module for finding pathnames
# https://docs.python.org/2/library/glob.html
import glob

# Module for regular expressions
# https://docs.python.org/2/library/re.html
import re

# Module for operating system functionality
# https://docs.python.org/2/library/os.html
import os

import sys, getopt

# Directory or Directories to look for markdown files
INPUT_DIRECTORY = '../../tensorflow/tensorflow/*/*'
# Directory to output to
OUTPUT_DIRECTORY = '../out/change_header_anchor_links_test'

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

# Creates a new anchor link, constructed from the original text
# A header with the form "   This is my Cool Header!!" creates
# the anchor "#this-is-my-cool-header"
# arg: header - Header string to be converted to an anchor
# arg: existingHeaders - a list of anchors that is used to check
#		the newly constructed anchor. If an existing anchor matches, a
#		number (starting from 1) is concatenated to the end and it checks
#		for uniqueness again. This repeats with incrementing numbers until a
#		unique anchor tag is found
def create_anchor_from_header(header, existingAnchors=None):
	# Strip white space on the left/right and make lower case
	out = header.strip().lower()

	# Remove characters that aren't alphanumeric, hyphens, or spaces
	out = re.sub(r"[^\w\- ]+", lambda x: "", out)

	# Replace groups of white space with hyphens
	out = re.sub(r"\s+", lambda x: "-", out)

	# Remove any amount of hyphens at the end of the header
	out = re.sub(r"\-+$", "", out)

	if existingAnchors:
		if out in existingAnchors:
			i = 1
			while (out + "-" + str(i)) in existingAnchors and i < 100:
				i +=  1
			return out + "-" + str(i)
	
	return out

# RegEx pattern for matching markdown headers (starts with one or more '#' symbols followed by a space, then any number of characters)
ph = re.compile('^#+ ')

# RegEx pattern for matching it contains the markdown id syntax '{#SOMESETOFCHARACTERS}'
pb = re.compile(r"\{#.+\}")

# RegEx pattern for matching lines that contain an anchor link
pl = re.compile(r"\]\(#[^\)]+\)")


# Ensure that input/output direcories are properly formatted
INPUT_DIRECTORY = end_path_in_slash(INPUT_DIRECTORY)
OUTPUT_DIRECTORY = end_path_in_slash(OUTPUT_DIRECTORY)

##
##	GO THROUGH EACH MD FILE IN THE INPUT DIRECTORY
##

# Create list of all markdown files in the given directory
filePaths = glob.glob(INPUT_DIRECTORY + '*.md')

for filePath in filePaths:
	# Dictionary that maps old headers to the new syntax
	headers = {}

	# Open file with read capabilities
	f = open(filePath, 'r')

	# First pass through the file: collect all headers that currently use 
	# {#anchor} notation
	for line in f:
		if ph.search(line) and pb.search(line):
			# Line defines a header

			# Index of the start of the header, after the '#' characters
			startIndex = line.find('# ') + 2

			# Index of the open and close brace characters
			# These indicatate an outdated {#anchor}
			openBraceIndex = line.rfind('{')
			closeBraceIndex = line.rfind('}')

			# Check to see if indices exists, if not, print to console, print the regular line, and continue
			if startIndex == -1 or openBraceIndex == -1:
				print "Something weird going on in " + filePath + ":\r\n\t" + line 
				text += line
				continue

			# The original header text
			headerText = line[startIndex : openBraceIndex]

			# The original anchor link
			originalAnchor = line[openBraceIndex + 1 : closeBraceIndex]

			if originalAnchor not in headers:
				# Create the new anchor link
				newAnchor = create_anchor_from_header(headerText, headers.values())
				# Place new anchor in dictionary with old anchor as key
				headers[originalAnchor] = newAnchor
	
	# Reset iterator
	f.seek(0)

	# Second pass through the file: create string to hold new text data
	# Changing lines as needed

	# Modified text holder used to rewrite file
	text = ""

	for line in f:
		
		hasAnchorHeader = ph.search(line) and pb.search(line)
		hasAnchorLink = pl.search(line)
		
		if hasAnchorHeader or hasAnchorLink:	
			replacementLine = ""

			if hasAnchorHeader:

				# Line has a header with {#anchor} notation
				
				# Index of the start of the braces notation
				openBraceIndex = line.rfind('{')

				# Use everything except for the {#anchor}
				replacementLine += line[:openBraceIndex] + "\r\n"

			if hasAnchorLink:
				# Line has at least one anchor link in it

				# Get list of all link start and end indices
				links = [m.span() for m in pl.finditer(line)]

				# Most recent index used
				lastIndex = 0

				for link in links:
					# Check each header link and change if necessary

					# Extract #anchor text
					anchor = line[link[0] + 2 : link[1] - 1]

					if anchor in headers:
						# The anchor has been identified in {#anchor} notation before
						# Replace the link with the corresponding Github style anchor
						replacementLine += line[lastIndex : link[0] + 2] + "#" + headers[anchor] + ")"
					else:
						# Normal anchor: don't change it
						replacementLine += line[lastIndex : link[1]]

					lastIndex = link[1]

				replacementLine += line[lastIndex:]

			# Add on modifed line to the text holder
			text += replacementLine
		else:
			# Line does not need to be modified
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
	
import glob, re, os

inputDir = '../../tensorflow/tensorflow/*/*/*/*/*/*'
outputDir = '../out/anchor_list/'

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
ph = re.compile('^#+ ')

# RegEx pattern for matching it contains the markdown id syntax '{#SOMESETOFCHARACTERS}'
pb = re.compile(r"\{#.+\}")

# RegEx pattern for matching lines that contain an anchor link
pl = re.compile(r"\]\(#[^\)]+\)")

pol = re.compile(r"\]\([^\)]+#[^\)]+\)")

api = re.compile(r"api_docs/")

# Ensure that input/output direcories are properly formatted
inputDir = end_path_in_slash(inputDir)
outputDir = end_path_in_slash(outputDir)

filePaths = glob.glob(inputDir + '*.md')

counter = 0

for filePath in filePaths:
	if not api.search(filePath):
		f = open(filePath, 'r')

		for line in f:
			if pol.search(line) and not api.search(line):
				print filePath + ":\n\t" + line
				counter += 1
		f.close()

print counter
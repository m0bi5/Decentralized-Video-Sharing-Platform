
from subprocess import Popen,PIPE
import re

#Function serves as a CLI to access the ipfs.exe
def terminal(command):
	result = Popen(args=command,stdout = PIPE)
	result.wait()
	return result.stdout.read().decode("utf-8") 
	

#Function used to retrieve a file hash from a given string
def getHash(string):
	fileHash=''
	#Search for hash in the string
	for substring in string.split():
		#All IPFS hashes begin with Qm
		if substring[:2]=='Qm': 
			fileHash=substring
	return fileHash

#Function used to upload a file to an IPFS node
def fileUpload(path):
	command=['ipfs','add',path]
	output=terminal(command)
	return getHash(output)



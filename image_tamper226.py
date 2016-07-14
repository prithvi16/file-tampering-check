roll no:226

from PIL import Image
import hashlib 
import sys


print ("Enter the path of first file:")
firstImg=raw_input()

print("Enter the path of second file:")
secondImg=raw_input()

file1=open(firstImg).read()
file2=open(secondImg).read()

hash1=hashlib.md5(file1).hexdigest()
print(hash1)

hash2=hashlib.md5(file2).hexdigest()
print(hash2)

if hash1==hash2:
	print (" NOT TAMPERED!!!")
	
else:
	print(" IS TAMPERERD")








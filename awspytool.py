import boto3
import system

def handleUserInput(str):
	if str == 'r':
		rfile = str(input('Enter path of file: '))
		readFile(rfile)
	elif str == 'c':
		cfile = str(input('Enter new file name: '))
		createFile(cfile)
	elif str == 'u':
		file_to_upload = str(input('Enter path of file to upload: '))
		bucket_name = str(input('Enter S3 bucket name: '))
		upload_to_AWS(file_to_upload, bucket_name)
	elif str == 'd':
		file_to_download = str(input('Enter file path on AWS to download: '))
		bucket_name = str(input('Enter S3 bucket name'))
	elif str == 'x'
		file_to_delete = str(input('Enter file path on AWS to delete: '))
		bucket_name = str(input('Enter S3 bucket name'))
	elif str == 'EXIT'
		print('Bye')
		sys.exit()

def readFile(str):
	file = open(str, 'r')
	lines = file.readlines()
	print('\nContents of current file: {}'.format(str))
	c = 0
	for line in lines:
		print("{}".format(line.strip()))

	file.close()

def createFile(str):
	file = open('name.txt', 'w')
	file.write('{}'.format(str))
	print('\nFile name.txt created in current dir')

def upload_to_AWS():
	s3 = boto3.client('s3')

	s3.upload_file('name.txt', 'assignment1cs403', 'names_on_s3.txt')
	print('\nFile names_on_s3.txt uploaded to AWS')

def download_from_AWS():
	s3 = boto3.client('s3')

	s3.download_file('assignment1cs403', 'names_on_s3.txt', 'names_downloaded.txt')
	print('\nFile names_downloaded.txt saved in current dir')

def delete_from_AWS():
	s3 = boto3.client('s3')
	
	s3.delete_object(Bucket='assignment1cs403', Key='names_on_s3.txt')
	print('\nDeleted file from aws')

def main():
	print('Type...\n"r" to read file\n"c" to create file\n"u" to upload a file to aws\n"d" to download a file from aws\n"x" to delete a file from aws\n"EXIT" to exit')
	chosenfunc = str(input('Enter your selection: '))
	name = str(input('\nEnter your name:  '))
	createFile(name)
	upload_to_AWS()
	download_from_AWS()
	#readFile('file/location/on/computer')
	delete_from_AWS()
	input('Press ENTER to exit')

main()
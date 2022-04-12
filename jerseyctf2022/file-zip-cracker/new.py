import zipfile

# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
	try:
		zip_file.extractall(pwd=password.encode())
		return True
	except KeyboardInterrupt:
		exit(0)
	except Exception as e:
		pass
       
# Zipped File
zipfilename0 = 'secret_folder.zip'
zipfilename = 'secret_folder.zip'
zip_file = zipfile.ZipFile(zipfilename)

# Years
yearMax = 2023

# Actors
actors = []
with open("actorList.txt") as actorList:
	lines = actorList.readlines()   
	for l in lines:
		x = l.replace("\n", "")
		actors.append(x)
print(len(actors))
# Try
for p in range(2000, yearMax):
	for actor in actors:
		password = actor + str(p)
		print(password)
		# If the file was extracted, you found the right password.
		if extractFile(zip_file, password):
			print('*' * 20)
			print('Password found: %s' % password)
			print('Files extracted...')
			exit(0)
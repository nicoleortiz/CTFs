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
zipfilename = 'compressed_file.zip'
zip_file = zipfile.ZipFile(zipfilename)

list = ['Johnny_Depp2017', 'JohnnyDepp2006', 'Heart_of_Davy_Jones',
	'i\'ve_got_a_jar_of_dirt_and_guess_what\'s_inside_it']
	
for password in list:
	# If the file was extracted, you found the right password.
	if extractFile(zip_file, password):
		print('*' * 20)
		print('Password found: %s' % password)
		print('Files extracted...')
		exit(0)
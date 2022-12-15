

# Read all file names which have csv/xlsx extension in the current folder
# Remove extra characters at the end of the second '-'

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
existing_files = []
for f in files:
	# print(f.index('.'))
	dot_index = f.index('.')
	if(f[dot_index+1:] in ['xlsx','csv']):
		if('-' in f[2:]):
			dash_index = f.index('-',2)
			if(dash_index<5):
				if(f[:dash_index]+'.'+f[dot_index+1:] not in existing_files):
					os.rename(f,f[:dash_index]+'.'+f[dot_index+1:])
					existing_files.append(f[:dash_index]+'.'+f[dot_index+1:])
				else:
					os.rename(f,f[:dash_index]+'new.'+f[dot_index+1:])
					existing_files.append(f[:dash_index]+'new.'+f[dot_index+1:])



files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	print(f)
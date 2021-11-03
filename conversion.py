import os
import shutil
import glob

#Get and store the original root dir
rootdir = os.getcwd()

#Get the Directory containing all the .odr files
odrdir = "D:\\downloads\\GTA5Models\\raw\\mpheist4\\int_mp_h_props\\"

blenderdir ="D:\\Programme\\"

if(not os.path.exists("temp")):
	os.mkdir("temp")

tmppath = os.path.abspath("temp") + "\\"

print(tmppath)
print(odrdir)
print(rootdir)

for files in os.listdir(tmppath):
    path = os.path.join(tmppath, files)
    try:
        shutil.rmtree(path)
    except OSError:
        os.remove(path)

os.chdir(odrdir)
#Copy all Folders from the odr dir, these folders contain the textures used later by the qc compiler

names = []
for file in os.listdir():
	if(os.path.isdir(file)):
		shutil.copytree(file, tmppath + file)
	if(not os.path.isdir(file)):
		shutil.copyfile(file, tmppath + file)
		names.append(file[:-4])

#Copy Needed Script Files from Root dir to Temp dir
os.chdir(rootdir)
shutil.copytree("glob2", tmppath + "glob2")
shutil.copyfile("openformat-to-obj.py", tmppath + "openformat-to-obj.py")
shutil.copyfile("ShaderManager.xml", tmppath + "ShaderManager.xml")

#Now that everything is set up in the temp folder, navigate into it and start the conversion
os.chdir(tmppath)
os.system("py openformat-to-obj.py *.odr -f")
()
#Start blender to for the OBJ to SMD Conversion
os.chdir(blenderdir)
os.system("blender --background --python " + rootdir + "\\blenderscript.py" )

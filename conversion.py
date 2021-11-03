import os
import shutil
import glob
import subprocess

#Get and store the original root dir
rootdir = os.getcwd()

cfg = open("run.cfg", "r")
lines = cfg.readlines()
for line in lines:
	if line.startswith("ODR"):
		odrdir = line.split("=")[1].strip(" ").strip("\n")
	if line.startswith("Blender"):
		blenderdir = line.split("=")[1].strip(" ").strip("\n")
	if line.startswith("Source Engine"):
		sourcedir = line.split("=")[1].strip(" ").strip("\n")
	if line.startswith("Source Game"):
		gamedir = line.split("=")[1].strip(" ").strip("\n")
		

#Get the Directory containing all the .odr files
#odrdir = "D:\\downloads\\GTA5Models\\raw\\mpheist4\\int_mp_h_props\\"
#blenderdir ="D:\\Programme\\"

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
#Start blender to for the OBJ to SMD Conversion pass on the root dir so the blender script can find the config
os.chdir(blenderdir)
os.system("blender --background --python " + rootdir + "\\blenderscript.py -- " + rootdir)

#Compiling the SMD Model to a MDL model so it can be used in the Source Engine
os.chdir(tmppath)
#Generate a Generic QC File in the temp Folder
for smd in glob.glob("*.smd"):
    qc = open(smd[:-4] + ".qc", "w+")
    qc.write("$modelname	\"props\\test\\" + smd[:-4] +".mdl\"" + "\n")
    qc.write("$scale		200" + "\n")
    qc.write("$body mybody	\"" + os.path.abspath(smd)[:-4] + ".smd\"" + "\n")
    qc.write("$staticprop" + "\n")
    qc.write("$surfaceprop	default" + "\n")
    qc.write("$cdmaterials	\"models\props\"" + "\n")
    qc.write("$sequence idle	\"" + os.path.abspath(smd)[:-4] + ".smd\"" + "\n")
    qc.write("$collisionmodel	\"" + os.path.abspath(smd)[:-4] + ".smd\" { $concave }" )
    qc.close()

    #Send each QC file to studiomdl to be compiled, works 
    qcpath = os.path.abspath(smd)[:-4] + ".qc" + '"'
    os.chdir(sourcedir)
    os.system("studiomdl.exe -game " + '"' + gamedir + '" "' + qcpath )
    os.chdir(tmppath)

   

import bpy
import glob
import os
import sys

#Pass On the Root Dir so we know where to look for the config
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
rootdir = argv[0]
 
cfg = open(rootdir + "\\run.cfg", "r")
lines = cfg.readlines()
for line in lines:
	if line.startswith("Source Engine"):
		engine_path = line.split("=")[1].strip(" ").strip("\n")
	if line.startswith("SMD Export"):
		smd_export_path = line.split("=")[1].strip(" ").strip("\n")

#Clear the Scene
collection = bpy.data.collections.get('Collection')
 
for obj in collection.objects:
    bpy.data.objects.remove(obj, do_unlink=True)
    
bpy.data.collections.remove(collection)

#SetUp SMD Export
bpy.context.scene.vs.export_path = smd_export_path
bpy.context.scene.vs.export_format = 'SMD'
bpy.context.scene.vs.engine_path = engine_path

for model in glob.glob(rootdir + "\\temp\\*.obj"):
    bpy.ops.import_scene.obj(filepath= os.path.abspath(model), filter_glob='*.obj;*.mtl', use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=False, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', axis_forward='-Z', axis_up='Y')#
    bpy.ops.export_scene.smd()
    for obj in bpy.data.objects : 
        obj.select_set(True)
    bpy.ops.object.delete()
    
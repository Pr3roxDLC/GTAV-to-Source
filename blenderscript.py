import bpy
import glob
import os

#Clear the Scene

collection = bpy.data.collections.get('Collection')
 
for obj in collection.objects:
    bpy.data.objects.remove(obj, do_unlink=True)
    
bpy.data.collections.remove(collection)

#SetUp SMD Export
bpy.context.scene.vs.export_path = "D:\\downloads\\GTA5Models\\output\\dlcheist4\\int_mp_h_props\\"
bpy.context.scene.vs.export_format = 'SMD'
bpy.context.scene.vs.engine_path = "D:\\downloads\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\bin\\"

for model in glob.glob("D:\\downloads\\GTA5Models\\temp\\*.obj"):
    bpy.ops.import_scene.obj(filepath= os.path.abspath(model), filter_glob='*.obj;*.mtl', use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=False, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', axis_forward='-Z', axis_up='Y')#
    bpy.ops.export_scene.smd()
    for obj in bpy.data.objects : 
        obj.select_set(True)
    bpy.ops.object.delete()
    
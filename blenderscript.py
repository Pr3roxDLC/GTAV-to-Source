#!/usr/bin/python
# -*- coding: utf-8 -*-

import bpy
import glob
import os
import sys
import shutil

# Pass On the Root Dir so we know where to look for the config
argv = sys.argv
argv = argv[argv.index('--') + 1:]  # get all args after "--"
rootdir = argv[0]

cfg = open(rootdir + '\\run.cfg', 'r')
lines = cfg.readlines()
for line in lines:
    if line.startswith('Source Engine'):
        engine_path = line.split('=')[1].strip(' ').strip('\n')

# Clear the Scene
collection = bpy.data.collections.get('Collection')
for obj in collection.objects:
    bpy.data.objects.remove(obj, do_unlink=True)
bpy.data.collections.remove(collection)

# SetUp SMD Export
bpy.context.scene.vs.export_path = rootdir + '\\temp\\'
bpy.context.scene.vs.export_format = 'SMD'
bpy.context.scene.vs.engine_path = engine_path


#Import Each OBJ file and export a SMD file for each created Sub Model
for model in glob.glob(rootdir + '\\temp\\*.obj'):
    bpy.ops.import_scene.obj(  #
        filepath=os.path.abspath(model),
        filter_glob='*.obj;*.mtl',
        use_edges=True,
        use_smooth_groups=True,
        use_split_objects=True,
        use_split_groups=False,
        use_groups_as_vgroups=False,
        use_image_search=True,
        split_mode='ON',
        axis_forward='-Z',
        axis_up='Y',
        )
    bpy.ops.export_scene.smd()

    #Export DDS Textures as <ModelName>.dds so they can be used for compiling the MDL models later
    for obj in bpy.data.objects:
        try:
            shutil.copyfile(bpy.data.materials[obj.active_material.name].node_tree.nodes['Image Texture'
                            ].image.filepath, rootdir + '\\temp\\'
                            + obj.name + '.dds')
        except (FileNotFoundError) as error:
            print('No Texture File Found for: ' + obj.name + ' skipping.')

    #Clear the Scene so blender doesnt crash
    for obj in bpy.data.objects:
        obj.select_set(True)
    bpy.ops.object.delete()

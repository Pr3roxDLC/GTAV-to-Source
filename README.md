# GTAV-to-Source
Very Hacky Python Script to mass convert .odr models to .mdl.
This builds on https://github.com/hedgehog90's Converter.


# Getting Started

Make sure you have all of the following installed:

1. Python 3 - this is a python script, so you will need python 3 to run it
2. Blender 2.8 - any version above this will also work, we use blender to convert the models
3. Blender Source Tools - we need this blender plugin to export models so we can compile them to source models
4. Any Source Game - we need any source game that comes with the studiomdl.exe tool, for example CS:GO
5. OpenIV - this tool is required to export the GTA V models

Once all of the above are installed and set up, configure the run.cfg for your environment

1. Root Path : This path points to the location of this script, it must be in the folowing format DRIVE:\Path\To\This\Repository\
2. ODR Dir Path : This will point to the location of your raw unconverted models
3. Blender Path : This specifies the location of your blender installation
4. Source Engine Path : This must point to the \bin\ folder of your source game
5. Source Game Path : this must point to the game folder of your source game, for example ...\Counter-Strike Global Offensive\csgo\
6. Scale : This is by how much the models will be scaled for the source engine
7. StudioMDL Timeout : Sometimes the modelcompilation will freeze/take very long, this will specify the maximum time in seconds any model can compile

After this is done, use Open IV to export the models from GTA, Left Click on any Drawable Object file (.ydr) and select Export to openFormats (.odr). Export the models to the ODR Dir Path defined above.

Optional: Export all the textures from the model rpf to ODR Dir Path\textures\ . Sometimes GTA doesnt embed the textures correctly with the models, resulting in them not being exported correctly when exporting them to .odr, therefor we can export the textures manually and put them in the \texture\ folder so incase we encounter a missing texture, we can automatically try to look for it in the \texture\ folder

Start the conversion by running the conversion.py script from cmd.
The scipt will populate a temp folder to work with and then output all the models to ...\Game Path\props\test\




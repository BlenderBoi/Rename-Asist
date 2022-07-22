import bpy
import os

script_file = os.path.realpath(__file__)
addon_directory = os.path.dirname(script_file)
addon_name = os.path.basename(addon_directory)

def get_addon_name():

    return addon_name

def get_addon_preferences():

    addon_preferences = bpy.context.preferences.addons[addon_name].preferences

    return addon_preferences



def draw_subpanel(self, boolean, property, label, layout):

    if boolean:
        ICON = "TRIA_DOWN"
    else:
        ICON = "TRIA_RIGHT"

    row = layout.row(align=True)
    row.alignment = "LEFT"
    row.prop(self, property, text=label, emboss=False, icon=ICON)

    return boolean


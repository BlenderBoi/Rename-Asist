import bpy
import os
import pathlib

from . import Preferences

from . import Panels
from . import Utility_Functions



def update_panel(self, context):

    addon_preferences = Utility_Functions.get_addon_preferences()
    message = ": Updating Panel locations has failed"

    panels = []


    pt = Panels.RA_PT_Rename_Asist_Panel
    catagory = addon_preferences.PANEL_Category
    label = addon_preferences.PANEL_Label
    item = [pt, catagory, label]
    panels.append(item)

    try:
        pass
        for item in panels:

            panel = item[0]
            category = item[1]
            label = item[2]

            if "bl_rna" in panel.__dict__:
                bpy.utils.unregister_class(panel)

            panel.bl_category = category
            panel.bl_label = label

            bpy.utils.register_class(panel)

    except Exception as e:
        print("\n[{}]\n{}\n\nError:\n{}".format(__name__, message, e))
        pass





class Rename_Asist_user_preferences(bpy.types.AddonPreferences):

    bl_idname = Utility_Functions.get_addon_name()



    PANEL_Enable: bpy.props.BoolProperty(default=True)
    PANEL_Category: bpy.props.StringProperty(default="Rename Asist", update=update_panel)
    PANEL_Label: bpy.props.StringProperty(default="Rename Asist", update=update_panel)


    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)
        row = col.row(align=True)

        col.prop(self, "PANEL_Enable", text="Enable Panel")
        col.prop(self, "PANEL_Category", text="Category")
        col.prop(self, "PANEL_Label", text="Label")






classes = [Rename_Asist_user_preferences]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)



    update_panel(None, bpy.context)

def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

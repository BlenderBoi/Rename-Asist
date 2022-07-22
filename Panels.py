import bpy
import os
from . import Utility_Functions




class RA_PT_Rename_Asist_Panel(bpy.types.Panel):
    """Rename Asist Panel"""
    bl_label = "Rename Asist Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rename Asist"


    @classmethod
    def poll(cls, context):
        preferences = Utility_Functions.get_addon_preferences()
        return preferences.PANEL_Enable


    def draw(self, context):

        layout = self.layout

        if context.mode == "OBJECT":
            layout.label(text="Selected Objects", icon="RESTRICT_SELECT_OFF")
            layout.prop(context.scene.rename_asist_data, "Filter_By_Object_Type", text="")

            for object in context.selected_objects:

                icon = "OBJECT_DATA"

                show = False


                if context.scene.rename_asist_data.Filter_By_Object_Type == "ALL":
                    show = True
                elif context.scene.rename_asist_data.Filter_By_Object_Type == object.type:
                    show = True

                if object.type == "MESH":
                    icon = "MESH_DATA"
                if object.type == "LIGHT":
                    icon = "LIGHT_DATA"
                if object.type == "CURVE":
                    icon = "CURVE_DATA"
                if object.type == "ARMATURE":
                    icon = "ARMATURE_DATA"
                if object.type == "CAMERA":
                    icon = "CAMERA_DATA"
                if object.type == "FONT":
                    icon = "FONT_DATA"
                if object.type == "META":
                    icon = "META_DATA"
                if object.type == "VOLUME":
                    icon = "VOLIME_DATA"
                if object.type == "SURFACE":
                    icon = "SURFACE_DATA"
                if object.type == "EMPTY":
                    icon = "EMPTY_DATA"
                if object.type == "LIGHT_PROBE":
                    icon = "OUTLINER_OB_LIGHTPROBE"
                if object.type == "SPEAKER":
                    icon = "OUTLINER_OB_SPEAKER"

                if show:

                    col = layout.column(align=True)
                    row = col.row(align=True)

                    #focusoperator

                    op = row.operator("ra.view_object", icon="VIEWZOOM", text="")
                    op.object = object.name
                    row.prop(object, "name", text="", icon=icon)
                    op = row.operator("ra.deselect_object", icon="RESTRICT_SELECT_ON", text="")
                    op.object = object.name

            layout.operator("ra.view_selected_objects", icon="ZOOM_SELECTED", text="View Selected")

ENUM_Object_Type = [

        ("ALL","All","", "BLANK1", 0),
        ("MESH","Mesh","", "MESH_DATA", 1),
        ("META","Meta","", "META_DATA", 2),
        ("LIGHT","Light","", "LIGHT_DATA", 3),
        ("CURVE","Curve","", "CURVE_DATA", 4),
        ("ARMATURE","Armature","", "ARMATURE_DATA", 5),
        ("CAMERA","Camera","", "CAMERA_DATA", 6),
        ("FONT","Text","", "FONT_DATA", 7),
        ("VOLUME","Volume","", "VOLIME_DATA", 8),
        ("SURFACE","Surface","", "SURFACE_DATA", 9),
        ("EMPTY","Empty","", "EMPTY_DATA", 10),
        ("LIGHT_PROBE","Light Probe","", "OUTLINER_OB_LIGHTPROBE", 11),
        ("SPEAKER","Speaker","", "OUTLINER_OB_SPEAKER", 12),

        ]


class Rename_Asist_Data(bpy.types.PropertyGroup):

    Filter_By_Object_Type: bpy.props.EnumProperty(items=ENUM_Object_Type)

classes = [RA_PT_Rename_Asist_Panel, Rename_Asist_Data]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.rename_asist_data = bpy.props.PointerProperty(type=Rename_Asist_Data)

def unregister():


    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.rename_asist_data


if __name__ == "__main__":
    register()

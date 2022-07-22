import bpy


def deselect_all(context):

    for object in context.selected_objects:
        object.select_set(False)

def select_objects(objects):
    for object in objects:
        object.select_set(True)

def set_active(context, object):
    object.select_set(True)
    context.view_layer.objects.active = object


def View_Object(context, object):
    SaveSelected = [obj for obj in context.selected_objects]
    SaveActive = context.active_object
    deselect_all(context)
    set_active(context, object)
    bpy.ops.view3d.view_selected(use_all_regions=False)
    deselect_all(context)
    select_objects(SaveSelected)
    set_active(context, SaveActive)


def View_Selected_Object(context, objects):
    SaveSelected = [obj for obj in context.selected_objects]
    SaveActive = context.active_object
    deselect_all(context)
    select_objects(objects)
    bpy.ops.view3d.view_selected(use_all_regions=False)
    deselect_all(context)
    select_objects(SaveSelected)
    set_active(context, SaveActive)


class RA_OT_View_Object(bpy.types.Operator):

    bl_idname = "ra.view_object"
    bl_label = "View Object"
    bl_description = "View Object"
    bl_options = {"REGISTER", "UNDO"}

    object: bpy.props.StringProperty()

    def execute(self, context):

        
        if self.object:
            obj = bpy.data.objects.get(self.object)
            if obj:
                View_Object(context, obj)


        return {'FINISHED'}

class RA_OT_View_Selected_Objects(bpy.types.Operator):

    bl_idname = "ra.view_selected_objects"
    bl_label = "View Selected Objects"
    bl_description = "View Selected Objects"
    bl_options = {"REGISTER", "UNDO"}


    def execute(self, context):

        if context.scene.rename_asist_data.Filter_By_Object_Type == "ALL":
            objects = [object for object in context.selected_objects]

        else:
            objects = [object for object in context.selected_objects if object.type == context.scene.rename_asist_data.Filter_By_Object_Type]

        View_Selected_Object(context, objects)

        return {'FINISHED'}



class RA_OT_Deselect_Object(bpy.types.Operator):

    bl_idname = "ra.deselect_object"
    bl_label = "Deselect Object"
    bl_description = "Deselect Object"
    bl_options = {"REGISTER", "UNDO"}

    object: bpy.props.StringProperty()

    def execute(self, context):

        
        if self.object:
            obj = bpy.data.objects.get(self.object)
            if obj:
                obj.select_set(False)


        return {'FINISHED'}







classes = [
        RA_OT_Deselect_Object,
        RA_OT_View_Object,
        RA_OT_View_Selected_Objects,
        ]


def register():


    for cls in classes:
        bpy.utils.register_class(cls)



def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)



if __name__ == "__main__":
    register()

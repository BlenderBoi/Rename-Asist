bl_info = {
    "name": "Rename Asist",
    "author": "BlenderBoi",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "description": "",
    "wiki_url": "",
    "category": "Utility",
}

import bpy
from . import Preferences
from . import Panels
from . import Operator

modules = [Panels, Preferences, Operator]

def register():

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()

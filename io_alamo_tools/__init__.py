from bpy.types import (
    Panel,
    Operator,
    PropertyGroup,
)
from bpy.props import (
    StringProperty,
    BoolProperty,
    IntProperty,
    FloatProperty,
    EnumProperty,
    PointerProperty,
)
from bpy.props import *
import mathutils
import bpy
import importlib

bl_info = {
    "name": "ALAMO Tools",
    "author": "Gaukler, evilbobthebob, inertial, 1138",
    "version": (0, 0, 3, 5),
    "blender": (2, 93, 0),
    "category": "Import-Export",
}

ADDON_FOLDER = "io_alamo_tools"

modules = (
    ".validation",
    ".UI",
    ".UI_material",
    ".import_alo",
    ".import_ala",
    ".export_alo",
    ".export_ala",
    ".settings",
    ".utils",
)


def import_modules():
    for mod in modules:
        # print('importing with importlib.import_module =' + str(mod) + "=")
        importlib.import_module(mod, ADDON_FOLDER)


def reimport_modules():
    """
    Reimports the modules. Extremely useful while developing the addon
    """
    for mod in modules:
        # Reimporting modules during addon development
        want_reload_module = importlib.import_module(mod, ADDON_FOLDER)
        importlib.reload(want_reload_module)


from . import validation
from . import UI
from . import UI_material
from . import import_alo
from . import import_ala
from . import export_alo
from . import export_ala
from . import settings
from . import utils

classes = (
    import_alo.ALO_Importer,
    import_ala.ALA_Importer,
    export_alo.ALO_Exporter,
    export_ala.ALA_Exporter,
)


# blender registration
def menu_func_import(self, context):
    self.layout.operator(import_alo.ALO_Importer.bl_idname, text=".ALO Importer")
    self.layout.operator(import_ala.ALA_Importer.bl_idname, text=".ALA Importer")


def menu_func_export(self, context):
    self.layout.operator(export_alo.ALO_Exporter.bl_idname, text=".ALO Exporter")
    self.layout.operator(export_ala.ALA_Exporter.bl_idname, text=".ALA Exporter")


def register():
    import_modules()
    UI.register()
    UI_material.register()

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    UI.unregister()
    UI_material.unregister()

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

import bpy
from bpy.props import PointerProperty

from . Properties import venvProperties
from . Preferences import venvPreferences
from . Operators import PREFERENCES_OT_create_activate_venv
from . Operators import PREFERENCES_OT_install_requirements_venv
from . Operators import PREFERENCES_OT_deactivate_destroy_venv

bl_info = {
    "name": "VirtualEnvironmentManager",
    "author": "Spectral Vectors",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Addon Preferences",
    "description": "Creates a Virtual Environment to install Python packages",
    "warning": "Under Development",
    "doc_url": "",
    "category": "Interface",
}

classes = [
    venvProperties,
    venvPreferences,
    PREFERENCES_OT_create_activate_venv,
    PREFERENCES_OT_install_requirements_venv,
    PREFERENCES_OT_deactivate_destroy_venv
]


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.bpy_venv_props = PointerProperty(type=venvProperties)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.bpy_venv_props


if __name__ == "__package__":
    register()

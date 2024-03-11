import os
import sys
import bpy
from bpy.types import PropertyGroup
from bpy.props import StringProperty
from bpy.props import BoolProperty


class venvProperties(PropertyGroup):

    venv_name: StringProperty(
        name="venv Name",
        description="The name you assign to the virtual environment folder",
        default='',
    )

    directory: StringProperty(
        name="Parent Directory",
        description="The folder in which to create the virtual environment",
        default=os.path.expanduser('~\\Documents'),
        subtype='DIR_PATH',
    )

    requirements: StringProperty(
        name="requirements.txt",
        description="A list of required Python packages to install",
        default='',
        subtype='FILE_PATH'
    )

    blender_python: StringProperty(
        name="Blender Python",
        description="Blender's default Python interpreter",
        default=sys.executable,
    )

    venv_python: StringProperty(
        name="venv Python",
        description="The virtual environment's Python interpreter",
        default='',
    )

    venv_scripts: StringProperty(
        name="venv Scripts",
        description="The virtual environment's Scripts directory",
        default='',
    )

    venv_packages: StringProperty(
        name="venv Packages",
        description="The location of the virtual environment's site-packages",
        default='',
    )

    version: StringProperty(
        name="Python Version",
        description="Version number of the virtual environment's Python",
        default=sys.version[:4],
    )

    windows: BoolProperty(
        name="Windows",
        description='True if the OS is Windows',
        default=sys.platform.startswith('win'),
    )

    venv_active: BoolProperty(
        name="venv Active",
        description='True if the Virtual Environment is Active',
        default=False,
    )

import venv
import os
import sys
import subprocess
import bpy
from bpy.types import Operator


class PREFERENCES_OT_create_activate_venv(Operator):
    """Creates and Activates a Virtual Environment"""
    bl_idname = "bpy_venv.create_activate"
    bl_label = "Create & Activate"

    def execute(self, context):
        props = context.scene.bpy_venv_props
        venv_name = props.venv_name
        parent_directory = props.directory

        venv_path = os.path.join(parent_directory, venv_name)
        venv.create(venv_path)

        # Get path to executable
        props.venv_scripts = os.path.join(venv_path, 'Scripts')
        python = 'python.exe' if props.windows else 'python'
        props.venv_python = os.path.join(props.venv_scripts, python)

        # Get path to site-packages
        win_packages = 'Lib\\site-packages'
        unix_packages = f'lib\\python{props.version}\\site-packages'
        site_packages = win_packages if props.windows else unix_packages
        props.venv_packages = os.path.join(venv_path, site_packages)

        # Activate the Virtual Environment
        os.chdir(props.venv_scripts)
        activate = 'activate.bat' if props.windows else 'activate'
        subprocess.check_call([activate])

        # Set Blender's Python to use the Virtual Env's Python binary
        sys.executable = props.venv_python
        # Add the Virtual Environment's site-packages to sys.path
        sys.path.append(props.venv_packages)
        props.venv_active = True

        return {'FINISHED'}


class PREFERENCES_OT_install_requirements_venv(Operator):
    """Installs the listed Python packages in a requirements.txt file"""
    bl_idname = "bpy_venv.install_requirements"
    bl_label = "Install requirements.txt"

    def execute(self, context):
        props = context.scene.bpy_venv_props
        if not props.requirements == '':
            # Ensure and Upgrade pip
            pip_install = ["python", "-m", "pip", "install"]
            pip_calls = [
                ["python", "-m", "ensurepip"],
                [*pip_install, "--upgrade", "pip"],
            ]
            for call in pip_calls:
                subprocess.check_call(call)

            # Install packages from the requirements.txt file
            requirements_path = props.requirements
            requirements = open(requirements_path)
            packages = requirements.readlines()
            requirements.close()

            for package in packages:
                subprocess.check_call([*pip_install, package])

            return {'FINISHED'}
        else:
            return {'CANCELLED'}


class PREFERENCES_OT_deactivate_destroy_venv(Operator):
    """Deactivates the Virtual Environment and restores Blender's defaults"""
    bl_idname = "bpy_venv.deactivate_destroy"
    bl_label = "Deactivate & Remove"

    def execute(self, context):
        props = context.scene.bpy_venv_props
        # Dectivate the Virtual Environment
        os.chdir(props.venv_scripts)
        deactivate = 'deactivate.bat' if props.windows else 'deactivate'
        subprocess.check_call([deactivate])

        # Set Blender's Python interpreter back to default
        sys.executable = props.blender_python
        # Remove the Virtual Environment's site-packages from sys.path
        sys.path.remove(props.venv_packages)
        props.venv_active = False

        return {'FINISHED'}

import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty


class venvPreferences(AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout
        props = context.scene.bpy_venv_props
        active = props.venv_active

        column = layout.column(align=True)
        column.label(text="Virtual Environment", icon='FILE_SCRIPT')
        if not active:
            column.prop(props, 'venv_name')
            column.prop(props, 'directory')
            column.operator('bpy_venv.create_activate')
        if active:
            box = column.box()
            box.label(
                text=f'venv: {props.venv_name} is Active',
                icon='DESKTOP')
            box.label(
                text=f'Location: {props.directory}\\{props.venv_name}',
                icon='FILE_FOLDER')
            column = layout.column(align=False)
            row = column.row()
            row.prop(props, 'requirements', text='', icon='TEXT')
            row.operator('bpy_venv.install_requirements')
            column.operator('bpy_venv.deactivate_destroy')

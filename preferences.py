import bpy
from . import addon_updater_ops


@addon_updater_ops.make_annotations
class BRCP_preferences(bpy.types.AddonPreferences):
    """Blender Rich Presence Plus preferences/updater"""
    bl_idname = __package__

    # Updater preferences
    auto_check_update: bpy.props.BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=True)

    updater_interval_months: bpy.props.IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0)

    updater_interval_days: bpy.props.IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
        max=31)

    updater_interval_hours: bpy.props.IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23)

    updater_interval_minutes: bpy.props.IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59)

    # Version
    text_category: bpy.props.BoolProperty(
        name="Text category",
        description="Options where you can modify everything it'll display",
        default=False
    )

    version_text: bpy.props.StringProperty(
        name="Version text (When hovering on big icon)",
        description="Replace displayed version by custom text",
        default='Version {blender_version}'
    )

    blendfile_text: bpy.props.StringProperty(
        name="Upper row",
        description="Replace file name by custom text",
        default='{file_name}.blend'
    )

    workspace_text: bpy.props.StringProperty(
        name="Lower row",
        description="Replace workspace by custom text",
        default='{workspace} {render_state}'
    )

    # Whitelisted workspaces
    blacklist_workspaces: bpy.props.BoolProperty(
        name="Hide workspaces except:",
        description="Blacklists unselected workspaces",
        default=False
    )

    workspace_default: bpy.props.BoolProperty(
        name="Default workspace",
        description="Workspace you begin in by default",
        default=True
    )

    workspace_sculpting: bpy.props.BoolProperty(
        name="Sculpting workspace",
        description="Workspace for mesh sculpt",
        default=True
    )

    workspace_uv: bpy.props.BoolProperty(
        name="UV workspaces",
        description="Workspaces for mesh UV editing",
        default=True
    )

    workspace_texture: bpy.props.BoolProperty(
        name="Texture workspaces",
        description="Workspaces for texture editing",
        default=True
    )

    workspace_shading: bpy.props.BoolProperty(
        name="Shading workspace",
        description="Workspace for object shading",
        default=True
    )

    workspace_animation: bpy.props.BoolProperty(
        name="Animation workspace",
        description="Workspace for animation",
        default=True
    )

    workspace_rendering: bpy.props.BoolProperty(
        name="Rendering workspace",
        description="Workspace for scene rendering",
        default=True
    )

    workspace_compositing: bpy.props.BoolProperty(
        name="Compositing workspace",
        description="Workspace for scene composition",
        default=True
    )

    workspace_scripting: bpy.props.BoolProperty(
        name="Scripting workspace",
        description="Workspace for Python related scripting",
        default=True
    )

    workspace_geometry_nodes: bpy.props.BoolProperty(
        name="Geometry nodes workspace",
        description="Workspace for Geometry node work",
        default=True
    )

    workspace_2d: bpy.props.BoolProperty(
        name="2D related workspaces",
        description="Workspaces for 2D related work",
        default=True
    )

    workspace_motiontracking: bpy.props.BoolProperty(
        name="Motion tracking workspace",
        description="Workspace related to VFX motion tracking",
        default=True
    )

    workspace_masking: bpy.props.BoolProperty(
        name="Masking workspace",
        description="Worksapce related to VFX masking",
        default=True
    )

    workspace_video: bpy.props.BoolProperty(
        name="Video editing workspace",
        description="Workspace related to editing videos",
        default=True
    )

    workspace_custom: bpy.props.BoolProperty(
        name="Custom workspaces",
        description="Any other workspace that isn't the Blender default",
        default=True
    )

    display_state: bpy.props.BoolProperty(
        name="Show user state",
        description="Displays the user state as the small image in the Rich Presence",
        default=True
    )

    # Blacklisted states
    blacklist_states: bpy.props.BoolProperty(
        name="Hide state except:",
        description="Blacklists unselected states",
        default=False
    )

    state_object: bpy.props.BoolProperty(
        name="Object mode",
        default=True
    )

    state_edit: bpy.props.BoolProperty(
        name="Edit mode",
        default=True
    )

    state_sculpt: bpy.props.BoolProperty(
        name="Sculpt mode",
        default=True
    )

    state_pose: bpy.props.BoolProperty(
        name="Pose mode",
        default=True
    )

    state_weightpaint: bpy.props.BoolProperty(
        name="Weight paint",
        default=True
    )

    state_texturepaint: bpy.props.BoolProperty(
        name="Texture paint",
        default=True
    )

    state_vertexpaint: bpy.props.BoolProperty(
        name="Vertex paint",
        default=True
    )

    state_pencil: bpy.props.BoolProperty(
        name="Grease pencil paint",
        default=True
    )

    others_category: bpy.props.BoolProperty(
        name="Others category",
        description="Options for other categories that arent's so important",
        default=False
    )

    # Name
    add_space_on_capital_letters: bpy.props.BoolProperty(
        name="Add spaces before capital letters",
        default=False
    )

    # Render
    display_render_engine: bpy.props.BoolProperty(
        name="Show render engine",
        default=True
    )

    # Time
    display_time: bpy.props.BoolProperty(
        name="Show elapsed time",
        default=True
    )

    display_render_time: bpy.props.BoolProperty(
        name="Show approximate render end time",
        default=True
    )

    def draw(self, context):
        layout = self.layout
        settings = addon_updater_ops.get_user_preferences(context)

        box = layout.box()
        box.label(text="Using the following key strings will replace them for their description")
        box.label(text="{file_name} = Current Blend file name")
        box.label(text="{folder_name} = Blend file's Folder name")
        box.label(text="{full_path} = Full Blend file directory")
        box.label(text="{workspace} = Current workspace")
        box.label(text="{blender_version} = Current Blender version")
        box.label(text="{file_size} = Current blend file size")
        box.label(text="{render_state} = Render state (And which engine if activated) only when rendering")

        col = layout.row()
        col.prop(self, 'text_category', emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.text_category else 'DISCLOSURE_TRI_RIGHT')

        # Version
        if self.text_category:
            row = layout.row()
            row.prop(self, 'version_text')

            # Blend file
            col = layout.column()
            col.prop(self, 'blendfile_text')

            # Workspace
            col.prop(self, 'workspace_text')

            col = layout.column()
            col.prop(self, 'blacklist_workspaces')

            if self.blacklist_workspaces:
                row = layout.row()
                row.prop(self, 'workspace_default', icon='CHECKBOX_HLT' if self.workspace_default else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_sculpting', icon='CHECKBOX_HLT' if self.workspace_sculpting else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_uv', icon='CHECKBOX_HLT' if self.workspace_uv else 'CHECKBOX_DEHLT')
                row = layout.row()
                row.prop(self, 'workspace_texture', icon='CHECKBOX_HLT' if self.workspace_texture else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_shading', icon='CHECKBOX_HLT' if self.workspace_shading else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_animation', icon='CHECKBOX_HLT' if self.workspace_animation else 'CHECKBOX_DEHLT')
                row = layout.row()
                row.prop(self, 'workspace_rendering', icon='CHECKBOX_HLT' if self.workspace_rendering else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_compositing', icon='CHECKBOX_HLT' if self.workspace_compositing else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_geometry_nodes', icon='CHECKBOX_HLT' if self.workspace_compositing else 'CHECKBOX_DEHLT')
                row = layout.row()
                row.prop(self, 'workspace_scripting', icon='CHECKBOX_HLT' if self.workspace_scripting else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_2d', icon='CHECKBOX_HLT' if self.workspace_2d else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_motiontracking', icon='CHECKBOX_HLT' if self.workspace_motiontracking else 'CHECKBOX_DEHLT')
                row = layout.row()
                row.prop(self, 'workspace_masking', icon='CHECKBOX_HLT' if self.workspace_masking else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_video', icon='CHECKBOX_HLT' if self.workspace_video else 'CHECKBOX_DEHLT')
                row.prop(self, 'workspace_custom', icon='CHECKBOX_HLT' if self.workspace_custom else 'CHECKBOX_DEHLT')

        row = layout.row()
        row.prop(self, 'others_category', emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.others_category else 'DISCLOSURE_TRI_RIGHT')

        if self.others_category:
            # State
            row = layout.row()
            row.prop(self, 'display_state')
            row.prop(self, 'display_render_engine')

            row = layout.row()
            row.prop(self, 'display_time')
            row.prop(self, 'display_render_time')

            row = layout.row()
            row.prop(self, 'add_space_on_capital_letters')

            col = layout.column()
            col.prop(self, 'blacklist_states')

            if self.blacklist_states:
                row = layout.row()
                row.prop(self, 'state_object', icon='CHECKBOX_HLT' if self.state_object else 'CHECKBOX_DEHLT')
                row.prop(self, 'state_edit', icon='CHECKBOX_HLT' if self.state_edit else 'CHECKBOX_DEHLT')
                row.prop(self, 'state_sculpt', icon='CHECKBOX_HLT' if self.state_sculpt else 'CHECKBOX_DEHLT')
                row = layout.row()
                row.prop(self, 'state_pose', icon='CHECKBOX_HLT' if self.state_pose else 'CHECKBOX_DEHLT')
                row.prop(self, 'state_weightpaint', icon='CHECKBOX_HLT' if self.state_weightpaint else 'CHECKBOX_DEHLT')
                row.prop(self, 'state_texturepaint', icon='CHECKBOX_HLT' if self.state_texturepaint else 'CHECKBOX_DEHLT')
                row = layout.row()
                row.prop(self, 'state_vertexpaint', icon='CHECKBOX_HLT' if self.state_vertexpaint else 'CHECKBOX_DEHLT')
                row.prop(self, 'state_pencil', icon='CHECKBOX_HLT' if self.state_pencil else 'CHECKBOX_DEHLT')

        col = layout.column()

        addon_updater_ops.update_settings_ui(self, context)

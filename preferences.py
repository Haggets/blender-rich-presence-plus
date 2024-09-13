import bpy
from bpy.props import BoolProperty, StringProperty


class RPP_preferences(bpy.types.AddonPreferences):
    """Blender Rich Presence Plus preferences"""

    bl_idname = __package__

    top_row_text: StringProperty(name="Top Row Text", default="{file_name}")
    bottom_row_text: StringProperty(
        name="Bottom Row Text", default="{workspace} {render_state}"
    )
    image_hover_text: StringProperty(
        name="Hover text", default="Version {blender_version}"
    )

    display_elapsed_time: BoolProperty(name="Display elapsed time", default=True)
    strip_blend_suffix: BoolProperty(name="Strip .blend suffix", default=False)

    def draw(self, context):
        layout = self.layout
        main_col = layout.column()

        prefs_col = main_col.column()
        prefs_col.prop(self, "top_row_text")
        prefs_col.prop(self, "bottom_row_text")
        prefs_col.prop(self, "image_hover_text")
        prefs_col.prop(self, "display_elapsed_time")
        prefs_col.prop(self, "strip_blend_suffix")

        help_box = main_col.box()
        help_box.label(
            text="Using the following key strings will replace them for their description"
        )
        help_box.label(text=r"Blend file", icon_value="")
        help_box.label(text=r"{file_name} = Current Blend file name")
        help_box.label(text=r"{folder_name} = Blend file's Folder name")
        help_box.label(text=r"{full_path} = Full Blend file directory")

        help_box.label(text=r"{workspace} = Current workspace")
        help_box.label(text=r"{blender_version} = Current Blender version")
        help_box.label(text=r"{file_size} = Current blend file size")
        help_box.label(
            text=r"{render_state} = Render state (And which engine if activated) only when rendering"
        )

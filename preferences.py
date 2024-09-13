import bpy
from bpy.props import BoolProperty, StringProperty


class BRCP_preferences(bpy.types.AddonPreferences):
    """Blender Rich Presence Plus preferences"""

    bl_idname = __package__

    # Version
    text_category: BoolProperty(
        name="Text category",
        description="Options where you can modify everything it'll display",
        default=False,
    )

    version_text: StringProperty(
        name="Version text (When hovering on big icon)",
        description="Replace displayed version by custom text",
        default="Version {blender_version}",
    )

    blendfile_text: StringProperty(
        name="Upper row",
        description="Replace file name by custom text",
        default="{file_name}.blend",
    )

    workspace_text: StringProperty(
        name="Lower row",
        description="Replace workspace by custom text",
        default="{workspace} {render_state}",
    )

    # Whitelisted workspaces
    blacklist_workspaces: BoolProperty(
        name="Hide workspaces except:",
        description="Blacklists unselected workspaces",
        default=False,
    )

    workspace_default: BoolProperty(
        name="Default workspace",
        description="Workspace you begin in by default",
        default=True,
    )

    workspace_sculpting: BoolProperty(
        name="Sculpting workspace",
        description="Workspace for mesh sculpt",
        default=True,
    )

    workspace_uv: BoolProperty(
        name="UV workspaces", description="Workspaces for mesh UV editing", default=True
    )

    workspace_texture: BoolProperty(
        name="Texture workspaces",
        description="Workspaces for texture editing",
        default=True,
    )

    workspace_shading: BoolProperty(
        name="Shading workspace",
        description="Workspace for object shading",
        default=True,
    )

    workspace_animation: BoolProperty(
        name="Animation workspace", description="Workspace for animation", default=True
    )

    workspace_rendering: BoolProperty(
        name="Rendering workspace",
        description="Workspace for scene rendering",
        default=True,
    )

    workspace_compositing: BoolProperty(
        name="Compositing workspace",
        description="Workspace for scene composition",
        default=True,
    )

    workspace_scripting: BoolProperty(
        name="Scripting workspace",
        description="Workspace for Python related scripting",
        default=True,
    )

    workspace_geometry_nodes: BoolProperty(
        name="Geometry nodes workspace",
        description="Workspace for Geometry node work",
        default=True,
    )

    workspace_2d: BoolProperty(
        name="2D related workspaces",
        description="Workspaces for 2D related work",
        default=True,
    )

    workspace_motiontracking: BoolProperty(
        name="Motion tracking workspace",
        description="Workspace related to VFX motion tracking",
        default=True,
    )

    workspace_masking: BoolProperty(
        name="Masking workspace",
        description="Worksapce related to VFX masking",
        default=True,
    )

    workspace_video: BoolProperty(
        name="Video editing workspace",
        description="Workspace related to editing videos",
        default=True,
    )

    workspace_custom: BoolProperty(
        name="Custom workspaces",
        description="Any other workspace that isn't the Blender default",
        default=True,
    )

    display_state: BoolProperty(
        name="Show user state",
        description="Displays the user state as the small image in the Rich Presence",
        default=True,
    )

    # Blacklisted states
    blacklist_states: BoolProperty(
        name="Hide state except:",
        description="Blacklists unselected states",
        default=False,
    )

    state_object: BoolProperty(name="Object mode", default=True)

    state_edit: BoolProperty(name="Edit mode", default=True)

    state_sculpt: BoolProperty(name="Sculpt mode", default=True)

    state_pose: BoolProperty(name="Pose mode", default=True)

    state_weightpaint: BoolProperty(name="Weight paint", default=True)

    state_texturepaint: BoolProperty(name="Texture paint", default=True)

    state_vertexpaint: BoolProperty(name="Vertex paint", default=True)

    state_pencil: BoolProperty(name="Grease pencil paint", default=True)

    others_category: BoolProperty(
        name="Others category",
        description="Options for other categories that arent's so important",
        default=False,
    )

    # Name
    add_space_on_capital_letters: BoolProperty(
        name="Add spaces before capital letters", default=False
    )

    # Render
    display_render_engine: BoolProperty(name="Show render engine", default=True)

    # Time
    display_time: BoolProperty(name="Show elapsed time", default=True)

    display_render_time: BoolProperty(
        name="Show approximate render end time", default=True
    )

    def draw(self, context):
        layout = self.layout

        help_box = layout.box()
        help_box.label(
            text="Using the following key strings will replace them for their description"
        )
        help_box.label(text=r"{file_name} = Current Blend file name")
        help_box.label(text=r"{folder_name} = Blend file's Folder name")
        help_box.label(text=r"{full_path} = Full Blend file directory")
        help_box.label(text=r"{workspace} = Current workspace")
        help_box.label(text=r"{blender_version} = Current Blender version")
        help_box.label(text=r"{file_size} = Current blend file size")
        help_box.label(
            text=r"{render_state} = Render state (And which engine if activated) only when rendering"
        )

        col = layout.row()
        col.prop(
            self,
            "text_category",
            emboss=False,
            icon=(
                "DISCLOSURE_TRI_DOWN" if self.text_category else "DISCLOSURE_TRI_RIGHT"
            ),
        )

        # Version
        if self.text_category:
            row = layout.row()
            row.prop(self, "version_text")

            # Blend file
            col = layout.column()
            col.prop(self, "blendfile_text")

            # Workspace
            col.prop(self, "workspace_text")

            col = layout.column()
            col.prop(self, "blacklist_workspaces")

            if self.blacklist_workspaces:
                row = layout.row()
                row.prop(
                    self,
                    "workspace_default",
                    icon="CHECKBOX_HLT" if self.workspace_default else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "workspace_sculpting",
                    icon=(
                        "CHECKBOX_HLT" if self.workspace_sculpting else "CHECKBOX_DEHLT"
                    ),
                )
                row.prop(
                    self,
                    "workspace_uv",
                    icon="CHECKBOX_HLT" if self.workspace_uv else "CHECKBOX_DEHLT",
                )
                row = layout.row()
                row.prop(
                    self,
                    "workspace_texture",
                    icon="CHECKBOX_HLT" if self.workspace_texture else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "workspace_shading",
                    icon="CHECKBOX_HLT" if self.workspace_shading else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "workspace_animation",
                    icon=(
                        "CHECKBOX_HLT" if self.workspace_animation else "CHECKBOX_DEHLT"
                    ),
                )
                row = layout.row()
                row.prop(
                    self,
                    "workspace_rendering",
                    icon=(
                        "CHECKBOX_HLT" if self.workspace_rendering else "CHECKBOX_DEHLT"
                    ),
                )
                row.prop(
                    self,
                    "workspace_compositing",
                    icon=(
                        "CHECKBOX_HLT"
                        if self.workspace_compositing
                        else "CHECKBOX_DEHLT"
                    ),
                )
                row.prop(
                    self,
                    "workspace_geometry_nodes",
                    icon=(
                        "CHECKBOX_HLT"
                        if self.workspace_compositing
                        else "CHECKBOX_DEHLT"
                    ),
                )
                row = layout.row()
                row.prop(
                    self,
                    "workspace_scripting",
                    icon=(
                        "CHECKBOX_HLT" if self.workspace_scripting else "CHECKBOX_DEHLT"
                    ),
                )
                row.prop(
                    self,
                    "workspace_2d",
                    icon="CHECKBOX_HLT" if self.workspace_2d else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "workspace_motiontracking",
                    icon=(
                        "CHECKBOX_HLT"
                        if self.workspace_motiontracking
                        else "CHECKBOX_DEHLT"
                    ),
                )
                row = layout.row()
                row.prop(
                    self,
                    "workspace_masking",
                    icon="CHECKBOX_HLT" if self.workspace_masking else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "workspace_video",
                    icon="CHECKBOX_HLT" if self.workspace_video else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "workspace_custom",
                    icon="CHECKBOX_HLT" if self.workspace_custom else "CHECKBOX_DEHLT",
                )

        row = layout.row()
        row.prop(
            self,
            "others_category",
            emboss=False,
            icon=(
                "DISCLOSURE_TRI_DOWN"
                if self.others_category
                else "DISCLOSURE_TRI_RIGHT"
            ),
        )

        if self.others_category:
            # State
            row = layout.row()
            row.prop(self, "display_state")
            row.prop(self, "display_render_engine")

            row = layout.row()
            row.prop(self, "display_time")
            row.prop(self, "display_render_time")

            row = layout.row()
            row.prop(self, "add_space_on_capital_letters")

            col = layout.column()
            col.prop(self, "blacklist_states")

            if self.blacklist_states:
                row = layout.row()
                row.prop(
                    self,
                    "state_object",
                    icon="CHECKBOX_HLT" if self.state_object else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "state_edit",
                    icon="CHECKBOX_HLT" if self.state_edit else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "state_sculpt",
                    icon="CHECKBOX_HLT" if self.state_sculpt else "CHECKBOX_DEHLT",
                )
                row = layout.row()
                row.prop(
                    self,
                    "state_pose",
                    icon="CHECKBOX_HLT" if self.state_pose else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "state_weightpaint",
                    icon="CHECKBOX_HLT" if self.state_weightpaint else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "state_texturepaint",
                    icon=(
                        "CHECKBOX_HLT" if self.state_texturepaint else "CHECKBOX_DEHLT"
                    ),
                )
                row = layout.row()
                row.prop(
                    self,
                    "state_vertexpaint",
                    icon="CHECKBOX_HLT" if self.state_vertexpaint else "CHECKBOX_DEHLT",
                )
                row.prop(
                    self,
                    "state_pencil",
                    icon="CHECKBOX_HLT" if self.state_pencil else "CHECKBOX_DEHLT",
                )

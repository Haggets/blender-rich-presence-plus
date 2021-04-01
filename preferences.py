import bpy

class RichPresencePreferences(bpy.types.AddonPreferences):
    """Blender Rich Presence preferences"""

    bl_idname = __package__

    #Version
    version_category : bpy.props.BoolProperty(
        name="Version category",
        description="Options related to the version Blender is on",
        default=False
    )

    display_version : bpy.props.EnumProperty(
        name="Display on large image text",
        description="If to display the version Blender is currently on, custom text or nothing",
        items=[
            ('OP1', "Blender version", "Displays current Blender version"),
            ('OP2', "Custom text", "Displays custom text of your preference"),
            ('OP3', "Nothing", "Keeps the large text empty")
        ],
        default='OP1'
    )

    version_custom_text : bpy.props.StringProperty(
        name="Custom version text",
        description="Replace displayed version by custom text",
        default=''
    )

    #Blend file
    blendfile_category : bpy.props.BoolProperty(
        name="Blend file category",
        description="Options related to the blend file",
        default=False
    )

    display_blendfile : bpy.props.EnumProperty(
        name="Display on status:",
        description="if to display just the file name, the full path or custom text",
        items=[
            ('OP1', "File name", "Display only the blend file name"),
            ('OP2', "Full path", "Displays full path to the blend file"),
            ('OP3', "Custom text", "Displays custom text of your preference"),
            ('OP4', "Nothing", "Keeps details empty")
        ],
        default='OP1'
    )

    blendfile_custom_text : bpy.props.StringProperty(
        name="Custom blend file text",
        description="Replace file name by custom text",
        default=''
    )

    #Workspaces
    workspace_category : bpy.props.BoolProperty(
        name="Workspace category",
        description="Options related to the workspace the user is in",
        default=False
    )

    display_workspace : bpy.props.EnumProperty(
        name="Display on details",
        description="If to display the workspace the user is in, custom text or nothing",
        items=[
            ('OP1', "Workspace", "Displays workspace"),
            ('OP2', "Custom text", "Displays custom text of your preference"),
            ('OP3', "Nothing", "Keeps the status space empty")
        ],
        default='OP1'
    )

    workspace_custom_text : bpy.props.StringProperty(
        name="Custom workspace text",
        description="Replace workspace by custom text",
        default=''
    )

    #Whitelisted workspaces
    blacklist_workspaces : bpy.props.BoolProperty(
        name="Hide workspaces except:",
        description="Blacklists unselected workspaces",
        default=False
    )

    workspace_default : bpy.props.BoolProperty(
        name="Default workspace",
        description="Workspace you begin in by default",
        default=True
    )
    
    workspace_sculpting : bpy.props.BoolProperty(
        name="Sculpting workspace",
        description="Workspace for mesh sculpt",
        default=True
    )

    workspace_uv : bpy.props.BoolProperty(
        name="UV workspaces",
        description="Workspaces for mesh UV editing",
        default=True
    )

    workspace_texture : bpy.props.BoolProperty(
        name="Texture workspaces",
        description="Workspaces for texture editing",
        default=True
    )

    workspace_shading : bpy.props.BoolProperty(
        name="Shading workspace",
        description="Workspace for object shading",
        default=True
    )

    workspace_animation : bpy.props.BoolProperty(
        name="Animation workspace",
        description="Workspace for animation",
        default=True
    )

    workspace_rendering : bpy.props.BoolProperty(
        name="Rendering workspace",
        description="Workspace for scene rendering",
        default=True
    )
    
    workspace_compositing : bpy.props.BoolProperty(
        name="Compositing workspace",
        description="Workspace for scene composition",
        default=True
    )

    workspace_scripting : bpy.props.BoolProperty(
        name="Scripting workspace",
        description="Workspace for Python related scripting",
        default=True
    )

    workspace_2d : bpy.props.BoolProperty(
        name="2D related workspaces",
        description="Workspaces for 2D related work",
        default=True
    )

    workspace_motiontracking : bpy.props.BoolProperty(
        name="Motion tracking workspace",
        description="Workspace related to VFX motion tracking",
        default=True
    )

    workspace_masking : bpy.props.BoolProperty(
        name="Masking workspace",
        description="Worksapce related to VFX masking",
        default=True
    )

    workspace_video : bpy.props.BoolProperty(
        name="Video editing workspace",
        description="Workspace related to editing videos",
        default=True
    )

    workspace_custom : bpy.props.BoolProperty(
        name="Custom workspaces",
        description="Any other workspace that isn't the Blender default",
        default=True
    )

    #States/Modes
    state_category : bpy.props.BoolProperty(
        name="State category",
        description="Options related to the state/mode the user is in (Object, Edit, Pose...)",
        default=False
    )

    display_state : bpy.props.BoolProperty(
        name="Show user state",
        description="Displays the user state as the small image in the Rich Presence",
        default=True
    )

    #Blacklisted states
    blacklist_states : bpy.props.BoolProperty(
        name="Hide status except:",
        description="Blacklists unselected states",
        default=False
    )

    state_object : bpy.props.BoolProperty(
        name="Object mode",
        default=True
    )
    
    state_edit : bpy.props.BoolProperty(
        name="Edit mode",
        default=True
    )

    state_sculpt : bpy.props.BoolProperty(
        name="Sculpt mode",
        default=True
    )

    state_pose : bpy.props.BoolProperty(
        name="Pose mode",
        default=True
    )

    state_weightpaint : bpy.props.BoolProperty(
        name="Weight paint",
        default=True
    )

    state_texturepaint : bpy.props.BoolProperty(
        name="Texture paint",
        default=True
    )

    state_vertexpaint : bpy.props.BoolProperty(
        name="Vertex paint",
        default=True
    )

    state_pencil : bpy.props.BoolProperty(
        name="Grease pencil paint",
        default=True
    )

    others_category : bpy.props.BoolProperty(
        name="Others category",
        description="Options for other categories that arent's so important",
        default=False
    )

    #Render
    display_render_engine : bpy.props.BoolProperty(
        name="Show render engine",
        default=True
    )

    #Time
    display_time : bpy.props.BoolProperty(
        name="Show elapsed time",
        default=True
    )

    display_render_time : bpy.props.BoolProperty(
        name="Show approximate render end time",
        default=True
    )

    def draw(self, context):
        layout = self.layout

        col = layout.row()
        col.prop(self,'version_category', emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.version_category else 'DISCLOSURE_TRI_RIGHT')

        #Version
        if self.version_category:
            row = layout.row()
            row.prop(self, 'display_version', expand=True)

            if self.display_version == 'OP2':
                col = layout.column()
                col.prop(self, 'version_custom_text')
                col.label(text='Text must be at least 2 characters', icon='ERROR')
                if len(self.version_custom_text) <= 1:
                    self.version_custom_text = ''


        row = layout.row()
        row.prop(self,'blendfile_category', emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.blendfile_category else 'DISCLOSURE_TRI_RIGHT')

        #Blend file
        if self.blendfile_category:
            row = layout.row()
            row.prop(self, 'display_blendfile', expand=True)
            
            if self.display_blendfile == 'OP3':
                col = layout.column()
                col.prop(self, 'blendfile_custom_text')
                col.label(text='Text must be at least 4 characters', icon='ERROR')
                if len(self.blendfile_custom_text) <= 3:
                    self.blendfile_custom_text = ''

        row = layout.row()
        row.prop(self,'workspace_category', emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.workspace_category else 'DISCLOSURE_TRI_RIGHT')

        #Workspace
        if self.workspace_category:
            row = layout.row()
            row.prop(self, 'display_workspace', expand=True)

            col = layout.column()
            if self.display_workspace == 'OP1':
                col.prop(self, 'blacklist_workspaces')

                if self.blacklist_workspaces:
                    col.prop(self, 'workspace_default', emboss=False, icon='CHECKBOX_HLT' if self.workspace_default else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_sculpting', emboss=False, icon='CHECKBOX_HLT' if self.workspace_sculpting else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_uv', emboss=False, icon='CHECKBOX_HLT' if self.workspace_uv else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_texture', emboss=False, icon='CHECKBOX_HLT' if self.workspace_texture else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_shading', emboss=False, icon='CHECKBOX_HLT' if self.workspace_shading else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_animation', emboss=False, icon='CHECKBOX_HLT' if self.workspace_animation else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_rendering', emboss=False, icon='CHECKBOX_HLT' if self.workspace_rendering else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_compositing', emboss=False, icon='CHECKBOX_HLT' if self.workspace_compositing else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_scripting', emboss=False, icon='CHECKBOX_HLT' if self.workspace_scripting else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_2d', emboss=False, icon='CHECKBOX_HLT' if self.workspace_2d else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_motiontracking', emboss=False, icon='CHECKBOX_HLT' if self.workspace_motiontracking else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_masking', emboss=False, icon='CHECKBOX_HLT' if self.workspace_masking else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_video', emboss=False, icon='CHECKBOX_HLT' if self.workspace_video else 'CHECKBOX_DEHLT')
                    col.prop(self, 'workspace_custom', emboss=False, icon='CHECKBOX_HLT' if self.workspace_custom else 'CHECKBOX_DEHLT')

            elif self.display_workspace == 'OP2':
                col.prop(self, 'workspace_custom_text')
                col.label(text='Text must be at least 2 characters', icon='ERROR')

                if len(self.workspace_custom_text) <= 1:
                    self.workspace_custom_text = '' 
                
        row = layout.row()
        row.prop(self, 'state_category', emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.state_category else 'DISCLOSURE_TRI_RIGHT')

        #State
        if self.state_category:
            row = layout.row()
            row.prop(self, 'display_state')

            col = layout.column()
            col.prop(self, 'blacklist_states')

            if self.blacklist_states:
                col.prop(self, 'state_object', emboss=False, icon='CHECKBOX_HLT' if self.state_object else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_edit', emboss=False, icon='CHECKBOX_HLT' if self.state_edit else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_sculpt', emboss=False, icon='CHECKBOX_HLT' if self.state_sculpt else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_pose', emboss=False, icon='CHECKBOX_HLT' if self.state_pose else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_weightpaint', emboss=False, icon='CHECKBOX_HLT' if self.state_weightpaint else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_texturepaint', emboss=False, icon='CHECKBOX_HLT' if self.state_texturepaint else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_vertexpaint', emboss=False, icon='CHECKBOX_HLT' if self.state_vertexpaint else 'CHECKBOX_DEHLT')
                col.prop(self, 'state_pencil', emboss=False, icon='CHECKBOX_HLT' if self.state_pencil else 'CHECKBOX_DEHLT')


        row = layout.row()
        row.prop(self, 'others_category',emboss=False, icon='DISCLOSURE_TRI_DOWN' if self.others_category else 'DISCLOSURE_TRI_RIGHT')

        #Others
        if self.others_category:
            if self.others_category:
                row = layout.row()
                row.prop(self, 'display_render_engine')
                row = layout.row()
                row.prop(self, 'display_time')
                row.prop(self, 'display_render_time')
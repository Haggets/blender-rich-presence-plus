import bpy

from ..preferences import RPP_preferences


def workspace(preferences: RPP_preferences):  # Gets workspace user is currently in
    if preferences.workspace_text:
        workspace = preferences.workspace_text
    else:
        workspace = None

    if workspace and len(workspace) <= 1:
        workspace = workspace + " "

    return workspace


def get_workspace(preferences: RPP_preferences):
    workspace = bpy.context.workspace.name

    if workspace == "Layout" or workspace == "Default":
        if preferences.workspace_default or not preferences.blacklist_workspaces:
            workspace = "General work"
        else:
            workspace = None

    elif workspace.count("Sculpt"):
        if preferences.workspace_sculpting or not preferences.blacklist_workspaces:
            workspace = "Sculpting"
        else:
            workspace = None

    elif workspace.count("UV"):
        if preferences.workspace_uv or not preferences.blacklist_workspaces:

            workspace = "UV editing"
        else:
            workspace = None

    elif workspace.count("Texture"):
        if preferences.workspace_texture or not preferences.blacklist_workspaces:
            if workspace.count("Paint"):
                workspace = "Texture painting"
            else:
                workspace = "Texture work"
        else:
            workspace = None

    elif workspace.count("Shading"):
        if preferences.workspace_shading or not preferences.blacklist_workspaces:
            workspace = "Shading"
        else:
            workspace = None

    elif workspace.count("2D"):
        if preferences.workspace_2d or not preferences.blacklist_workspaces:
            workspace = "2D animating"
        else:
            workspace = None

    elif workspace.count("Animation"):
        if preferences.workspace_animation or not preferences.blacklist_workspaces:
            workspace = "Animating"
        else:
            workspace = None

    elif workspace.count("Rendering"):
        if preferences.workspace_rendering or not preferences.blacklist_workspaces:
            workspace = "Rendering"
        else:
            workspace = None

    elif workspace.count("Compositing"):
        if preferences.workspace_compositing or not preferences.blacklist_workspaces:
            workspace = "Compositing"
        else:
            workspace = None

    elif workspace.count("Geometry Nodes"):
        if preferences.workspace_geometry_nodes or not preferences.blacklist_workspaces:
            workspace = "Geometry Nodes Work"
        else:
            workspace = None

    elif workspace.count("Scripting"):
        if preferences.workspace_scripting or not preferences.blacklist_workspaces:
            workspace = "Scripting"
        else:
            workspace = None

    elif workspace.count("Motion Tracking"):
        if preferences.workspace_motiontracking or not preferences.blacklist_workspaces:
            workspace = "Motion tracking"
        else:
            workspace = None

    elif workspace.count("Masking"):
        if preferences.workspace_masking or not preferences.blacklist_workspaces:
            workspace = "Masking"
        else:
            workspace = None

    elif workspace.count("Video editing"):
        if preferences.workspace_video or not preferences.blacklist_workspaces:
            workspace = "Video editing"
        else:
            workspace = None

    else:
        if preferences.workspace_custom or not preferences.blacklist_workspaces:
            pass
        else:
            workspace = None

    return workspace

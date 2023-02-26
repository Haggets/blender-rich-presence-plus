import bpy

# Updater
from . import addon_updater_ops
from . import addon_updater

from . import preferences

from bpy.app.handlers import persistent
from .pypresence import pypresence as rpc
from datetime import datetime, timedelta
from os.path import getsize

bl_info = {
    "name": "Blender Rich Presence Plus",
    "author": "Haggets",
    "version": (1, 2, 1),
    "blender": (2, 83, 0),
    "description": "Fully customizable Discord Rich Presence for Blender",
    "url": "https://github.com/Haggets/blender-rich-presence-plus",
    "wiki_url": "https://github.com/Haggets/blender-rich-presence-plus",
    "tracker_url": "https://github.com/Haggets/blender-rich-presence-plus/issues",
    "category": "System",
}


def register():

    # Registers addon updater
    addon_updater_ops.register(bl_info)

    bpy.utils.register_class(preferences.BRCP_preferences)

    try:
        RPC.connect()  # Start the handshake loop
    except:
        Global.discordopen = False
        print("Couldn't connect, retrying...")

    bpy.app.timers.register(update_presence, first_interval=1.0, persistent=True)
    bpy.app.handlers.render_init.append(start_render)
    bpy.app.handlers.render_complete.append(stop_render)
    bpy.app.handlers.render_cancel.append(stop_render)
    bpy.app.handlers.render_post.append(during_render)


def unregister():

    addon_updater_ops.unregister()

    bpy.utils.unregister_class(preferences.BRCP_preferences)

    if Global.discordopen:
        RPC.clear()  # Clears the Rich Presence before closing
        RPC.close()

    bpy.app.timers.unregister(update_presence)
    bpy.app.handlers.render_init.remove(start_render)
    bpy.app.handlers.render_complete.remove(stop_render)
    bpy.app.handlers.render_cancel.remove(stop_render)
    bpy.app.handlers.render_post.remove(during_render)


# Bot ID
client_id = '823368505465896960'

# Initializes Rich Presence
RPC = rpc.Presence(client_id)

# Rich Presence variables
state = ''
details = ''
start = datetime.now().timestamp()
large_image = 'blender'
large_text = ''
small_image = ''
small_text = ''

# Other variables


class Global():
    rendering = False
    renderstart = 0
    renderend = 0
    paststartframe = False
    endframe = 0

    referencetime = 0
    postreferencetime = 0
    estimated1 = 0
    estimated2 = 0
    reference = False

    discordopen = False
    retries = 0


if __name__ == "__main__":
    register()


def change_keystring(variable, key, replacement):
    if not replacement:
        if key == '{file_name}':
            replacement = 'New File'
        elif key == '{folder_name}':
            replacement = 'No Folder'
        elif key == '{full_path}':
            replacement = 'No Directory'
        else:
            replacement = ''

    if variable.count(key):
        variable = variable.replace(key, replacement)

    return variable


def change_all_keystrings(variable):
    pref = bpy.context.preferences.addons[__name__].preferences

    variable = change_keystring(variable, '{folder_name}', bpy.data.filepath.split('\\')[len(bpy.data.filepath.split('\\'))-2])
    variable = change_keystring(variable, '{full_path}', bpy.data.filepath)
    variable = change_keystring(variable, '{blender_version}', bpy.app.version_string)
    variable = change_keystring(variable, '{workspace}', get_workspace())
    variable = change_keystring(variable, '{render_state}', render(variable))

    if bpy.data.filepath:
        if getsize(bpy.data.filepath)/1000000 < 1:
            size = str(int(getsize(bpy.data.filepath)/1000)) + 'KB'
        else:
            size = str(int(getsize(bpy.data.filepath)/1000000)) + 'MB'

        variable = change_keystring(variable, '{file_size}', size)

        if pref.add_space_on_capital_letters:
            upperlist = []
            name = bpy.path.display_name(bpy.data.filepath)
            for c in name:
                if c.isupper():
                    upperlist.append(c)

            for c in upperlist:
                idx = name.find(c)
                prioridx = idx - 1
                if prioridx == -1:
                    continue

                if name[idx - 1].isupper():
                    continue

                name = name.replace(c, " " + c)

            name = name.strip()

            variable = change_keystring(variable, '{file_name}', name)
        else:
            variable = change_keystring(variable, '{file_name}', bpy.path.display_name(bpy.data.filepath))
    else:
        variable = change_keystring(variable, '{file_size}', 'Unknown File Size')

    return variable


def version():  # Gets currently used version of Blender
    pref = bpy.context.preferences.addons[__name__].preferences

    if pref.version_text:
        version = pref.version_text

        version = change_all_keystrings(version)
    else:
        version = None

    if version and len(version) <= 1:
        version = version + ' '

    return version


def blendfile():  # Gets file name or full file path the user is currently on
    pref = bpy.context.preferences.addons[__name__].preferences

    blendfile = ''

    if pref.blendfile_text:
        blendfile = pref.blendfile_text

        blendfile = change_all_keystrings(blendfile)

        # Removes the .blend when the scene is now, since it looks weird with it
        if blendfile.count('New File') or blendfile.count('No Folder') or blendfile.count('No Directory'):
            blendfile = blendfile.replace('.blend', '')
    else:
        blendfile = None

    # Adds filler spaces to allow for the string to be shorter than 3 letters
    if blendfile and len(blendfile) <= 3:
        blendfile = blendfile + '   '

    return blendfile


def workspace():  # Gets workspace user is currently in
    pref = bpy.context.preferences.addons[__name__].preferences

    if pref.workspace_text:
        workspace = pref.workspace_text

        workspace = change_all_keystrings(workspace)
    else:
        workspace = None

    if workspace and len(workspace) <= 1:
        workspace = workspace + ' '

    return workspace


def get_workspace():
    pref = bpy.context.preferences.addons[__name__].preferences

    workspace = bpy.context.workspace.name

    if workspace == "Layout" or workspace == "Default":
        if pref.workspace_default or not pref.blacklist_workspaces:
            workspace = "General work"
        else:
            workspace = None

    elif workspace.count("Sculpt"):
        if pref.workspace_sculpting or not pref.blacklist_workspaces:
            workspace = "Sculpting"
        else:
            workspace = None

    elif workspace.count("UV"):
        if pref.workspace_uv or not pref.blacklist_workspaces:

            workspace = "UV editing"
        else:
            workspace = None

    elif workspace.count("Texture"):
        if pref.workspace_texture or not pref.blacklist_workspaces:
            if workspace.count("Paint"):
                workspace = "Texture painting"
            else:
                workspace = "Texture work"
        else:
            workspace = None

    elif workspace.count("Shading"):
        if pref.workspace_shading or not pref.blacklist_workspaces:
            workspace = "Shading"
        else:
            workspace = None

    elif workspace.count("2D"):
        if pref.workspace_2d or not pref.blacklist_workspaces:
            workspace = "2D animating"
        else:
            workspace = None

    elif workspace.count("Animation"):
        if pref.workspace_animation or not pref.blacklist_workspaces:
            workspace = "Animating"
        else:
            workspace = None

    elif workspace.count("Rendering"):
        if pref.workspace_rendering or not pref.blacklist_workspaces:
            workspace = "Rendering"
        else:
            workspace = None

    elif workspace.count("Compositing"):
        if pref.workspace_compositing or not pref.blacklist_workspaces:
            workspace = "Compositing"
        else:
            workspace = None

    elif workspace.count("Geometry Nodes"):
        if pref.workspace_geometry_nodes or not pref.blacklist_workspaces:
            workspace = "Geometry Nodes Work"
        else:
            workspace = None

    elif workspace.count("Scripting"):
        if pref.workspace_scripting or not pref.blacklist_workspaces:
            workspace = "Scripting"
        else:
            workspace = None

    elif workspace.count("Motion Tracking"):
        if pref.workspace_motiontracking or not pref.blacklist_workspaces:
            workspace = "Motion tracking"
        else:
            workspace = None

    elif workspace.count("Masking"):
        if pref.workspace_masking or not pref.blacklist_workspaces:
            workspace = "Masking"
        else:
            workspace = None

    elif workspace.count("Video editing"):
        if pref.workspace_video or not pref.blacklist_workspaces:
            workspace = "Video editing"
        else:
            workspace = None

    else:
        if pref.workspace_custom or not pref.blacklist_workspaces:
            pass
        else:
            workspace = None

    return workspace


def render(variable):
    pref = bpy.context.preferences.addons[__name__].preferences

    render = ''

    if Global.rendering:
        # Adds a suffix to indicate that the user is rendering
        engine = bpy.context.engine

        if engine.startswith('BLENDER_'):  # Small fixup since Eevee is called "Blender_Eevee" internally
            engine = engine.replace('BLENDER_', '').title()
        else:
            engine = engine.title()

        if variable.replace('{render_state}', '').replace(' ', '').endswith('Rendering'):
            if pref.display_render_engine:
                render = " in {}".format(engine)
        else:
            if pref.display_render_engine:
                render = " (Rendering in {})".format(engine)
            else:
                render = " (Rendering)"

    return render


def get_state():  # Gets current mode user is in
    pref = bpy.context.preferences.addons[__name__].preferences

    if pref.display_state:
        state = bpy.context.mode
        image = ''

        if state == 'OBJECT':
            if pref.state_object or not pref.blacklist_states:
                state = "Object mode"
                image = 'object_mode'
            else:
                state = None
                image = None

        elif state.count('EDIT'):
            if pref.state_edit or not pref.blacklist_states:
                if state == 'EDIT_MESH':
                    state = "Edit mode (Mesh)"
                    image = 'edit_mode_mesh'
                elif state == 'EDIT_ARMATURE':
                    state = "Edit mode (Armature)"
                    image = 'edit_mode_armature'
                elif state == 'EDIT_CURVE':
                    state = "Edit mode (Curve)"
                    image = 'edit_mode_curve'
                elif state == 'EDIT_SURFACE':
                    state = "Edit mode (Surface)"
                    image = 'edit_mode_surface'
                elif state == 'EDIT_TEXT':
                    state = "Edit mode (Text)"
                    image = 'edit_mode_text'
                elif state == 'EDIT_METABALL':
                    state = "Edit mode (Metaball)"
                    image = 'edit_mode_metaball'
                elif state == 'EDIT_LATTICE':
                    state = "Edit mode (Lattice)"
                    image = 'edit_mode_lattice'
                elif state == 'EDIT_GPENCIL':
                    state = "Edit mode (Pencil)"
                    image = 'edit_mode_pencil'
            else:
                state = None
                image = None

        elif state.count('SCULPT'):
            if pref.state_sculpt or not pref.blacklist_states:
                if state == 'SCULPT':
                    state = "Sculpt mode (Mesh)"
                elif state == 'SCULPT_GPENCIL':
                    state = "Sculpt mode (Pencil)"
                image = 'sculpt_mode'
            else:
                state = None
                image = None

        elif state == 'POSE':
            if pref.state_pose or not pref.blacklist_states:
                state = "Pose mode"
                image = 'pose_mode'
            else:
                state = None
                image = None

        elif state.count('WEIGHT'):
            if pref.state_weightpaint or not pref.blacklist_states:
                if state == 'PAINT_WEIGHT':
                    state = "Weight paint"
                elif state == 'WEIGHT_GPENCIL':
                    state = "Weight paint (Pencil)"
                image = 'weight_paint'
            else:
                state = None
                image = None

        elif state == 'PAINT_TEXTURE':
            if pref.state_texturepaint or not pref.blacklist_states:
                state = "Texture paint"
                image = 'texture_paint'
            else:
                state = None
                image = None

        elif state.count('VERTEX'):
            if pref.state_vertexpaint or not pref.blacklist_states:
                if state == 'PAINT_VERTEX':
                    state = "Vertex paint"
                elif state == 'VERTEX_GPENCIL':
                    state = "Vertex paint (Pencil)"
                image = 'vertex_paint'
            else:
                state = None
                image = None

        elif state == 'PAINT_GPENCIL':
            if pref.state_pencil or not pref.blacklist_states:
                state = "Grease Pencil Paint"
                image = 'pencil_paint'
            else:
                state = None
                image = None
    else:
        state = None
        image = None

    return state, image


def get_start(*args):
    global start

    pref = bpy.context.preferences.addons[__name__].preferences

    if pref.display_time:
        time = start
    else:
        time = None

    return time


@persistent
def start_render(*args):
    Global.rendering = True
    Global.paststartframe = False
    Global.renderstart = datetime.now()


@persistent
def during_render(*args):
    pref = bpy.context.preferences.addons[__name__].preferences

    # Get total frame count
    endframe = bpy.context.scene.frame_end

    # If disabled, the time left will not be shown
    if pref.display_render_time:
        Global.paststartframe = True

    # If there is no reference time and the current frame is a reference frame
    if Global.reference:
        Global.referencetime = datetime.now()  # Get time after end of reference frame

    # If there is no post reference time and the current frame is not a reference frame
    elif not Global.reference:
        Global.postreferencetime = datetime.now()  # Time taken to render relative to the reference frame

    # Only on the first frame, gets rough time estimate
    if not Global.renderend:
        # Gets render time from subtracting first frame time spent by initial render time
        Global.estimated1 = Global.postreferencetime - Global.renderstart
        Global.renderend = Global.estimated1 * endframe  # Multiplies rendered time by total amount of frames
        Global.renderend = Global.renderstart + Global.renderend  # Sums the estimated time to the initial render time
    else:  # After first frame
        if not Global.reference:
            # Gets rendered time from subtracting current frame time spent by reference frame time
            Global.estimated2 = Global.postreferencetime - Global.referencetime
            # Sums both estimates and then divides them, averaging out the estimate
            Global.estimated1 = (Global.estimated1+Global.estimated2)/2
            Global.renderend = Global.estimated1 * endframe  # Multiplies averaged estimate by total amount of frames

            Global.renderend = Global.renderstart + Global.renderend  # Sums averaged estimated time to the intial render time

    if Global.reference:
        Global.reference = False
    elif not Global.reference:
        Global.reference = True

    #print(Global.renderstart, Global.renderend)
    # print(Global.estimated1)
    # print(Global.estimated2)
    #print('render:', Global.renderend)


@persistent
def stop_render(*args):
    Global.rendering = False
    Global.paststartframe = False

    Global.reference = False
    Global.renderend = 0


def update_presence():
    large_text = version()
    details = blendfile()
    small_text, small_image = get_state()
    state = workspace()
    start = get_start()

    if not Global.discordopen:
        try:
            RPC.connect()  # Start the handshake loop
            Global.discordopen = True
            Global.retries = 0
        except:
            if Global.retries == 5:
                print("5 failed attempts, disabling logging...")
                Global.retries += 1
            elif Global.retries < 5:
                print("Couldn't connect, retrying...")
                Global.retries += 1
            else:
                pass
    else:
        try:
            # Updates rich presence
            RPC.update(
                state=state,
                details=details,
                start=start if not Global.rendering else Global.renderstart.timestamp(),
                end=None if not Global.paststartframe else Global.renderend.timestamp(),
                large_image=large_image,
                large_text=large_text,
                small_image=small_image,
                small_text=small_text
            )
        except:
            pass

    # print('Updated')
    return 15

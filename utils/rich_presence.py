from datetime import datetime
from os.path import getsize

from bpy.app.handlers import persistent

# Rich Presence variables
state = ""
details = ""
start = datetime.now().timestamp()
large_image = "blender"
large_text = ""
small_image = ""
small_text = ""


class Global:
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


def change_keystring(variable, key, replacement):
    if not replacement:
        if key == "{file_name}":
            replacement = "New File"
        elif key == "{folder_name}":
            replacement = "No Folder"
        elif key == "{full_path}":
            replacement = "No Directory"
        else:
            replacement = ""

    if variable.count(key):
        variable = variable.replace(key, replacement)

    return variable


def change_all_keystrings(variable):
    pref = bpy.context.preferences.addons[__name__].preferences

    variable = change_keystring(
        variable,
        "{folder_name}",
        bpy.data.filepath.split("\\")[len(bpy.data.filepath.split("\\")) - 2],
    )
    variable = change_keystring(variable, "{full_path}", bpy.data.filepath)
    variable = change_keystring(variable, "{blender_version}", bpy.app.version_string)
    variable = change_keystring(variable, "{workspace}", get_workspace())
    variable = change_keystring(variable, "{render_state}", render(variable))

    if bpy.data.filepath:
        if getsize(bpy.data.filepath) / 1000000 < 1:
            size = str(int(getsize(bpy.data.filepath) / 1000)) + "KB"
        else:
            size = str(int(getsize(bpy.data.filepath) / 1000000)) + "MB"

        variable = change_keystring(variable, "{file_size}", size)

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

            variable = change_keystring(variable, "{file_name}", name)
        else:
            variable = change_keystring(
                variable, "{file_name}", bpy.path.display_name(bpy.data.filepath)
            )
    else:
        variable = change_keystring(
            variable, "{file_name}", bpy.path.display_name(bpy.data.filepath)
        )
        variable = change_keystring(variable, "{file_size}", "Unknown File Size")

    return variable

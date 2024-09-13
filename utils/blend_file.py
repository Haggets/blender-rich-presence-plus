from ..preferences import RPP_preferences


def blendfile(
    preferences: RPP_preferences,
):  # Gets file name or full file path the user is currently on
    blendfile = ""
    if not preferences.top_row_text:
        return blendfile

    blendfile = preferences.top_row_text

    if (
        blendfile.count("New File")
        or blendfile.count("No Folder")
        or blendfile.count("No Directory")
    ):
        blendfile = blendfile.replace(".blend", "")

    # Adds filler spaces to allow for the string to be shorter than 3 letters
    if blendfile and len(blendfile) <= 3:
        blendfile = blendfile + "   "

    return blendfile


def get_start(preferences: RPP_preferences):
    global start
    if not preferences.display_time:
        return

    time = start

    return time

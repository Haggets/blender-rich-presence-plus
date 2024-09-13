from ..preferences import RPP_preferences


def version(preferences: RPP_preferences):  # Gets currently used version of Blender
    version = preferences.version_text or ""

    if version and len(version) <= 1:
        version = version + " "

    return version

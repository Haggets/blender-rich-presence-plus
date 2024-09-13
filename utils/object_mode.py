import bpy

from ..preferences import RPP_preferences


def get_state(preferences: RPP_preferences):  # Gets current mode user is in
    if not preferences.display_state:
        return "", ""

    current_state = bpy.context.mode.split("_")
    if len(current_state) > 1:
        current_substate = current_state[1]
        state = f"{current_state.capitalize()} Mode ({current_substate.capitalize()})"
        image = f"{state.lower()}_mode_{current_substate.lower()}"
    else:
        state = f"{state.capitalize()} Mode"
        image = f"{state.lower()}_mode"

    return state, image

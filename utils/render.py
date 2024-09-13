from bpy.app.handlers import persistent


def render(variable):
    pref = bpy.context.preferences.addons[__name__].preferences

    render = ""

    if Global.rendering:
        # Adds a suffix to indicate that the user is rendering
        engine = bpy.context.engine

        if engine.startswith(
            "BLENDER_"
        ):  # Small fixup since Eevee is called "Blender_Eevee" internally
            engine = engine.replace("BLENDER_", "").title()
        else:
            engine = engine.title()

        if (
            variable.replace("{render_state}", "")
            .replace(" ", "")
            .endswith("Rendering")
        ):
            if pref.display_render_engine:
                render = " in {}".format(engine)
        else:
            if pref.display_render_engine:
                render = " (Rendering in {})".format(engine)
            else:
                render = " (Rendering)"

    return render


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
        Global.postreferencetime = (
            datetime.now()
        )  # Time taken to render relative to the reference frame

    # Only on the first frame, gets rough time estimate
    if not Global.renderend:
        # Gets render time from subtracting first frame time spent by initial render time
        Global.estimated1 = Global.postreferencetime - Global.renderstart
        Global.renderend = (
            Global.estimated1 * endframe
        )  # Multiplies rendered time by total amount of frames
        Global.renderend = (
            Global.renderstart + Global.renderend
        )  # Sums the estimated time to the initial render time
    else:  # After first frame
        if not Global.reference:
            # Gets rendered time from subtracting current frame time spent by reference frame time
            Global.estimated2 = Global.postreferencetime - Global.referencetime
            # Sums both estimates and then divides them, averaging out the estimate
            Global.estimated1 = (Global.estimated1 + Global.estimated2) / 2
            Global.renderend = (
                Global.estimated1 * endframe
            )  # Multiplies averaged estimate by total amount of frames

            Global.renderend = (
                Global.renderstart + Global.renderend
            )  # Sums averaged estimated time to the intial render time

    if Global.reference:
        Global.reference = False
    elif not Global.reference:
        Global.reference = True

    # print(Global.renderstart, Global.renderend)
    # print(Global.estimated1)
    # print(Global.estimated2)
    # print('render:', Global.renderend)


@persistent
def stop_render(*args):
    Global.rendering = False
    Global.paststartframe = False

    Global.reference = False
    Global.renderend = 0

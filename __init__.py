from bpy.app import handlers, timers
from bpy.utils import register_class, unregister_class

from .preferences import RPP_preferences
from .pypresence import pypresence as rpc
from .utils.render import during_render, start_render, stop_render

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

# ID of the application
client_id = "823368505465896960"
RPC = rpc.Presence(client_id)


def update_presence():
    # Updates rich presence
    RPC.update(
        state="state",
        details="details",
        # start="start" if not Global.rendering else Global.renderstart.timestamp(),
        # end=None if not Global.paststartframe else Global.renderend.timestamp(),
        # large_image=large_image,
        # large_text=large_text,
        # small_image=small_image,
        # small_text=small_text,
    )

    print("Updated")
    return 15


def register():
    register_class(RPP_preferences)

    RPC.connect()

    timers.register(update_presence, first_interval=1.0, persistent=True)
    handlers.render_init.append(start_render)
    handlers.render_complete.append(stop_render)
    handlers.render_cancel.append(stop_render)
    handlers.render_post.append(during_render)


def unregister():
    RPC.clear()
    RPC.close()

    unregister_class(RPP_preferences)

    timers.unregister(update_presence)
    handlers.render_init.remove(start_render)
    handlers.render_complete.remove(stop_render)
    handlers.render_cancel.remove(stop_render)
    handlers.render_post.remove(during_render)


if __name__ == "__main__":
    register()

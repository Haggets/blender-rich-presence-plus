[![discord](https://img.shields.io/discord/693987167210438656.svg?style=for-the-badge&label=Discord&logo=discord&color=7289DA&json?)](https://discord.gg/kH99XSU) [![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

# Blender Rich Presence Plus
Another Blender Rich Presence plugin that unlike the rest, gives you total control in terms of customization, being able to freely modify what to show, and when to show it

## Features

* Show the version Blender is currently on, custom text or nothing at all
* Show the name of the blend file, the full path of it, custom text or nothing at all
* Show the current workspace the user is on, show custom text, or nothing at all
* Filter out specific workspaces (Hide every workspace except the shading workspace, for example)
* Show the current state/mode the user is on (Object mode, Edit mode (Which includes every type of edit mode with their respective icon), sculpt mode...) or nothing at all
* Filter out specifc states/modes (Hide every state except object mode, for example)
* Show the current render engine being used while rendering (Displayed right after the workspace text), or not
* Show elapsed time since you booted up Blender, or not
* Show elapsed time since you began a render for single frame renders (The prior time will resume itself after the render is over)
* Show an estimate time to when your render will be finished for rendering animations (NOT 100% accurate)

## Examples

![information shown when in a new file while in object mode and in the default workspace](images/GeneralDemonstration.png "Default status") ![Current mode shown is a varation of edit mode, metaball in this case](images/Modes.png "Mode differences, modes are separated by what's currently being edited, with fitting images and text for them") ![Sculpting](images/Sculpting.png "Workspace and mode shown accordingly based on what you're doing and on what workspace you're in")

![Custom text displayed instead of information](images/CustomText.png "Custom text, you're able to replace information by whatever text you want")  ![All information hidden](images/FullyHidden.png "Information customization, you're able to hide everything if you so desire") ![Approximate render estimate and current engine being used](images/RenderTime.png "Approximate render estimate, NOT 100% accurate. Also current engine used for rendering")

As you can see, this plugin was made with the intention of providing as much customizability as possible in case you need or want something different, so if you want as much or as little information as possible shown about your current Blender session, this plugin will not disappoint

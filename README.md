#Mesh: Make Coplanar (v0.1)
Author: Scott Michaud

##Install Instructions:

1. Place mesh_makecoplanar.py in your Addons folder. On a default, Windows, 64-bit installation of Blender 2.72, it is probably in the following directory:

C:\Program Files\Blender Foundation\Blender\2.72\scripts\addons

2. Open Blender
3. Open User Preferences (alt + ctrl + u)
4. Click the Addons tab
5. Select the "Mesh" category
6. Click the checkbox for "Mesh: Make Coplanar"
7. (Unless you want to repeat Step 3 through Step 6 each time you turn on Blender) Click "Save User Settings" (probably in the bottom left of the Blender User Preferences pop-up window).

##Usage Instructions:

1. In Edit Mode, select 3-or-more vertices.
2. Either:
a. Press the space bar and type "Make Coplanar".
-or-
b. Press Ctrl + V (Vertex Tools Menu) and select "Make Coplanar"

These vertices will be crushed to the nearest point in an approximate plane of best fit for all selected vertices.

##TODO:

In a future release, I intend to make this an interactive tool. I expect that users would be able to:

1. Select three-or-more vertices that define your intended plane.
2. Run the "Make Coplanar" command. If four-or-more, the plane will be an approximate average of these and the vertices will snap to it.
3. Your selected vertices will deselect.
4. Select more vertices to add to plane, defined in Step 1.
5. Press "Enter" to apply these extra vertices, or "Esc" to cancel.
6. Depending on feedback, either:
a. All vertices will be deselected.
b. The original vertices (from Step 1) will be selected.
c. All affected vertices (from Step 1 and Step 4) will be selected.
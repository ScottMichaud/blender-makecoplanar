#Mesh: Make Coplanar (v0.5)

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
	1. Press the space bar and type "Make Coplanar". OR
	2. Press Ctrl + V (Vertex Tools Menu) and select "Make Coplanar"
3. The desired plane to move vertices to will be calculated:
	1. If 3 vertices were selected, it will be the plane that they form.
	2. If 4+ vertices were selected, an average plane will be calculated. These vertices will be moved onto it.
4. Your vertices will unselect.
5. Select more vertices to align with that plane.
6. Press Enter to move this second selection onto the plane, or ESC to just move the first selection (if 4+).
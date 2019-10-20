# Mesh: Make Coplanar (v0.6)

This add-on now requires 2.8x. I might consider redesigning the add-on to have a better UX if it becomes popular. It was mostly something that I hacked together to solve my use case.

## Install Instructions:

1. Download `mesh_makecoplanar.py` from this repo (ex: by clicking the `Clone or Download` button and clicking `Download Zip`).
2. Open Blender Preferences with `Edit -> Preferences`.
3. Click the `Add-ons` tab (on the left).
4. Filter your add-ons to only show `Mesh` by clicking on the filter drop-down (below `Official`) and select `Mesh`.
5. If `Mesh: Make Coplanar` exists with an author `Scott Michaud`, click `Remove` to uninstall the old version.
6. On the top right, click the `Install...` button.
7. Navigate to where you downloaded `mesh_makecoplanar.py` and `Install Add-on from File...`.
8. Click the checkbox (square) to the top-right of `Mesh: Make Coplanar`.

## Usage Instructions:

1. In Edit Mode, select 3-or-more vertices.
2. Either:
	1. Press the space bar and type "Make Coplanar". **OR**
	2. Press Ctrl + V (Vertex Tools Menu) and select "Make Coplanar"
3. The desired plane to move vertices to will be calculated:
	1. If 3 vertices were selected, it will be the plane that they form.
	2. If 4+ vertices were selected, an average plane will be calculated. These vertices will be moved onto it.
4. Your vertices will unselect.
5. Select more vertices to align with that plane.
6. Press `Enter` to move this second selection onto the plane, or `ESC` to not move the second selection.

There are two common use-cases:
1. If you have a bunch of vertices that are not coplanar, then select the vertices that closest represents the plane that you are trying to model and run the command, then select the outliers to conform them to the same plane and press `Enter`.
2. If you already have a plane, but you have some vertices that fell off of it, then select 3 vertices from the plane and run the command, then select the outlier vertices and press `Enter`.

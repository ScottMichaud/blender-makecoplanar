bl_info = {
	"name": "Make Coplanar",
	"author": "Scott Michaud",
	"version": (0, 1),
	"blender": (2, 72, 0),
	"location": "View3D > Specials > Make Coplanar",
	"description": "Forces currently selected vertices to be coplanar. TODO: Subsequent selections will conform to that plane.",
	"warning": "",
	"category": "Mesh",
}

import bpy
import bmesh
import mathutils
	
class MakeCoplanar(bpy.types.Operator):
	bl_idname = 'mesh.makecoplanar'
	bl_label = 'Make Coplanar'
	bl_options = {'REGISTER', 'UNDO'}
	
	normal = None
	distance = None
	
	
	def make_coplanar(context):
		
		bm = bmesh.from_edit_mesh(bpy.context.active_object.data)
		vtxs = bm.verts
		selected_vtxs = [i for i in vtxs if i.select]
		num = len(selected_vtxs)
		list_normals = []
		list_distances = []
		avg_normal = mathutils.Vector((0.0,0.0,0.0)) #Initialize with 3D Zero vector.
		avg_distance = 0.0
		
		if num < 3:
			return
		
		#Get a sample of normals. Each vertex will contribute to three.
		#All pairings is better, but factorial complexity -- worse than exponential.
		#This is linear and probably good enough.
		for i in range(num):
			first_next = (i + 1) % num #Allow wrapping around for last two entries.
			second_next = (i + 2) % num
			vector_1 = selected_vtxs[i].co - selected_vtxs[first_next].co
			vector_2 = selected_vtxs[i].co - selected_vtxs[second_next].co
			cross_12 = vector_1.cross(vector_2)
			cross_12.normalize()
			list_normals.append(cross_12)
		
		#Make all normals acute (or right) to one another.
		#This makes best use of floating point precision. Subtraction sucks.
		for i in range(1, num):
			test_scalar = list_normals[i].dot(list_normals[0])
			if test_scalar < 0:
				list_normals[i] = -1 * list_normals[i]
		
		#Find the average normal, then normalize it.
		for i in range(num):
			avg_normal += list_normals[i]
		avg_normal.normalize()
		
		#Get distance for each vertex to a plane that crosses origin.
		#Also, get the average.
		for i in range(num):
			distance = selected_vtxs[i].co.dot(avg_normal)
			list_distances.append(distance)
			avg_distance += distance
		avg_distance /= num
		
		#Store data for interactive tool.
		
		MakeCoplanar.normal = avg_normal
		MakeCoplanar.distance = avg_distance
		
		#No sense adjusting 3 vertices, which are already coplanar, by rounding error.
		#We have the data for future vertices.
		if num == 3:
			return
		
		#Move each vertex +/- how far it is away from the average distance...
		#... along the average normal direction.
		for i in range(num):
			delta = list_distances[i] - avg_distance
			adjust = avg_normal * delta #It's a vector, pointing in avg_normal direction, magnitude delta.
			selected_vtxs[i].co -= adjust
		
		bpy.context.active_object.data.update() #Update the base mesh.
	
	def execute(self, context):
		MakeCoplanar.make_coplanar(context)		
		bpy.context.scene.update()
		
		#Currently, exit immediately.
		return {'FINISHED'}
		
def menu_func(self, context):
	self.layout.operator(MakeCoplanar.bl_idname, text="Make Coplanar")

def register():
	bpy.utils.register_module(__name__)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.append(menu_func)

def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(menu_func)

if __name__ == "__main__":
	register()
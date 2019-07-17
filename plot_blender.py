import numpy as np
from util import *
import bpy, bmesh
import math
import mathutils

def update_camera(camera, focus_point=(0.0, 0.0, 0.0), distance=15.0):


    print("Updating camera")
    print("Old location", camera.location)
    camera.location = mathutils.Vector((0.0, 0.0, distance))
    focus_point = mathutils.Vector(focus_point)
    looking_direction = camera.location - focus_point
    rot_quat = looking_direction.to_track_quat('Z', 'Y')

    camera.rotation_euler = rot_quat.to_euler()
    camera.location = rot_quat * mathutils.Vector((0.0, 0.0, distance))
    print("New location", camera.location)




def cylinder_between(p1, p2, r):
    #print("Drawing line between", p1, p2)
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    dz = p2[2]-p1[2]
    dist = math.sqrt(dx**2 + dy**2 + dz**2)

    bpy.ops.mesh.primitive_cylinder_add(
        radius = r,
        depth = dist,
        location = (dx/2 + p1[0], dy/2 + p1[1], dz/2 + p1[2])
        )

    phi = math.atan2(dy, dx)
    theta = math.acos(dz/dist)
    bpy.context.object.rotation_euler[1] = theta
    bpy.context.object.rotation_euler[2] = phi
    #bpy.context.object.color = [176, 196, 222, 1]
    """
    activeObject = bpy.context.active_object #Set active object to variable
    mat = bpy.data.materials.new(name="MaterialName") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (1, 0, 0) #change color
    """


def render2d(string, alpha, delta=1, init_direction=np.array([1., 0]), colors={}):
    #TODO colors
    pos = np.zeros(2, dtype=np.float64)
    direction = init_direction
    color = 'k'
    saved_states = []

    for x in string:
        if x == 'F':
            new_pos = pos + direction
            #bge.render.drawLine([pos[0], pos[1], 0],[new_pos[0], new_pos[1], 0],[255,40,0])
            print(pos+[0], new_pos+[0])
            cylinder_between([pos[0], pos[1], 0],[new_pos[0], new_pos[1], 0], 0.01)
            pos = new_pos
        elif x == '+':
            direction = rotate(direction, alpha)
        elif x == '-':
            direction = rotate(direction, -alpha)
        elif x == '*':
            direction *= delta
        elif x == '/':
            direction /= delta
        elif x == '|':
            direction = rotate(direction, 180)
        elif x == '[':
            saved_states.append((pos, direction))
        elif x == ']':
            pos, direction = saved_states.pop()
        elif x in colors:
            color = colors[x]



"""

def axis_equal_3d(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize / 2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

def plot3d(string, alpha, delta=1, init_direction=np.array([1., 0, 0]), colors={}):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	pos = np.zeros(3, dtype=np.float64)
	direction = init_direction
	color = 'k'
	saved_states = []
	for x in string:
		if x == 'F':
			new_pos = pos + direction
			ax.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], [pos[2], new_pos[2]], c=color)
			pos = new_pos
		elif x == '+':
			direction = rotate_x(direction, alpha)
		elif x == '-':
			direction = rotate_x(direction, -alpha)
		elif x == '&':
			direction = rotate_y(direction, alpha)
		elif x == '^':
			direction = rotate_y(direction, -alpha)
		elif x == '<':
			direction = rotate_z(direction, alpha)
		elif x == '>':
			direction = rotate_z(direction, -alpha)
		elif x == '*':
			direction = direction * delta
		elif x == '/':
			direction = direction / delta
		elif x == '|':
			direction = rotate_x(direction, 180)
			direction = rotate_y(direction, 180)
			direction = rotate_z(direction, 180)
		elif x == '[':
			saved_states.append((pos, direction))
		elif x == ']':
			pos, direction = saved_states.pop()
		elif x in colors:
			color = colors[x]
	axis_equal_3d(ax)
	plt.show()
"""

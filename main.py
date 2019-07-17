"""
Run this from blender
exec(open("/Users/gb/lsystem/main.py").read())

What I need to do

4. Rewrite the plot lib for blender (and do an absolute import)

"""
import sys
sys.path.append('/Users/gb/lsystem')
from grammar import *
from plot_blender import *
import json

import bpy, bmesh

def delete_cube():
    objs = bpy.data.objects
    objs.remove(objs["Cube"], True)

def apply_materials():
    # The first thing is the camera, the last is the lighting. Dont select those.
    for obj in bpy.data.objects[1:-1]:
        mat = bpy.data.materials.new(name="MaterialName")
        bpy.context.scene.objects.active = obj
        active_obj = bpy.context.active_object
        active_obj.data.materials.append(mat)
        bpy.context.object.active_material.diffuse_color = (176, 196, 222)

def dragon():
    system = LSystem('FX', {'X':'X+YF+', 'Y':'-FX-Y'})
    for _ in range(10):
        system.step()
    render2d(system.state, 90, init_direction=np.array([0.1, 0]))


def render_from_files(f):
    data = json.load(open(f))

    system = LSystem(data["axiom"], data["rules"])
    for _ in range(data["number_iterations"]):
        system.step()
    render2d(system.state, data["angle"], init_direction=np.array([0.1, 0]))



def main():
    #example_code()
    delete_cube()
    update_camera(bpy.data.objects['Camera'])
    render_from_files("/Users/gb/lsystem/generated/good/24491.txt")
    apply_materials()

main()

from grammar import *
from plot import *

# Grammar

def algae():
	system = LSystem('A', {'A': 'AB', 'B': 'A'})
	for _ in range(8):
		print(system.state)
		system.step()

# 2D plots

def koch():
	system = LSystem('F', {'F': 'F+F-F-F+F'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 90)

def tree():
	system = LSystem('B', {'B': 'gF/[+B]-B*', 'g': 'b'})
	for _ in range(7):
		system.step()
	plot2d(system.state, 20, 1.2, np.array([0, 1.]), {'g': 'g', 'b': '#654321'})

def plant():
	system = LSystem('gX', {'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 25, 1, rotate(np.array([1., 0]), 50), {'g': 'g'})

def liana():
	system = LSystem('gF', {'F': 'F[+F]F[-F]F'})
	for _ in range(5):
		system.step()
	plot2d(system.state, 25, 1, np.array([0, 1.]), {'g': 'g'})

def tree3d():
	system = LSystem('B', {'B': 'gF/[+B][-B][&B]^B*', 'g': 'b'})
	for _ in range(6):
		system.step()
	plot3d(system.state, 20, 1.2, np.array([0, 0, 1.]), {'g': 'g', 'b': '#654321'})

def dragon():
	system = LSystem('FX', {'X':'X+YF+', 'Y':'-FX-Y'})
	for _ in range(10):
		system.step()
	plot2d(system.state, 90)


def pine3d():
	system = LSystem('B', {'B': 'gF/[+++B][---B][&&&B][^^^B]*gF/[++B][--B][&&B][^^B]*gF/B*', 'g': 'b'})
	print("Inital ", system.state)
	for i in range(5):
		print("Stepping ", i)
		system.step()
		#print("Step ", i, system.state)
	print("Rendering")
	plot3d(system.state, 20, 2, np.array([0, 0, 1.]), {'g': 'g', 'b': '#654321'})


"""
if x == 'F':
	new_pos = pos + direction
	plt.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], c=color)
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
"""
def test():
    #system = LSystem('gX', {'X': 'F+[[X]-X]-F[-FX]+X', 'F': 'FF'})
    #system = LSystem('gX', {'X': 'F++[[[X]-X]-X]--F[-F[[X]-X]-X]+X', 'F':'FFF'})
	system = LSystem('FX+FX+FX+FX', {'X':'*FX+FX+FX+FX/'})
	for _ in range(3):
		system.step()
	plot2d(system.state, 25, 0.5, rotate(np.array([0.1, 0]), 50))

if __name__ == '__main__':
	#dragon()
	test()

#############################################################
# Author: Caio Moreira Gomes                                #
#                                                           #
# That one is a software to compute differential equations  #
# numerically throught different methods.                   #
#                                                           #
# Every single method returns a list of pairs (t_n, y_n)    #
#############################################################

#############################
## Import libs
#############################
import matplotlib as plt
import string
import re

#############################
## Helper functions
#############################
def proc(t, y, string):
	"""
	Computes the equation without worry with the eval values.

	Args:
		t (float): The t value to compute the differential equation.
		y (float): The y value to compute the differential equation.
		string (string): The string containing the differential equation.
	
	Returns:
		float: The computed value in the equation.
	"""
	return eval(string)

def plot_graph(points):
	"""Plot the graph with matplotlib
	
	Args:
	    points (list(float, float)): The list with points (t_n, y_n)
	"""
	t_axis, y_axis = zip(*points)
	plt.pyplot.xlabel("t")
	plt.pyplot.ylabel("f'(t) = " + f)
	plt.pyplot.plot(t_axis, y_axis)

def print_points(points):
	"""Plot the graph with matplotlib
	
	Args:
	    points (list(float, float)): The list with points (t_n, y_n)
	"""
	for idx, (t, y) in enumerate(points):
		print(idx, y)
	print()


#############################
## Numerical Methods
#############################
def euler(t0, y0, h, n, f):
	"""
	Computes the Euler method.
	param t0  The initial t value to use in the numerical method.
	param y0  The initial y value to use in the numerical method.
	param h   The size of the step to use in this method.
	param n   The number of steps to perform.
	param f   The differential equation.
	
	return    The list of the computed values.
	"""
	## Define os pontos
	points = []
	t, y = t0, y0

	## Calcula os passos com o método de Euler
	for i in range(0, n):
		points += [(t, y)]
		k1 = proc(t, y, f)
		y += h*k1
		t += h
	return points
	
def euler_inverso(t0, y0, h, n, f):
	"""
	Computes the Inverse Euler method.
	param t0  The initial t value to use in the numerical method.
	param y0  The initial y value to use in the numerical method.
	param h   The size of the step to use in this method.
	param n   The number of steps to perform.
	param f   The differential equation.
	
	return    The list of the computed values.
	"""
	## Define os pontos
	points = []
	t, y = t0, y0

	## Calcula os passos com o método de Euler
	for i in range(0, n):
		points += [(t, y)]
		k1 = proc(t + h, y + h*proc(t, y, f), f)
		y += h*k1
		t += h
	
	return points
	
def euler_aprimorado(t0, y0, h, n, f):
	"""
	Computes the Enhanced Euler method.
	param t0  The initial t value to use in the numerical method.
	param y0  The initial y value to use in the numerical method.
	param h   The size of the step to use in this method.
	param n   The number of steps to perform.
	param f   The differential equation.
	
	return    The list of the computed values.
	"""
	## Define os pontos
	points = []
	t, y = t0, y0

	## Calcula os passos com o método de Euler
	for i in range(0, n):
		points += [(t, y)]
		k1 = proc(t, y, f)
		k2 = proc(t + h, y + h*k1, f)
		y += h*(k1+k2)/2
		t += h
		
	return points
	
def runge_kutta(t0, y0, h, n, f):
	"""
	This method computes the aproximation of a differential equation based in the Runge-Kutta computational method.
	param t0 The initial point to start the numerical aproximation.
	param y0 The initial value of the function in the aproximation.
	param h  The step length for aproximation.
	param n  The number of steps to take in the aproximation.
	param f  The differential equation to aproximate.
	
	return   The set of points computed in the numerical aproximation.
	"""

	## Define os pontos
	points = []
	t, y = t0, y0

	## Calcula os passos com o método de Euler
	for i in range(0, n):
		points += [(t, y)]
		k1 = proc(t, y, f)
		k2 = proc(t + 0.5*h, y + 0.5*h*k1, f)
		k3 = proc(t + 0.5*h, y + 0.5*h*k2, f)
		k4 = proc(t + h, y + h*k3, f)
		y += h*(k1+2*k2+2*k3+k4)/6
		t += h
		
	return points
	
def adam_bashforth(y_set, t0, h, n, f, order):
	"""
	param y_set The set containing all the y values of the method in order. 
				This parameter goes from n-k untill n in the array, means y_set[0] = y_{n-k}.
	param t0    The t value from the first step, it is the step n-k.
	param h     The step size.
	param n     Number of steps to use in the method.
	param f     The differential equation used.
	param order The order of the Adams Bashforth method. Goes from second order to the seventh order.
	
	return      The set of computed points.
	"""
	points = list(y_set)
	coeficients = [
		[3/2, -1/2],
		[23/12, -4/3, 5/12],
		[55/24, -59/24, 37/24, -3/8],
		[1901/720, -1387/360, 109/30, -637/360, 251/720],
		[4277/1440, -2641/480, 4991/720, -3649/720, 959/480, -95/288],
		[198721/60480, -18637/2520, 235183/20160, -10754/945, 135713/20160, -5603/2520, 19087/60480],
		[16083/4480, -1152169/120960, 242653/13440, 2102243/120960, -115747/13440, 32863/13440, -5257/17280]
	]
	
	if order < 2:
		raise("Order not supported")

	for j in range(0, n - order): 
		pt_set = list(reversed(points))
		total = 0
		for i in range(0, len(coeficients[order - 2])):
			total += coeficients[order - 2][i]*proc(t0 + h*(j+i), pt_set[i], f)
		val = pt_set[0] + h*total
		points.append(val)
	
	points = [(t0 + idx*h, y) for idx, y in enumerate(points)]
	
	return points
	
def adam_multon():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def adam_multon_by_euler():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def adam_multon_by_euler_inverso():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def adam_multon_by_euler_aprimorado():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def adam_multon_by_runge_kutta():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def formula_inversa():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def formula_inversa_by_euler():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def formula_inversa_by_euler_inverso():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def formula_inversa_by_euler_aprimorado():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points
	
def formula_inversa_by_runge_kutta():
	"""Summary
	
	Returns:
		TYPE: Description
	"""
	points = []
	return points



def detect_method(line):
	"""Summary
	
	Args:
		line (TYPE): Description
	"""
	method = line.split(" ")[0]
	route_method(method, line)
	pass

def route_method(line):
	"""
	Select the method to execute based in the name of the method
	
	Args:
		line (string): The original line containing the user data
	
	Returns:
		list: The list of the points
	"""
	points = []
	method = line.split(' ')[0]

	## Gen the string default from the line
	inputString = line.replace('\n', '').replace('\r', '')
	inputString = ' '.join(inputString.split(' ')[1:])

	if method == "euler":
		print("Metodo de Euler")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		print("y(", t0, ")")
		print("h =", h)
		points = euler(t0, y0, h, n + 1, f)

	elif method == "euler_inverso":
		print("Metodo de Euler Inverso")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		print("y(", t0, ")")
		print("h =", h)
		points = euler_inverso(t0, y0, h, n + 1, f)

	elif method == "euler_aprimorado":
		print("Metodo de Euler Aprimorado")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		print("y(", t0, ")")
		print("h =", h)
		points = euler_aprimorado(t0, y0, h, n + 1, f)

	elif method == "runge_kutta":
		print("Metodo de Runge-Kutta")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		print("y(", t0, ")")
		print("h =", h)
		points = runge_kutta(t0, y0, h, n + 1, f)

	elif method == "adam_bashforth":
		print("Metodo Adam-Bashforth")
		t0, h, n, f, order = inputString.split(" ")[-5:] ## The last five elements
		t0, h, n, order = float(t0), float(h), int(n), int(order)

		y_set = inputString.split(" ")[:-5]
		y_set = [float(a) for a in y_set]

		print("y(", t0, ")")
		print("h =", h)
		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_euler":
		print("Metodo Adam-Bashforth por Euler")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler(t0, y0, h, order, f)
		_, y_set = zip(*points)
		print(y_set)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_euler_inverso":
		print("Metodo Adam-Bashforth por Euler Inverso")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_inverso(t0, y0, h, order, f)
		_, y_set = zip(*points)
		print(y_set)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_euler_aprimorado":
		print("Metodo Adam-Bashforth por Euler Aprimorado")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_aprimorado(t0, y0, h, order, f)
		_, y_set = zip(*points)
		print(y_set)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_runge_kutta":
		print("Metodo Adam-Bashforth por Runge-Kutta")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = runge_kutta(t0, y0, h, order, f)
		_, y_set = zip(*points)
		print(y_set)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_multon":
		print("adam_multon")
		# points = adam_multon()

	elif method == "adam_multon_by_euler":
		print("adam_multon_by_euler")
		# points = adam_multon_by_euler()

	elif method == "adam_multon_by_euler_inverso":
		print("adam_multon_by_euler_inverso")
		# points = adam_multon_by_euler_inverso()

	elif method == "adam_multon_by_euler_aprimorado":
		print("adam_multon_by_euler_aprimorado")
		# points = adam_multon_by_euler_aprimorado()

	elif method == "adam_multon_by_runge_kutta":
		print("adam_multon_by_runge_kutta")
		# points = adam_multon_by_runge_kutta()

	elif method == "formula_inversa":
		print("formula_inversa")
		# points = formula_inversa()

	elif method == "formula_inversa_by_euler":
		print("formula_inversa_by_euler")
		# points = formula_inversa_by_euler()

	elif method == "formula_inversa_by_euler_inverso":
		print("formula_inversa_by_euler_inverso")
		# points = formula_inversa_by_euler_inverso()

	elif method == "formula_inversa_by_euler_aprimorado":
		print("formula_inversa_by_euler_aprimorado")
		# points = formula_inversa_by_euler_aprimorado()

	elif method == "formula_inversa_by_runge_kutta":
		print("formula_inversa_by_runge_kutta")
		# points = formula_inversa_by_runge_kutta()

	return points

def main():
	"""
	The main control and the default guide to the software
	"""
	fname = "entrada.txt"
	with open(fname, "r") as f:
		for line in f:
			## filter any multiple spaces
			line = ' '.join(line.split('  '))

			# Correct the problem from 4x -> 4*x
			# valstr = re.sub(r'([0-9])([a-z])', r'\1*\2', f) 
			points = route_method(line)
			print_points(points)


if __name__ == "__main__":
	main()
##################################################################################
# MIT License                                                                    #
#                                                                                #
# Copyright (c) 2018 Caio Gomes                                                  #
#                                                                                #
# Permission is hereby granted, free of charge, to any person obtaining a copy   #
# of this software and associated documentation files (the "Software"), to deal  #
# in the Software without restriction, including without limitation the rights   #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      #
# copies of the Software, and to permit persons to whom the Software is          #
# furnished to do so, subject to the following conditions:                       #
#                                                                                #
# The above copyright notice and this permission notice shall be included in all #
# copies or substantial portions of the Software.                                #
#                                                                                #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  #
# SOFTWARE.                                                                      #
##################################################################################
# That one is a software to compute differential equations  numerically throught #
# different methods.                                                             #
#                                                                                #
# Every single method returns a list of pairs (t_n, y_n)                         #
##################################################################################

#############################
## Import libs
#############################
import matplotlib.pyplot as plt
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

def plot_graph(points, f):
	"""Plot the graph with matplotlib
	
	Args:
	    points (list(float, float)): The list with points (t_n, y_n)
	    f (str): The string containing the function to be ploted
	"""
	t_axis, y_axis = zip(*points)
	# plt.pyplot.xlabel("t")
	# plt.pyplot.ylabel("f'(t) = " + f)
	# plt.pyplot.plot(t_axis, y_axis)
	plt.xlabel("t")
	plt.ylabel("f'(t) = " + f)
	plt.plot(t_axis, y_axis)
	plt.show()

def print_points(points, f):
	"""Plot the points of the graph
	
	Args:
	    points (list(float, float)): The list with points (t_n, y_n)
	    f (FILE): The file where you must print the points
	"""
	for idx, (t, y) in enumerate(points):
		# print(idx, y)
		log_write(str(idx) + " " + str(y))
	log_write("")

def log_write(string):
	"""
	Log in the terminal with a print and log the same data in a text file called 'saida.txt'
	
	Args:
	    string (str): The text to log
	"""
	print(string)
	with open("saida.txt", "a") as f:
		f.write(string + "\n")

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
	Computes the adams bashforth default method.
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

	constants = [5/12, -3/8, 251/720, -95/288, 19087/60480, -5257/17280, 1070017/3628800]
	
	if order < 1:
		raise ValueError("orders lower than 1 not supported in Adams Bashforth Method")

	elif order == 1:
		y0 = y_set[0]
		points = euler(t0, y0, h, n, f)

	else:
		for j in range(0, n - order):  # iterate untill the last point from prediction
			pt_set = list(reversed(points))
			total = 0
			i_limit = len(coeficients[order - 2]) - 1
			for i in range(0, len(coeficients[order - 2])):
				total += coeficients[order - 2][i]*proc(t0 + h*(j+ (i_limit - i)), pt_set[i], f)
			val = pt_set[0] + h*total
			# val -= constants[order - 2]*h
			points.append(val)
		
		points = [(t0 + idx*h, y) for idx, y in enumerate(points)]
	
	return points
	
def adam_multon(y_set, t0, h, n, f, order, function=None):
	"""
	Computes the adams multon default method.
	param y_set    The set containing all the y values of the method in order. 
				   This parameter goes from n-k untill n in the array, means y_set[0] = y_{n-k}.
	param t0       The t value from the first step, it is the step n-k.
	param h        The step size.
	param n        Number of steps to use in the method.
	param f        The differential equation used.
	param order    The order of the Adams Bashforth method. Goes from second order to the seventh order.
	param function The function to compute the next point to use as inference for the derivative computation.
	
	return      The set of computed points.
	"""
	points = list(y_set)

	coeficients = [
		[1/2, 1/2],
		[5/12, 2/3, -1/12],
		[3/8, 19/24, -5/24, 1/24],
		[251/720, 323/360, -11/30, 53/360, -19/720],
		[95/288, 1427/1440, -133/240, 241/720, -173/1440, 3/160],
		[19087/60480, 2713/2520, -15487/20160, 586/945, -6737/20160, 263/2520, -863/60480],
		[5257/17280, 139849/120960, -4511/4480, 123133/120960, -88547/120960, 1537/4480, -11351/120960, 275/24192]
	]

	constants = [-1/2, 1/24, -19/720, 3/160, -863/60480, 275/24192, 33953/3628800]

	if order < 1:
		raise ValueError("orders lower than 1 not supported in Adams Multon Method")

	elif order == 1:
		y0 = y_set[0]
		points = euler_inverso(t0, y0, h, n, f)

	else:
		for j in range(0, n - order + 1): # iterate untill the last point from prediction
			pt_set = list(reversed(points))
			total = 0

			i_limit = len(coeficients[order - 2]) - 1
			for i in range(0, len(coeficients[order - 2]) - 1):
				total += coeficients[order - 2][i + 1]*proc(t0 + h*(j+ (i_limit - i - 1)), pt_set[i], f)

			## get the next step
			mx = min(len(pt_set), 8)
			lst = list(reversed(pt_set[:mx]))
			t_val = t0 + h*(max(len(pt_set) - mx, 0))
			# n_set = adam_bashforth(lst, t_val, h, mx + 1, f, mx - 1)
			if function == None:
				n_set = euler_inverso(t0 + h*len(pt_set), pt_set[0], h, 2, f)
			else:
				n_set = function(t0 + h*len(pt_set), pt_set[0], h, 2, f)
			
			## retrive the predicted point
			_, y_val = n_set[-1]

			## Add the last point
			total += coeficients[order - 2][0]*proc(t0 + h*(j+i_limit), y_val, f) # them add the predicted point

			val = pt_set[0] + h*total
			# val += constants[order - 1]
			points.append(val)
		
		points = [(t0 + idx*h, y) for idx, y in enumerate(points)]

	return points
	
def formula_inversa(y_set, t0, h, n, f, order, function=None):
	"""
	Computes the adams multon default method.
	param y_set    The set containing all the y values of the method in order. 
				   This parameter goes from n-k untill n in the array, means y_set[0] = y_{n-k}.
	param t0       The t value from the first step, it is the step n-k.
	param h        The step size.
	param n        Number of steps to use in the method.
	param f        The differential equation used.
	param order    The order of the Adams Bashforth method. Goes from second order to the seventh order.
	param function The function to compute the next point to use as inference for the derivative computation.
	
	return      The set of computed points.
	"""
	points = list(y_set)

	coeficients = [
		[1, 1],
		[4/3, -1/3, 2/3],
		[18/11, -9/11, 2/11, 6/11],
		[48/25, -36/25, 16/25, -3/25, 12/25],
		[300/137, -300/137, 200/137, -75/137, 12/137, 60/137],
		[360/147, -450/147, 400/147, -225/147, 72/147, -10/147, 60/147]
	]

	for j in range(0, n - order + 1):
		pt_set = list(reversed(points))
		total = 0

		# computes the before points values
		for i in range(0, order - 1):
			total += pt_set[i]*coeficients[order - 1][i]

		# here we suppose the next stop from adams
		mn = min(8, len(pt_set))
		y_set = list(reversed(pt_set[:mn]))
		t_val = t0 + h*abs(len(y_set) - mn)
		# _, y_val = adam_bashforth(y_set, t_val, h, mn + 1, f, mn - 1)[-1]
		if function == None:
			_, y_val = runge_kutta(t0 + h*len(pt_set), pt_set[0], h, 2, f)[-1]
		else:
			_, y_val = function(t0 + h*len(pt_set), pt_set[0], h, 2, f)[-1]

		# The differential value computed
		other = h*coeficients[order - 1][-1]*proc(t0 + h*len(pt_set), y_val, f)

		val = total + other
		points.append(val)

	points = [(t0 + h*idx, y) for idx, y in enumerate(points)]

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
		# print("Metodo de Euler")
		log_write("Metodo de Euler")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)
		points = euler(t0, y0, h, n + 1, f)

	elif method == "euler_inverso":
		# print("Metodo de Euler Inverso")
		log_write("Metodo de Euler Inverso")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)
		points = euler_inverso(t0, y0, h, n + 1, f)

	elif method == "euler_aprimorado":
		# print("Metodo de Euler Aprimorado")
		log_write("Metodo de Euler Aprimorado")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)
		points = euler_aprimorado(t0, y0, h, n + 1, f)

	elif method == "runge_kutta":
		# print("Metodo de Runge-Kutta")
		log_write("Metodo de Runge-Kutta")
		y0, t0, h, n, f = inputString.split(" ")
		y0, t0, h, n = float(y0), float(t0), float(h), int(n)

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)
		points = runge_kutta(t0, y0, h, n + 1, f)

	elif method == "adam_bashforth":
		# print("Metodo Adam-Bashforth")
		log_write("Metodo Adam-Bashforth")
		t0, h, n, f, order = inputString.split(" ")[-5:] ## The last five elements
		t0, h, n, order = float(t0), float(h), int(n), int(order)

		y_set = inputString.split(" ")[:-5]
		y_set = [float(a) for a in y_set]

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_euler":
		# print("Metodo Adam-Bashforth por Euler")
		log_write("Metodo Adam-Bashforth por Euler")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler(t0, y0, h, order, f)
		_, y_set = zip(*points)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_euler_inverso":
		# print("Metodo Adam-Bashforth por Euler Inverso")
		log_write("Metodo Adam-Bashforth por Euler Inverso")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_inverso(t0, y0, h, order, f)
		_, y_set = zip(*points)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_euler_aprimorado":
		# print("Metodo Adam-Bashforth por Euler Aprimorado")
		log_write("Metodo Adam-Bashforth por Euler Aprimorado")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_aprimorado(t0, y0, h, order, f)
		_, y_set = zip(*points)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_bashforth_by_runge_kutta":
		# print("Metodo Adam-Bashforth por Runge-Kutta")
		log_write("Metodo Adam-Bashforth por Runge-Kutta")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = runge_kutta(t0, y0, h, order, f)
		_, y_set = zip(*points)

		points = adam_bashforth(y_set, t0, h, n + 1, f, order)

	elif method == "adam_multon":
		# print("Metodo Adam-Multon")
		log_write("Metodo Adam-Multon")
		t0, h, n, f, order = inputString.split(" ")[-5:] ## The last five elements
		t0, h, n, order = float(t0), float(h), int(n), int(order)

		y_set = inputString.split(" ")[:-5]
		y_set = [float(a) for a in y_set]

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)
		points = adam_multon(y_set, t0, h, n + 1, f, order)

	elif method == "adam_multon_by_euler":
		# print("Metodo Adam-Multon por Euler")
		log_write("Metodo Adam-Multon por Euler")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = adam_multon(y_set, t0, h, n + 1, f, order)

	elif method == "adam_multon_by_euler_inverso":
		# print("Metodo Adam-Multon por Euler Inverso")
		log_write("Metodo Adam-Multon por Euler Inverso")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_inverso(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = adam_multon(y_set, t0, h, n + 1, f, order)

	elif method == "adam_multon_by_euler_aprimorado":
		# print("Metodo Adam-Multon por Euler Aprimorado")
		log_write("Metodo Adam-Multon por Euler Aprimorado")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_aprimorado(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = adam_multon(y_set, t0, h, n + 1, f, order)

	elif method == "adam_multon_by_runge_kutta":
		# print("Metodo Adam-Multon por Runge-Kutta")
		log_write("Metodo Adam-Multon por Runge-Kutta")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = runge_kutta(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = adam_multon(y_set, t0, h, n + 1, f, order)

	elif method == "formula_inversa":
		# print("Metodo Formula Inversa")
		log_write("Metodo Formula Inversa")
		t0, h, n, f, order = inputString.split(" ")[-5:] ## The last five elements
		t0, h, n, order = float(t0), float(h), int(n), int(order)

		y_set = inputString.split(" ")[:-5]
		y_set = [float(a) for a in y_set]

		# print("y(", t0, ")")
		string = "y(" + str(t0) + ")"
		log_write(string)
		# print("h =", h)
		string = "h =" + str(h)
		log_write(string)
		points = formula_inversa(y_set, t0, h, n + 1, f, order)

	elif method == "formula_inversa_by_euler":
		# print("Metodo Formula Inversa por Euler")
		log_write("Metodo Formula Inversa por Euler")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = formula_inversa(y_set, t0, h, n + 1, f, order)

	elif method == "formula_inversa_by_euler_inverso":
		# print("Metodo Formula Inversa por Euler Inverso")
		log_write("Metodo Formula Inversa por Euler Inverso")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_inverso(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = formula_inversa(y_set, t0, h, n + 1, f, order)

	elif method == "formula_inversa_by_euler_aprimorado":
		# print("Metodo Formula Inversa por Euler Aprimorado")
		log_write("Metodo Formula Inversa por Euler Aprimorado")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = euler_aprimorado(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = formula_inversa(y_set, t0, h, n + 1, f, order)

	elif method == "formula_inversa_by_runge_kutta":
		# print("Metodo Formula Inversa por Runge-Kutta")
		log_write("Metodo Formula Inversa por Runge-Kutta")
		y0, t0, h, n, f, order = inputString.split(" ")
		y0, t0, h, n, order = float(y0), float(t0), float(h), int(n), int(order)

		points = runge_kutta(t0, y0, h, order - 1, f)
		_, y_set = zip(*points)

		points = formula_inversa(y_set, t0, h, n + 1, f, order)

	return points

def main():
	"""
	The main control and the default guide to the software
	"""
	# kill the output text file
	with open("saida.txt", "w") as f:
		f.write("")

	fname = "entrada.txt"
	with open(fname, "r") as f:
		for line in f:
			## filter any multiple spaces
			line = ' '.join(line.split('  '))

			# Correct the problem from 4x -> 4*x
			# valstr = re.sub(r'([0-9])([a-z])', r'\1*\2', f) 
			points = route_method(line)
			with open("saida.txt", "a") as f:
				print_points(points, f)


			inputString = line.replace('\n', '').replace('\r', '')
			inputString = ' '.join(inputString.split(' ')[1:])

			plot_graph(points, inputString.split(" ")[-1])


if __name__ == "__main__":
	main()
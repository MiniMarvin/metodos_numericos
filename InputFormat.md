# Input file format

### Euler
The example input is as follows:
```
euler y(0) t(0) h n f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t


### Backwards Euler
The example input is as follows:
```
euler_inverso y(0) t(0) h n f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Enhanced Euler
The example input is as follows:
```
euler_aprimorado y(0) t(0) h n f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t


### Runge-Kutta
The example input is as follows:
```
runge_kutta y(0) t(0) h n f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- f(t, y): The derivative of y in function of y and t

### Adam-Bashforth
The example input is as follows:
```
adam_bashforth y(0) y(1) y(2) ... y(n) t(0) h n f(t, y)
```
where:
- y(0) y(1) y(2) ... y(n): The n initial points of the y value to the method
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Multon
The example input is as follows:
```
adam_multon y(0) y(1) y(2) ... y(n) t(0) h n f(t, y)
```
where:
- y(0) y(1) y(2) ... y(n): The n initial points of the y value to the method
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Bashforth By Euler
This mode computs the Adam-Bashforth first points by euler. The example input is as follows:
```
adam_bashforth_by_euler y(0) t(0) h n f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Bashforth By Backwards Euler
This mode computs the Adam-Bashforth first points by euler. The example input is as follows:
```
adam_bashforth_by_euler_inverso y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Bashforth By Enhanced Euler
This mode computs the Adam-Bashforth first points by euler. The example input is as follows:
```
adam_bashforth_by_euler_aprimorado y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Bashforth By Runge-Kutta
This mode computs the Adam-Bashforth first points by Runge-Kutta. The example input is as follows:
```
adam_bashforth_by_runge_kutta y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Multon By Euler
This mode computs the Adam-Multon first points by euler. The example input is as follows:
```
adam_multon_by_euler y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Multon By Backwards Euler
This mode computs the Adam-Multon first points by backwards euler. The example input is as follows:
```
adam_multon_by_euler_inverso y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Multon By Enhanced Euler
This mode computs the Adam-Multon first points by enhanced euler. The example input is as follows:
```
adam_multon_by_euler_aprimorado y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

### Adam-Multon By Runge-Kutta
This mode computs the Adam-Multon first points by Runge-Kutta. The example input is as follows:
```
adam_multon_by_runge_kutta y(0) t(0) h f(t, y)
```
where:
- y(0): The initial y value of the function
- t(0): The initial t value of the function
- h: The size of the steps that the numerical method will use
- n: The number of steps that must be computed
- f(t, y): The derivative of y in function of y and t

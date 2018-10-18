# metodos_numericos
It's a repository to compute linear differential equations throught the following numerical methods
- Euler 
- Backwards Euler  
- Enhanced Euler  
- Runge-Kutta 
- Adams Bashforth
- Adams Multon

## Installing

This software is made to work in python3, the easiest way to work with this software is to setup with the following command:

```
chmod +x setup.sh
./setup.sh
```

Them to run just run the following command:
```
chmod +x start.sh
./start.sh
```


---
## Input File

This software works with a input file named _entrada.txt_ to run properly you must create a file with the following format:

```
euler 0 0 20 1-t+4*y
euler_inverso 0 0 0.1 20 1-t+4*y
euler_aprimorado 0 0 0.1 20 1-t+4*y
runge_kutta 0 0 0.1 20 1-t+4*y
adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 5
adam_bashforth_by_euler 0 0 0.1 20 1-t+4*y 6
adam_bashforth_by_euler_inverso 0 0 0.1 20 1-t+4*y 6
adam_bashforth_by_euler_aprimorado 0 0 0.1 20 1-t+4*y 6
adam_bashforth_by_runge_kutta 0 0 0.1 20 1-t+4*y 6
adam_multon 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 6
adam_multon_by_euler 0 0 0.1 20 1-t+4*y 6
adam_multon_by_euler_inverso 0 0 0.1 20 1-t+4*y 6
adam_multon_by_euler_aprimorado 0 0 0.1 20 1-t+4*y 6
adam_multon_by_runge_kutta 0 0 0.1 20 1-t+4*y 6
formula_inversa 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 6
formula_inversa_by_euler 0 0 0.1 20 1-t+4*y 6
formula_inversa_by_euler_inverso 0 0 0.1 20 1-t+4*y 6
formula_inversa_by_euler_aprimorado 0 0 0.1 20 1-t+4*y 6
formula_inversa_by_runge_kutta 0 0 0.1 20 1-t+4*y 6
```
Every single example has it's own code and the example contains all the allowed codes that may exists in the input file, every method follows the following input pattern described in [input format](InputFormat.md)

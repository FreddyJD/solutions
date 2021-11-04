"""
Fib sequence with memory outside of the function default
"""

memory = {}
def getNthFib(n):
	if n == 0:
		return 1
	if n == 1: 
		return 0
	if n in memory: 
		return memory[n]
	memory[n] = getNthFib(n - 1) + getNthFib(n - 2) 
	return memory[n] 

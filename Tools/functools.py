import functools

"""
@functools.cache
Simple lightweight unbounded function cache. Sometimes called “memoize”.

Returns the same as lru_cache(maxsize=None), creating a thin wrapper around
a dictionary lookup for the function arguments. Because it never needs to 
evict old values, this is smaller and faster than lru_cache() with a size 
limit.
"""

@functools.cache
def _factorial(n):
    if n == 1:
        return n
    else:
        return n * _factorial(n - 1)

print(_factorial(23))

"""

Decorator to wrap a function with a memoizing callable that saves up to 
the maxsize most recent calls. It can save time when an expensive or I/O
bound function is periodically called with the same arguments.
"""
@functools.lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

print(count_vowels("AeEiOUIou"))

"""
@singledispatch

It is a function decorator. It transforms a function into a generic 
function so that it can have different behaviors depending upon the 
type of its first argument. It is used for function overloading, 
the overloaded implementations are registered using the register()
attribute of the

"""

@functools.singledispatch
def fun(s):
    print(s)

@fun.register(int)
def _(s):
    print(s * 2)

fun('Test')
fun(10)
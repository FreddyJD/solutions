import collections

def parentheses_balance(n):
    if n == 0:
        yield ""
        return
    # 2
    for i in range(n):
        for y in parentheses_balance(i):
            for z in parentheses_balance(n - i - 1):
                yield '(' + y + ')' + z


def parentheses_counter(string): 
    return collections.Counter(string)


for parenthese in parentheses_balance(3): 
    print(parentheses_counter(parenthese))
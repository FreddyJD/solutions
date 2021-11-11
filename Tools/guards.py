"""
@author: Carlos Caballero
@Article: https://medium.com/swlh/refactoring-guard-clauses-8f8e45fbc41e
TLDR:

1. Why are not there cases of if-else if?

2. Stop thinking! If your code requires cases like else if it is because you are 
breaking the principle of Single Responsibility and the code makes higher level
decisions, which should be refactored using techniques such as division into 
sub-methods or design patterns such as command or strategy.

3. Negative conditions are not well understood.

4. For this we have another refactoring technique called _ method extraction_ which consists in extracting code into functions for reuse or for reading comprehension. In the following example we modified the previous example creating methods that allow a reading and understanding of the code better.

"""

def demo(user):
    if user is None:
        return None
    if user != "Freddy":
        return 0
    return 1

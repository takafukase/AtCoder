# import
from collections import deque

# input
S = input()

if __name__ == "__main__":

    stack = deque()
    for index, s in enumerate(S):
        if s == "(":
            stack.append(index+1)
        elif s == ")":
            print(stack.pop(), index+1)

# recursion at head and tail level


def head_recursion(n):
    if n == 0:
        return
    else:
        head_recursion(n-1)
    print n


head_recursion(10)


def tail_recursion(n):
    if n == 0:
        return
    else:
        print n
    tail_recursion(n-1)


tail_recursion(10)

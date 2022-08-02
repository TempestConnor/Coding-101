# n is the number of steps
# remind me to tell khuong wtf is going on
def staircase(n):
    if n == 2 or n == 1:
        return n
    prevPrev = 1
    prev = 2
    current = 0
    for step in range(3, n + 1):
        current = prev + prevPrev
        print(f"[@] current: {current}")
        prevPrev = prev
        print(f"[@] prevPrev: {prevPrev}")
        prev = current
        print(f"[@] prev: {prev}")
    return current


print(staircase(5))




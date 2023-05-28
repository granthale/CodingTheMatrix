import sys
sys.path.insert(0, '..')
from theField.plotting import plot

# Task 2.3.2
L = [[2,2], [3,2], [1.75,1], [2,1], [2.25,1], [2.5,1], [2.75,1], [3,1], [3.25,1]]
# plot(L,8)
# while True:
#     continue

# Quiz 2.4.2
# def add2(v, w):
#     return [v[0] + w[0], v[1] + w[1]]

# Task 2.4.3
# plot([add2(pt, [1,2]) for pt in L], 8)
# while True:
#     continue


# Quiz 2.4.4
def addn(v, w):
    if len(v) != len(w): return -999
    # return [(x+y) for (x,y) in zip(v,w)]
    return [v[i] + w[i] for i in range(len(v))]
# print(addn([1,1,1,1,1], [2,2,2,2,2]))

# Task 2.5.4

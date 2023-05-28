#Task 1.4.6-9
from plotting import plot
from math import e, pi

S = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
# plot(S,4)
# plot({1+2j+z for z in S})
# plot({.5j * z - 1j +2 for z in S})
# while True:
#     continue

# Task 1.4.10
from image import file2image

img = file2image("img01.png")
# if the intensity at img[y][x] < 120: add x + yi to the list
pts = [x + y*1j for y in range(len(img)) for x in range(len(img[0])) if img[y][x][0] < 120]
# plot(pts, 200)
# while True:
#     continue


# Task 1.4.11
# avg_real = sum(elem.real for elem in S) / len(S)
# avg_imag = sum(elem.imag for elem in S) / len(S)
# def f(z):
#     real = z.real - avg_real
#     imag = z.imag - avg_imag
#     return real + imag*1j

# new_S = {f(elem) for elem in S}
# plot(new_S)
# while True:
#     continue


# Task 1.4.12
# avg_real = sum(elem.real for elem in pts) / len(pts)
# avg_imag = sum(elem.imag for elem in pts) / len(pts)
# def f(z):
#     real = z.real - avg_real
#     imag = z.imag - avg_imag
#     return real + imag*1j

# new_pts = {f(elem) for elem in pts}
# plot(new_pts, 200)
# while True:
#     continue


# Task 1.4.17
# n = 20
# w = e**((2*pi*1j) / n)
# plot([w**i for i in range(n)])
# while True:
#     continue


# Task 1.4.18
# plot({pt * (e**(1j*(pi/4))) for pt in S})
# while True:
#     continue


# Task 1.4.19
# plot({pt * (e**(1j*(pi/4))) for pt in pts}, 200)
# while True:
#     continue

# Task 1.4.20
# avg_real = sum(elem.real for elem in pts) / len(pts)
# avg_imag = sum(elem.imag for elem in pts) / len(pts)
# def f(z):
#     real = z.real - avg_real
#     imag = z.imag - avg_imag
#     return real + imag*1j

# new_pts = {(.5 * f(elem))*(e**(1j*(pi/4))) for elem in pts}
# plot(new_pts, 200)
# while True:
#     continue


from GF2 import one

print(one * 0)
import math
import cmath
import re
def solve(a,b,c):
    delta = int(b)**2-4*int(a)*int(c)
    if delta >= 0:
        rst1 = (-int(b) + math.sqrt(delta)) / (2 * int(a))
        rst2 = (-int(b) - math.sqrt(delta)) / (2 * int(a))
    else:
        rst1 = (-int(b) + cmath.sqrt(delta)) / (2 * int(a))
        rst2 = (-int(b) - cmath.sqrt(delta)) / (2 * int(a))
    print(rst1,rst2)

while 1:
    print("pls input 3 numbers")
    a = input('请输入第一个数字：')
    while not re.findall('^[0-9]+$', a):
        a = input('输入只能是数字，请重新输入：')
    b = input('请输入第二个数字：')
    while not re.findall('^[0-9]+$', b):
        b = input('输入只能是数字，请重新输入：')
    c = input('请输入第三个数字：')
    while not re.findall('^[0-9]+$', c):
        c = input('输入只能是数字，请重新输入：')
    solve(a,b,c)

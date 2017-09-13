a = 1
def fun(a):
    print('func_in', id(a))
    a = 2
    print('re-point', id(a), id(2))

print('func_out', id(a), id(1))
fun(a)
print(a)

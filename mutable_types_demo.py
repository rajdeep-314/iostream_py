from mutable_types import *

# Demo
x = mutable_int(10)
print(x)
x.value = 20
print(10*x)
print()

y = mutable_str("abcd")
print(y + mutable_str("ef") + "gh")
y.value = "xyz"
print(2*y)
print()

z = mutable_float(10.2)
print(z/2)
z.value = 3.14
print(2*z)

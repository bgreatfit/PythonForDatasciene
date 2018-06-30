print()
x = 0
y = 0
try:
    z = x / y
except ZeroDivisionError:
    z = 0
# Or check before you do the division:

if y != 0:
    z = x / y
else:
    z = 0
# The latter can be reduced to:

z = (x / y) if y != 0 else 0
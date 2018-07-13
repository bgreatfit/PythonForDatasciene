import useful_func as uf
import math
with open('hello.txt') as f:
    file_data = f.read()
print(list(file_data))
num_list = [7, 8, 9, 7]
total = [n + 5 for n in num_list]
print(total)
print(math.__doc__)
#math.factorial()
print(__name__)
print(uf.__name__)
print(uf.sumlist(num_list))

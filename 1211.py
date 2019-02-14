# -*- coding: utf-8 -*-

# 输入打印
# s = input('input your birthday:')
# birthday = int(s)
# if birthday <20:
# 	print('hello',birthday)
# else:
# 	print('hi',birthday)

# 数据列表的使用
# list
list_a = [1, False, '123', [1, 2]]
# 添加
list_a.append(9)
print(list_a)
# 删除
list_a.pop()
print(list_a)
list_a.pop(0)
print(list_a)
# 修改
list_a[0] = True
print(list_a)
list_a.insert(1, 998)
print(list_a)
# 查询
print(list_a[1])

# tuple
tuple_a = ('司马光', '祖冲之', '魏延')
# 查询
print(tuple_a[0])

# 条件判断
age = 19
if age > 18:
    print('你已成年')

# 循环
for n in range(0, 10):
    if(n > 5):
        break
    print(n)

for n in range(0, 10):
    if(n % 2 == 0):
        continue
    print(n)

# 字典的使用
# dist
dist_a = {'a': 1, 'b': 2, 'c': 3}
# 添加
dist_a['d'] = 4
print(dist_a)
# 删除
dist_a.pop('d')
print(dist_a)
# 修改
dist_a['a'] = 9
print(dist_a)
# 查询
print(dist_a['c'])

# set
set_a = set([1, 2, 3, 'a'])
print(set_a)
# 添加
set_a.add(3)
set_a.add(4)
print(set_a)
# 删除
set_a.remove('a')
print(set_a)

# 函数
# 绝对值
print(abs(-99))

# 给函数设置别名
f = float
print(f("11.22"))

# 自定义函数


def my_abs(x):
    if not isinstance(x, (float, int)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
# my_abs('123d')

# 函数关键字参数


def person(name, age, **kw):
    if "city" in kw:
        print("city="+kw["city"])
    print({"name": name, "age": age, "other": kw})


# 函数调用
person("li", 12, gender="F", id="89757", city="dali")

# 递归函数


def fetch(x):
    if x == 1:
        return 1
    else:
        return x*fetch(x-1)


# 调用
print(fetch(5))


def fach(n):
    return fach_fach(n, 1)


def fach_fach(n, p):
    if n == 1:
        return p
    else:
        return fach_fach(n-1, n*p)


print(fach(5))


# 去除字符首尾空格
def trim(s):
    if s == "":
        return s
    if s[0] == " ":
        s = s[1:]
        return trim(s)
    if s[-1] == " ":
        s = s[:-1]
        return trim(s)
    return s

# 查找list中的最小和最大值


def findMinAndMax(L):
    if L == []:
        return (None, None)

    a = L[0]
    b = L[0]

    for n in L:
        if a > n:
            a = n
        if b < n:
            b = n

    return a, b


# 列表生成式
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)


#生成器 杨辉三角
def triangles():
	L = [1]
	while True:
		yield L
		L = [1] + [L[i - 1] + L[i] for i in range(1, len(L))] + [1]


for i,n in enumerate(triangles()):
	# if i == 10:
	# 	break
	print(n)

# a=['lisi','zhangs','sansi','woli']
a = ['lisi', 'zhangs', 'sansi', 'woli']
message = f"my first name {a[-1].title()}."
print(message)
a[0] = 'mingran'
print(a)
a.append('heng')
print(a)
a.insert(1, 'yan')
print(a)
del a[-1]
print(a)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
cars = ['bmw', 'audi', 'bens', 'sub']
cars.sort(reverse=True)
print(cars)
for i in range(10):
    for j in range(10):
        if i != j:
            k = 1000 * i + 100 * i + 10 * j + j
            for temp in range(31, 100):
                if temp * temp == k:
                    print("a:", k)


def solution(a, b, c, d):
    x = 1.5
    y = x
    f = a * y * y * y + b * y * y * +c * y + d
    fd = 3 * a * y * y + 2 * b * y + c
    h = f / fd
    x = y - h
    while abs(x - y) >= 1e-5:
        y = x
        f = a * y * y * y + b * y * y * +c * y + d
        fd = 3 * a * y * y + 2 * b * y + c
        h = f / fd
        x = y - h
        return x
    print("请输入方程的系数：")
    a, b, c, d = map(float, input().split())
    print("方程的参数为：", a, b, c, d)
    x = solution(a, b, c, d)
    print("所求方程的根为x=%.6fx")

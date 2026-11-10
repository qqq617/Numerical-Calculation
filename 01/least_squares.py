import math
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")

x = [1, 2, 3, 4]
y = [60, 30, 20, 15]

n = len(x)

Y = [math.log(value) for value in y]

sum_x = 0
sum_x2 = 0
sum_Y = 0
sum_xY = 0

for i in range(n):
    sum_x += x[i]
    sum_x2 += x[i] ** 2
    sum_Y += Y[i]
    sum_xY += x[i] * Y[i]

print(sum_x, sum_x2, sum_Y, sum_xY)

numerator = n * sum_xY - sum_x * sum_Y
denominator = n * sum_x2 - sum_x**2

b = numerator / denominator

A = (sum_Y - b * sum_x) / n

a = math.exp(A)


print("A =", A)
print("a =", a)
print("b =", b)


check1 = 0
check2 = 0

for i in range(n):
    residual = Y[i] - A - b * x[i]

    check1 += residual
    check2 += x[i] * residual

print("正规方程验证1:", check1)
print("正规方程验证2:", check2)

if abs(check1) < 1e-10 and abs(check2) < 1e-10:
    print("验证通过")
else:
    print("验证失败")

    
x_curve = [0.5 + i * 0.01 for i in range(401)]

y_curve = []

for xi in x_curve:
    yi = a * math.exp(b * xi)
    y_curve.append(yi)

plt.scatter(x, y, color="red", label="Original Data")

plt.plot(x_curve, y_curve, color="blue", label="Fitted Curve")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Exponential Least Squares Fitting")
plt.legend()
plt.grid(True)

plt.show()


def operate(a, b, x, y):
    x_prime = a * x + b * y
    y_prime = a * x - b * y
    return x_prime, y_prime


def main():
    print("欢迎使用本计算器！")
    while True:
        a = input("请输入a的值：")
        b = input("请输入b的值：")
        x = input("请输入x的值：")
        y = input("请输入y的值：")

        try:
            a = float(a)
            b = float(b)
            x = float(x)
            y = float(y)

            x_prime, y_prime = operate(a, b, x, y)
            print(f"运算结果：({x_prime}, {y_prime})")

            choice = input("按数字1键决定是否要再来一遍运算๑（按其他键退出）：")
            if choice != '1':
                break

        except ValueError:
            print("无法运算，请输入其他数值！")
            continue


if __name__ == "__main__":
    main()
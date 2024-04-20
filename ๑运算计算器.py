while True:
    print("欢迎使用本计算器！")
    a = float(input("请输入a的值: "))
    b = float(input("请输入b的值: "))
    x = float(input("请输入x的值: "))
    y = float(input("请输入y的值: "))

    try:
        x_prime = a * x + b * y
        y_prime = a * x - b * y
        print(f"经过运算后的结果是: ({x_prime}, {y_prime})")

        choice = input("是否要再来一遍运算? 按1继续, 其他键退出: ")
        if choice != "1":
            break
    except:
        print("无法运算,请输入其他数值!")
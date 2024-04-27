import time

def operate(a, b, x, y):
    x_prime = a * x + b * y
    y_prime = a * x - b * y
    return x_prime, y_prime

prompt_a = ""
prompt_b = ""
prompt_x = ""
prompt_y = ""
error_msg = ""
repeat_msg = ""
invalid_choice_msg = ""

def main():
    global prompt_a, prompt_b, prompt_x, prompt_y, error_msg, repeat_msg, invalid_choice_msg
    language = input("Please select language: Press 1 for English, Press 2 for Chinese(Entering another number will exit):")

    if language == "1":
        print("Welcome to this calculator!")
        prompt_a = "Please enter the value of a: "
        prompt_b = "Please enter the value of b: "
        prompt_x = "Please enter the value of x: "
        prompt_y = "Please enter the value of y: "
        error_msg = "Unable to perform calculation, please enter different values!"
        repeat_msg = "Press 1 to perform another calculation, or any other key to exit: "
        invalid_choice_msg = "Invalid language selection. Exiting in 3 seconds..."

    elif language == "2":
        print("欢迎使用本计算器！")
        prompt_a = "请输入a的值："
        prompt_b = "请输入b的值："
        prompt_x = "请输入x的值："
        prompt_y = "请输入y的值："
        error_msg = "无法运算，请输入其他数值！"
        repeat_msg = "按数字1键决定是否要再来一遍运算๑（按其他键退出）："
        invalid_choice_msg = "无效的语言选择。3秒后退出..."

    else:
        print(invalid_choice_msg)
        time.sleep(2)
        return

    while True:
        a = input(prompt_a)
        b = input(prompt_b)
        x = input(prompt_x)
        y = input(prompt_y)

        try:
            a = float(a)
            b = float(b)
            x = float(x)
            y = float(y)

            x_prime, y_prime = operate(a, b, x, y)
            print(f"Result: ({x_prime}, {y_prime})")

            choice = input(repeat_msg)
            if choice != '1':
                break

        except ValueError:
            print(error_msg)
            continue

if __name__ == "__main__":
    main()

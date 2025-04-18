import functions as _fs


# выбор уравнения и метода

def start():
    print("Введите номер уравнения:")
    for i in sorted(_fs.equations.keys()):
        print(f"\t{i}: {_fs.equations[i]['description']}")
    num = input()
    if num not in ["1", "2", "3", "4"]:
        raise ValueError("Недействительный номер уравнения!")
    eq_num = int(num)

    print("Введите номер метода:")
    print("1: Метод хорд")
    print("2: Метод простой итерации")
    print("3: Метод секущих")
    num = input()
    if num not in ["1", "2", "3"]:
        raise ValueError("Недействительный номер метода!")
    method_num = int(num)

    print("0 - клавиатура")
    print("1 - файл 'input.txt' (<a> <b> <epsilon> <mode_output>)")
    num = input("Выберите способ ввода данных: ")
    if num not in ["0", "1"]:
        raise ValueError("Недействительный способ ввода")
    input_mode = int(num)

    return eq_num, method_num, input_mode

def _read_keyboard():
    a = float(input("Введите левую границу 'a': "))
    b = float(input("Введите правую границу 'b': "))
    if a > b:
        raise ValueError("Недопустимые границы интервала!")

    eps = float(input("Введите epsilon: "))

    print("0 - консоль")
    print("1 - файл")
    mode_out = input("Выберите способ вывода: ")
    if mode_out not in ["0", "1"]:
        raise ValueError("Недействительный способ вывода")
    return a, b, eps, int(mode_out)


def _read_file():
    try:
        a, b, eps, mode_out = open("input.txt").readline().split()
    except ValueError:
        raise ValueError("Файл должен содержать a b epsilon mode_output")
    a, b, eps = map(float, (a, b, eps))
    if b <= a:
        raise ValueError("Недопустимые границы интервала!")
    if mode_out not in ["0", "1"]:
        raise ValueError("Недействительный способ вывода")
    return a, b, eps, int(mode_out)


def read(input_mode):
    """→ a, b, eps, output_mode"""
    return _read_keyboard() if input_mode == 0 else _read_file()


def write(root, f_val, iterations, output_mode):
    if output_mode == 0:
        print(f"Ответ: {root}, f({root})={f_val:.6f}, итераций: {iterations}")
    else:
        with open("output.txt", "w") as f:
            f.write(f"Ответ: {root}, f({root})={f_val:.6f}, итераций: {iterations}")

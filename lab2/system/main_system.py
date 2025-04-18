import math
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from newton import newton_system

def plot_system_with_solution(system, solution):
    x = np.linspace(-3, 3, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)

    F1 = np.vectorize(lambda x, y: system['functions'](x, y)[0])(X, Y)
    F2 = np.vectorize(lambda x, y: system['functions'](x, y)[1])(X, Y)

    fig, ax = plt.subplots(figsize=(7, 7))

    CS1 = ax.contour(X, Y, F1, levels=[0], colors='red', linewidths=1.5)
    ax.clabel(CS1, inline=True, fontsize=10, fmt='%1.1f', manual=[(-2, -1)])

    CS2 = ax.contour(X, Y, F2, levels=[0], colors='blue', linewidths=1.5)
    ax.clabel(CS2, inline=True, fontsize=10, fmt='%1.1f', manual=[(1, 1)])

    x_sol, y_sol = solution
    ax.plot(x_sol, y_sol, 'go', markersize=8, label='Solution')
    ax.legend()

    ax.set_title(f"Графики уравнений системы: {system['name']}")
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()

SYSTEMS = {
    1: {
        'name': 'Система 1: x² + y² = 2; x - y = 0',
        'functions': lambda x, y: (x ** 2 + y ** 2 - 2, x - y),
        'jacobian': lambda x, y: [[2 * x, 2 * y], [1, -1]]
    },
    2: {
        'name': 'Система 2: sin(x) + y = 2; x + cos(y) = 1',
        'functions': lambda x, y: (math.sin(x) + y - 2, x + math.cos(y) - 1),
        'jacobian': lambda x, y: [[math.cos(x), 1], [1, -math.sin(y)]]
    },
    3: {
        'name': 'Система 3: x³ - y = 0; x² + y² = 4',
        'functions': lambda x, y: (x ** 3 - y, x ** 2 + y ** 2 - 4),
        'jacobian': lambda x, y: [[3 * x ** 2, -1], [2 * x, 2 * y]]
    },
    4: {
        'name': 'Система 4: sin(y-1)+x=1.3; y-sin(x+1)=0.8',
        'functions': lambda x, y: (math.sin(y - 1) + x - 1.3, y - math.sin(x + 1) - 0.8),
        'jacobian': lambda x, y: [
            [1, math.cos(y - 1)],
            [-math.cos(x + 1), 1]
        ]
    }
}


def main():
    print("Доступные системы:")
    for key in SYSTEMS:
        print(f"{key}: {SYSTEMS[key]['name']}")

    while True:
        try:
            choice = int(input("Выберите систему (1/2/3/4): "))
            if choice in SYSTEMS:
                system = SYSTEMS[choice]
                break
            else:
                print("Введите число от 1 до 4")
        except ValueError:
            print("Некорректный ввод")

    while True:
        try:
            x0 = float(input("Введите начальное приближение x0: "))
            y0 = float(input("Введите начальное приближение y0: "))
            break
        except ValueError:
            print("Введите числовые значения")

    # метод Ньютона
    try:
        x_sol, y_sol, iters, errs = newton_system(system, x0, y0)

        print("\nРЕЗУЛЬТАТ:")
        print(f"Решение: x = {x_sol:.6f}, y = {y_sol:.6f}")
        print(f"Количество итераций: {iters}")
        print(f"Погрешности: {[f'{e:.2e}' for e in errs]}")

        f1, f2 = system['functions'](x_sol, y_sol)
        print("\nПроверка:")
        print(f"F1(x,y) = {f1:.2e}")
        print(f"F2(x,y) = {f2:.2e}")

    except Exception as e:
        print(f"\nОшибка: {str(e)}")
        return
    plot_system_with_solution(system, (x_sol, y_sol))


if __name__ == "__main__":
    main()
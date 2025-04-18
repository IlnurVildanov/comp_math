import numpy as np
import matplotlib.pyplot as plt

def secant_method(f, a, b, eps, max_iter=100, show=True):
    if show:
        _plot(f, a, b)

    x_prev, x_curr = a, b
    for k in range(1, max_iter + 1):
        f_prev, f_curr = f(x_prev), f(x_curr)
        if f_curr == f_prev:
            raise ZeroDivisionError("f(x_k) = f(x_{k-1}), деление на ноль.")

        x_next = x_curr - (x_curr - x_prev) / (f_curr - f_prev) * f_curr

        if abs(x_next - x_curr) <= eps or abs(f(x_next)) <= eps:
            return x_next, f(x_next), k

        x_prev, x_curr = x_curr, x_next

    raise RuntimeError("Секущие не сошлись за максимальное число итераций.")


def _plot(f, a, b, n=100):
    xs = np.linspace(a, b, n)
    ys = [f(x) for x in xs]
    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, label="f(x)")
    plt.axhline(0, color='k', lw=.5, ls='--')
    plt.title("Метод секущих – график функции")
    plt.grid(True)
    plt.legend()
    plt.show()

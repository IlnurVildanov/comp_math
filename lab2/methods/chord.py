import numpy as np
import matplotlib.pyplot as plt


def chord_method(f, a, b, tol, max_iter=100, show=True):
    if a > b:
        a, b = b, a

    if f(a) * f(b) > 0:
        raise ValueError("На интервале нет корня или их несколько.")

    if show:
        _plot(f, a, b)

    for k in range(1, max_iter + 1):
        fa, fb = f(a), f(b)
        x = a - (b - a) / (fb - fa) * fa   # формула хорды

        if abs(f(x)) < tol:
            return x, f(x), k

        # перестраиваем интервал
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    raise RuntimeError("Метод хорд не сошелся за максимальное число итераций.")


def _plot(f, a, b, n=100):
    xs = np.linspace(a, b, n)
    ys = [f(x) for x in xs]
    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, label="f(x)")
    plt.axhline(0, color='k', lw=.5, ls='--')
    plt.title("Метод хорд – график функции")
    plt.grid(True)
    plt.legend()
    plt.show()

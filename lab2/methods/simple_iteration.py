import numpy as np
import matplotlib.pyplot as plt


def simple_iteration_method(f, phi, phi_prime, a, b, eps, max_iter=100, show=True):
    if show:
        _plot(f, a, b)

    # достаточное условие сходимости: max phi'<1
    xs = np.linspace(a, b, 200)
    q = max(abs(phi_prime(x)) for x in xs)
    if q >= 1:
        raise ValueError(f"Сходимость не гарантирована: max|phi'| = {q:.3f}")

    x = (a + b) / 2          # начальное приближение
    for k in range(1, max_iter + 1):
        x_next = phi(x)
        if abs(x_next - x) < eps:
            return x_next, f(x_next), k
        x = x_next

    raise RuntimeError("Метод не сошелся за максимальное число итераций.")


def _plot(f, a, b, n=100):
    xs = np.linspace(a, b, n)
    ys = [f(x) for x in xs]
    plt.figure(figsize=(8, 6))
    plt.plot(xs, ys, label="f(x)")
    plt.axhline(0, color='k', lw=.5, ls='--')
    plt.title("Метод простой итерации – график функции")
    plt.grid(True)
    plt.legend()
    plt.show()

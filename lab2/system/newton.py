import math

def newton_system(system, x0, y0, eps=1e-6, max_iter=100, verbose=True):
    """
    Метод Ньютона для системы F(x,y)=0.
    → (x, y, iterations, errors)
    """
    f  = system['functions']
    J  = system['jacobian']
    xp, yp = x0, y0      # предыдущее приближение
    errors = []

    for k in range(1, max_iter + 1):
        f1, f2                   = f(xp, yp)
        (J11, J12), (J21, J22)   = J(xp, yp)
        det = J11 * J22 - J12 * J21
        if abs(det) < 1e-12:
            raise ValueError("det J ≈ 0 – метод оборвался")

        dx = (-f1 * J22 + f2 * J12) / det
        dy = (-J11 * f2 + f1 * J21) / det

        xn, yn = xp + dx, yp + dy
        err    = math.hypot(xn - xp, yn - yp)
        errors.append(err)

        if verbose:
            print(f"\nИтерация {k}:  x = {xn:.6f}, y = {yn:.6f},  err = {err:.2e}")

        if err < eps:
            return xn, yn, k, errors

        xp, yp = xn, yn

    raise RuntimeError("Метод Ньютона не сошелся за max_iter")

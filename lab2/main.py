import functions
import view as vw

from methods.chord import chord_method
from methods.simple_iteration import simple_iteration_method
from methods.secant import secant_method

# ввод
eq_num, meth_num, in_mode = vw.start()
a, b, eps, out_mode = vw.read(in_mode)

eq = functions.equations[eq_num]

# расчeт
if meth_num == 1:
    root, value, iters = chord_method(eq["f"], a, b, eps)
elif meth_num == 2:
    root, value, iters = simple_iteration_method(
        eq["f"], eq["phi"], eq["phi_prime"], a, b, eps)
else:
    root, value, iters = secant_method(eq["f"], a, b, eps)

# вывод
vw.write(root, value, iters, out_mode)

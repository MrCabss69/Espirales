# %% [markdown]
# ESTUDIO GEOMÉTRICO DE PARÁBOLAS

# %%
# IMPORTS
import numpy as np
import math
from math import log
import matplotlib.pyplot as plt

# %% [markdown]
# LOGARITMO EN ESPEJO

# %%
def log_fun(pendiente=0.1):

    # rango a plotear
    x = np.linspace(1,100,100)

    # calculamos la imagen
    y = [ log(xi)*pendiente for xi in x ]

    # ploteamos
    return x, np.array(y)

# %% [markdown]
# MATRIZ DE ROTACIÓN con theta grados:
# 
# 
# 
# $
# R(\theta) = \begin{pmatrix}
#                 cos(\theta) & -sen(\theta) \\
#                 sen(\theta) & cos(\theta)
#              \end{pmatrix}
# $

# %%
def R(theta,x,y):
    # rota el punto (x,y) en el eje cartesiano theta grados
    R = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    xx, yy = [], []
    for i in range(len(x)):
        newx, newy = np.dot( [x[i], y[i]], R )
        xx.append(newx)
        yy.append(newy)
    return np.array(xx), np.array(yy)

# %% [markdown]
# SIMETRÍAS EN 2D

# %%
def plot_simetrias(x,y):
    for i in [-1,1]:
        for j in [-1,1]:
            plt.plot(i*x,j*y)

# %% [markdown]
# PARÁBOLAS CUADRÁTICAS:
# 
# $ f(x) = ax² + bx + c $

# %%
def parabola_cuadratica(a, b, c, r=10):
    x = np.linspace(-r,r,100)
    y = [ a*(xx**2) + b*xx + c for xx in x]
    return x , np.array(y)

# %% [markdown]
# PARÁBOLAS N-ÉSIMAS - DADAS POR UN POLINOMIO DE ORDEN N para N > 2:
# 
# $  f(x) = a*x ^ {n-1} + b*x ^ {n-2} +.. + g $

# %%
def parabola_nesima(*kwargs):
    lista = list(kwargs)
    l, r = len(lista), 10
    x = np.linspace(-r,r,100)
    y = [sum([ lista[i]*(xx**(l-1-i)) for i in range(l-1)])+lista[-1] for xx in x ]
    return x, np.array(y)

# %% [markdown]
# SERIE DE FIBONACCI:
# 
# $ f(n) = f(n-1) + f(n-2) $

# %%
def fib(n=100):
    l = [1,1]
    while l[-1] < n:
        l.append(sum(l[-2:]))
    return l

# %% [markdown]
# ESPIRAL DE FIBONACCI:
# 
# "Aproximación de la espiral áurea generada dibujando arcos circulares conectando las esquinas opuestas de los cuadrados ajustados a los valores de la sucesión"

# %%
def fib_spiral(iters=10):
    f = fib()
    x = [ 1, 0, -1, 0 ] 
    y = [ 0, -1, 0, 1 ]
    rat, act = f[0] , (0,0)
    px, py   = [], []
    for i in range(iters):
        px.append(act[0])
        py.append(act[1])
        act = (act[0] + rat*x[i%4], act[1] + rat*y[i%4])
        rat = f[i+1]
    return np.array(px), np.array(py)

# %% [markdown]
# ESPIRAL ÁUREA:
# 
# Es una espiral logarítmica que tiene una razón de crecimiento o proporción equivalente al número áureo: $ \phi = 1.618 $

# %%
def golden_spiral(iters=10):
    x = [ 1, 0, -1, 0 ] 
    y = [ 0, -1, 0, 1 ]
    gold      = (1 + math.sqrt(5)) / 2 # phi, golden ratio
    rat, act  = 1 , (0,0)
    px, py    = []   , []
    for i in range(iters):
        px.append(act[0])
        py.append(act[1])
        act = (act[0] + rat*x[i%4], act[1] + rat*y[i%4])
        rat = gold * rat
    return np.array(px), np.array(py)

# %% [markdown]
# ECUACIÓN DE LA CIRCUNFERENCIA:
# 
# $
# r² = (x-{x_0})²+ (y-{y_0})²
# $

# %%
def ec_circunf(h1, h2, r):

    # ECUACIÓN DE LA CIRCUNFERENCIA: (x-h1)**2 + (y-h2)**2 = r**2 
    x = np.linspace(h1-r, h1+r, 100)
    y = [ math.sqrt( (r**2) - (xx-h1)**2 ) + h2 for xx in x ]
    return x, np.array(y)

# %% [markdown]
# 
# FUNCION PARA CREAR UN ARCO ENTRE 2 PUNTOS

# %%
def hanging_line(a, b, radio):

    # DIBUJAR UNA CURVA ENTRE DOS PUNTOS

    # alineados en eje x - tienen la misma altura
    if a[1] == b[1]:
        c1 , c2      = (a[0]+b[0])/2 , a[1]
        pts_x, pts_y = ec_circunf(c1, c2, radio)
    # alineados en eje y - tienen la misma posición
    else:
        c1 , c2       = a[0] , (a[1]+b[1])/2
        pts_x , pts_y = ec_circunf(c1, c2, radio)
        
    return pts_x, pts_y

# %% [markdown]
#     
# - TODO: 
# PENDIENTE CREAR CURVAS ENTRE LAS UNIONES DE LOS CAMBIOS DE CIRCUNFERENCIAS

# %% [markdown]
# REPRESENTACIÓN GRÁFICA DEL LOGARITMO Y SUS SIMETRÍAS

# %%
log_fun(100)
xp,yp = log_fun()
plot_simetrias(xp,yp)

# %% [markdown]
# REPRESENTACIÓN GRÁFICA DE PARÁBOLAS CUADRÁTICAS (polinimios de orden 2)

# %%
# DIBUJANDO PARÁBOLAS CUADRÁTICAS CONJUNTAS
for t in [(1, 0, -100),(1, 0, -50),(2, 0, -50)]:
    xp,yp = parabola_cuadratica(t[0],t[1],t[2])
    plot_simetrias(xp,yp)

# %% [markdown]
# REPRESENTACIÓN GRÁFICA DE PARÁBOLAS N-ÉSIMAS (polinomios de cualquier grado)

# %%
# POLINOMIOS DE GRADO SUPERIOR
px, py = parabola_nesima(1, 0, 1, 0)

# rotamos la parábola
pxr, pyr = R(math.pi/200,px,py)

# ploteamos las simetrías
plot_simetrias(px, py)
plot_simetrias(pxr, py)

# %% [markdown]
# APLICANDO LA ROTACIÓN DE UNA FUNCIÓN CON LA MATRIZ DE GIRO

# %%
# para la parabola original anterior: f(x) = x³ + x
angulo   = math.pi / 2     # 90º

# rotamos la parábola 90 grados
xxp, yyp = R(angulo,xp,yp)

# ploteamos los resultados
plot_simetrias(xp,yp)
plot_simetrias(xxp,yyp)
plt.show()

# %% [markdown]
# ESPIRAL DE FIBONACCI:

# %%
fib_x, fib_y  = fib_spiral()
plt.plot(fib_x,fib_y)
plt.show()

# %% [markdown]
# CON TODAS SIMETRÍAS

# %%
plot_simetrias(fib_x,fib_y)
plt.show()

# %% [markdown]
# ESPIRAL ÁUREA

# %%
gold_x, gold_y = golden_spiral()
plt.plot(gold_x,gold_y)
plt.show()

# %% [markdown]
# CON TODAS LAS SIMETRÍAS

# %%
plot_simetrias(gold_x,gold_y)
plt.show()

# %% [markdown]
# COMPARACIÓN ESPIRAL DE FIBONACCI VS ESPIRAL ÁUREA:

# %%
import matplotlib.pyplot as plt

fx,fy = fib_spiral()
gx,gy = golden_spiral()
plt.plot(fx,fy,'r', label='Fibonacci')
plt.plot(gx,gy,'g', label='Golden')
plt.legend()
plt.grid()
plt.show()


# %% [markdown]
# COMPARACIÓN DE SIMETRÍAS DE AMBAS ESPIRALES

# %%
fx,fy = fib_spiral()
gx,gy = golden_spiral()
plot_simetrias(fx,fy)
plot_simetrias(gx,gy)
plt.grid()
plt.show()
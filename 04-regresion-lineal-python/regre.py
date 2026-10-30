"""Funciones para realizar una regresión lineal"""

x = [20, 25, 30, 35, 40]
y = [50, 58, 65, 75, 82]


# f0
def media(x):
    """
    Qué hace:
        Calcula la media aritmética de una lista de números.

    Parámetros:
        x (list): Lista de números que se van a promediar.

    Retorno:
        float: Media aritmética de los valores de x.
    """
    return sum(x) / len(x)


# f1
def diferencia_cuadrado(x):
    """
    Qué hace:
        Calcula la suma de las diferencias al cuadrado
        entre cada valor de x y su media.

    Parámetros:
        x (list): Lista de valores numéricos.

    Retorno:
        float: Suma de las diferencias al cuadrado.
    """
    la_media = media(x)
    la_diferencia = 0

    for i in x:
        la_diferencia = la_diferencia + (i - la_media) * (i - la_media)

    return la_diferencia


# f2
def diferencia_xy(x, y):
    """
    Qué hace:
        Calcula la suma de los productos de las diferencias
        de cada par de valores de x e y respecto a sus medias.

    Parámetros:
        x (list): Valores de la variable independiente.
        y (list): Valores de la variable dependiente,
            correspondientes a los valores de x.

    Retorno:
        float: Suma de los productos de las diferencias.
    """
    mediax = media(x)
    mediay = media(y)
    lista_xy = [(a - mediax) * (b - mediay) for a, b in zip(x, y)]
    sumatoria = sum(lista_xy)

    return sumatoria


# f3
def obtener_b1(x, y):
    """
    Qué hace:
        Calcula la pendiente de la recta de regresión,
        que indica cuánto cambia y por cada unidad de x.

    Parámetros:
        x (list): Valores de la variable independiente.
        y (list): Valores de la variable dependiente,
            correspondientes a los valores de x.

    Retorno:
        float: Pendiente b1 de la recta de regresión.
    """
    diferencia = diferencia_xy(x, y)
    diferencia_cuadrados = diferencia_cuadrado(x)

    return diferencia / diferencia_cuadrados


# f4
def obtener_b0(x, y):
    """
    Qué hace:
        Calcula el intercepto de la recta de regresión,
        que representa el valor estimado de y cuando x vale cero.

    Parámetros:
        x (list): Valores de la variable independiente.
        y (list): Valores de la variable dependiente,
            correspondientes a los valores de x.

    Retorno:
        float: Intercepto b0 de la recta de regresión.
    """
    mediay = media(y)
    mediax = media(x)
    b1 = obtener_b1(x, y)

    return mediay - (b1 * mediax)


# f5
def obtener_y(x, y, valor_x):
    """
    Qué hace:
        Estima un valor de y mediante la ecuación
        de regresión lineal: y = b0 + b1 * valor_x.

    Parámetros:
        x (list): Valores de la variable independiente.
        y (list): Valores de la variable dependiente,
            correspondientes a los valores de x.
        valor_x (int o float): Valor de x para el que
            se desea estimar y.

    Retorno:
        float: Valor estimado de y para valor_x.
    """
    b0 = obtener_b0(x, y)
    b1 = obtener_b1(x, y)

    return b0 + (b1 * valor_x)

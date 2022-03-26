import math
from math import sin, cos, sqrt


def degrees_to_radians(a, b, c: float) -> float:
    return (a + b / 60 + c / 3600) * math.pi / 180


def golovan_values():
    # g = 9.828146316778
    # lam = 2.153878062299
    # phi = 1.561628713887
    lam = degrees_to_radians(123, 24, 29.2412)
    phi = degrees_to_radians(89, 28, 29.0441)
    print("lam=", lam, ";phi=", phi)
    h = 1252.253000
    mu = 398600.44 * 10 ** (9)
    a = 6378136.0
    u = 7.2921157 * 10 ** (-5)
    e2 = 6.69436619 * 10 ** (-3)
    w02 = 1.543 * 10 ** (-6)
    gfh = 9.78030 * (1 + 0.005302 * sin(phi) ** 2 - 0.000007 * sin(2 * phi) ** 2) - 0.00014 - 2 * w02 * h
    print("gfh=", gfh)
    Re = a / math.sqrt(1 - e2 * sin(phi) * sin(phi))
    print("Re=", Re)
    gn1gelm = -gfh * cos(lam) * cos(phi)
    gn2gelm = -gfh * sin(lam) * cos(phi)
    gn3gelm = -gfh * sin(phi)
    print("gn1gelm=", gn1gelm, ";gn2gelm=", gn2gelm, ";gn3gelm=", gn3gelm)
    ###################
    n1 = (Re + h) * cos(phi) * cos(lam)
    n2 = (Re + h) * cos(phi) * sin(lam)
    n3 = (Re + h) * sin(phi) - Re * e2 * sin(phi)
    print("n1=", n1, ";n2=", n2, ";n3=", n3)
    C20 = - 1082.6257 * 10 ** (-6)
    r = sqrt(n1 ** 2 + n2 ** 2 + n3 ** 2)
    g0n1 = -(mu / r ** 3) * (1 + 1.5 * C20 * (a / r) ** 2 * (5 * (n3 / r) ** 2 - 1)) * n1
    g0n2 = -(mu / r ** 3) * (1 + 1.5 * C20 * (a / r) ** 2 * (5 * (n3 / r) ** 2 - 1)) * n2
    g0n3 = -(mu / r ** 3) * (1 + 1.5 * C20 * (a / r) ** 2 * (5 * (n3 / r) ** 2 - 3)) * n3
    print("g0n1=", g0n1, ";g0n2=", g0n2, ";g0n3=", g0n3)
    gn1glon = g0n1 + u * u * n1
    gn2glon = g0n2 + u * u * n2
    gn3glon = g0n3
    print("gn1glon=", gn1glon, ";gn2glon=", gn2glon, ";gn3glon=", gn3glon)
    print(f'gn1gelm-gn1glon={(gn1gelm - gn1glon):1.8f}; gn2gelm-gn2glon={(gn2gelm - gn2glon):1.8f}; gn3gelm-gn3glon={(gn3gelm - gn3glon):1.8f}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # run_calman()
    golovan_values()

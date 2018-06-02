__author__ = 'ryuz6l'
from operator import mod


def crt(ms, aas):
    """
    Chinese Remainder Theorem:
    ms = list of pairwise relatively prime integers
    as = remainders when x is divided by ms
    (ai is 'each in as', mi 'each in ms')

    The solution for x modulo M (M = product of ms) will be:
    x = a1*M1*y1 + a2*M2*y2 + ... + ar*Mr*yr (mod M),
    where Mi = M/mi and yi = (Mi)^-1 (mod mi) for 1 <= i <= r.
    """

    M = reduce(mul, ms)        # multiply ms together
    Ms = [M/mi for mi in ms]   # list of all M/mi
    ys = [inverse(Mi, mi) for Mi,mi in zip(Ms,ms)] # uses inverse,eea
    return reduce(add,[ai*Mi*yi for ai,Mi,yi in zip(aas,Ms,ys)]) % M

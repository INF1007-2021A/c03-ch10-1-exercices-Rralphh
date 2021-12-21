#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    list=[]
    for c in cartesian_coordinates:
        a=(np.sqrt(c[0] ** 2 + c[1] ** 2), np.arctan2(c[1], c[0]))
        list.append(a)
        c=np.array(list)
    return c


def find_closest_index(values: np.ndarray, number: float) -> int:
    values=values-number
    print(values)
    b=np.abs(values)
    return b.argmin()

print(find_closest_index(np.array(([1,2,3],[4,5,6],[7,8,9])),2))
#print(coordinate_conversion(np.array([(0, 0), (10, 10), (2, -1)])))
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass

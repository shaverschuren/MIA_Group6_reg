

import numpy as np
import matplotlib.pyplot as plt
import registration as reg
import registration_util as util
from IPython.display import display, clear_output

def pbr(X,Xm):
    if len(X)==2:
        print('x must be larger than 1')
        return
    X=util.c2h(X)
    Xm=util.c2h(Xm)
    T=reg.ls_affine(X,Xm)
    return X


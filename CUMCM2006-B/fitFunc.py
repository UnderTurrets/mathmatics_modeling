'''
Created by Han Xu
email:736946693@qq.com
'''
from goodness_of_fit import goodness_of_fit
import numpy as np

'''
@:x_sequence np.array
@:y_sequence np.array
@:order int
@:return np.array
'''
def fit_with_numpy(x_sequence,y_sequence,order):
    # fit with numpy
    z1 = np.polyfit(x_sequence, y_sequence, order)

    # show the function
    p1 = np.poly1d(z1)
    print(p1)

    # get predicted values

    y_pred= p1(x_sequence)

    # show the goodness of fit
    rr = goodness_of_fit(y_pred, y_sequence)
    print(rr)
    return p1
'''
Created by Han Xu
email:736946693@qq.com
'''
#%% The file is used to compute the goodness of fit.


def __sst(y_origin):
    """
    compute SST(total sum of squares)
    @:param y_no_predicted: List[int] or array[int]
    @:return: SST
    """
    y_mean = sum(y_origin) / len(y_origin)
    s_list =[(y - y_mean) ** 2 for y in y_origin]
    sst = sum(s_list)
    return sst



def __ssr(y_fit, y_origin):
    """
    compute SSR(regression sum of squares)
    @:param y_fit: List[int] or array[int]
    @:param y_origin: List[int] or array[int]
    @:return: SSR
    """
    y_mean = sum(y_origin) / len(y_origin)
    s_list =[(y - y_mean) ** 2 for y in y_fit]
    ssr = sum(s_list)
    return ssr



def __sse(y_fit, y_origin):
    """
    compute SSE(error sum of squares)
    @:param y_fit: List[int] or array[int]
    @:param y_origin: List[int] or array[int]
    @:return: SSE
    """
    s_list = [(y_fit[i] - y_origin[i]) ** 2 for i in range(len(y_fit))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fit, y_origin):
    """
    compute the goodness of fit.R^2
    :param y_fit: List[int] or array[int]
    :param y_origin: List[int] or array[int]
    :return: R^2
    """
    SSR = __ssr(y_fit, y_origin)
    SST = __sst(y_origin)
    rr = SSR /SST
    return rr
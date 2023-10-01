'''
Created by Han Xu
email:736946693@qq.com
'''
import numpy as np

'''
separate X-ordinate from the set of Points
@:points_sequence vector<Point>
'''
def separateX_PointSet(points_sequence):
    x=[singlePoint[0] for singlePoint in points_sequence]
    return np.array(x)

'''
separate Y-ordinate from the set of Points
@:points_sequence vector<Point>
'''
def separateY_PointSet(points_sequence):
    y=[singlePoint[1] for singlePoint in points_sequence]
    return np.array(y)

'''
get(1,1),(1,2),(1,3),(1,4),return (1,2.5)
@:sameX_pointSet vector<Point>
@:return Point
'''
def get_mean(points_sequence):
    if(len(points_sequence)>0):
        sum_x = 0;sum_y = 0
        for single_point in points_sequence:
            sum_x += single_point[0]
            sum_y += single_point[1]
        return [sum_x / len(points_sequence), sum_y / len(points_sequence)]
    else:return

'''
get(1,1),(1,2),(1,3),(1,4),return (1-2*offset,2.5),(1-1*offset,2.5),(1+1*offset,2.5),(1+2*offset,2.5)
@:sameX_pointSet vector<Point>
@:offset float
'''
def get_mean_mulXPoints(sameX_pointSet,offset=1e-6):
    ret=[]
    total_num=len(sameX_pointSet)
    average_point=get_mean(sameX_pointSet)
    x_origin=sameX_pointSet[0][0]
    x_sequence=np.linspace(x_origin-(total_num//2)*offset,x_origin+(total_num//2)*offset,num=total_num)
    for i in range(total_num):
        ret.append([x_sequence[i],average_point[1]])
    return ret

'''
assing the points who have the same X to the same group
@:point_total vector<Point>
@:return vector<vector<Point>>
'''
def group_points(point_total):
    lower = 0
    ret = []
    for i in range(1, len(point_total)):
        if (point_total[i - 1][0] != point_total[i][0]):
            vector_sameX_points = point_total[lower:i]
            # print(vector_sameX_points)
            ret.append(vector_sameX_points)
            lower = i

    vector_sameX_points = point_total[lower:]
    # print(vector_sameX_points)
    ret.append(vector_sameX_points)
    # print(ret)
    return ret

'''
get(0,0).(1,2),(2,3),(3,4),return (1,ln(2)),(2,ln(3)),(3,ln(4))
(0,0) has been thrown!
'''
import math
def get_ln(points_sequence):
    ret=[]
    for single_point in points_sequence:

        if(single_point[1]>0):

            single_point[1]=math.log(single_point[1])
            ret.append(single_point)

        else:
            continue
            # single_point[1] = math.log(single_point[1]+1)
    return ret

'''
Normlize the Y-axis value of points.Use Max-min method.
@:points_sequence vector<Point>
@:return vector<Point>
'''
def MaxMinNorm_PointY(points_sequence):
    y_origin = np.array([single_point[1] for single_point in points_sequence])
    _range = np.max(y_origin) - np.min(y_origin)
    y_norm=(y_origin - np.min(y_origin)) / _range
    for i in range(len(points_sequence)):
        points_sequence[i][1]=y_norm[i]
    return points_sequence

'''
Normlize the Y-axis value of points.Use Z-score method.
@:points_sequence vector<Point>
@:return vector<Point>
'''
def ZscoreNorm_PointY(points_sequence):
    y_origin = np.array([single_point[1] for single_point in points_sequence])
    mu = np.mean(y_origin, axis=0)
    sigma = np.std(y_origin, axis=0)
    y_norm=(y_origin - mu) / sigma
    for i in range(len(points_sequence)):
        points_sequence[i][1]=y_norm[i]
    return points_sequence

'''
Delete the max Y-axis value and the min Y-axis value of points_sequence.
@:points_sequence vector<Point>
@:return vector<Point>
'''
def throw_MaxAndMin(points_sequence):
    ret=[]
    y_origin = np.array([single_point[1] for single_point in points_sequence])
    y_max=np.max(y_origin).item()
    y_min=np.min(y_origin).item()
    # print("最大:{},最小{}".format(y_max,y_min))
    for singe_point in points_sequence:
        if (singe_point[1]!=y_max and singe_point[1]!=y_min):
            ret.append(singe_point)
    return ret

'''
get(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4)
return (1-2*offset,2.5),(1-1*offset,2.5),(1+1*offset,2.5),(1+2*offset,2.5),(2-2*offset,2.5),(2-1*offset,2.5),(2+1*offset,2.5),(2+2*offset,2.5)
'''
def process_PointSet_txt1(points_sequence):
    # print(len(points_sequence))
    points_sequence=throw_MaxAndMin(points_sequence)
    # print(len(points_sequence))
    # points_sequence = throw_MaxAndMin(points_sequence)
    # print(len(points_sequence))
    points_sequence=ZscoreNorm_PointY(points_sequence)
    grouped_points=group_points(points_sequence)
    ret = []
    for sameXpoint_list in grouped_points:
        for single_point in get_mean_mulXPoints(sameXpoint_list):
            ret.append(single_point)

    return ret


'''
get(0,3.1355),(0,3.0381),(7.5714,3.0445),(7.1429,4.1109)
return (0,3.0868),(7.35715,3.5777)
'''
def process_PointSet_txt2(points_sequence):
    time_0_PointSet = []
    time_7to9_PointSet = []
    time_15to17_PointSet = []
    time_23to25_PointSet = []
    time_31to33_PointSet = []
    time_38More_PointSet = []
    for single_point in points_sequence:
        if (single_point[0] == 0):
            time_0_PointSet.append(single_point)

        elif (single_point[0] >= 7 and single_point[0] <= 9):
            time_7to9_PointSet.append(single_point)

        elif (single_point[0] >= 15 and single_point[0] <= 17):
            time_15to17_PointSet.append(single_point)

        elif (single_point[0] >= 23  and single_point[0] <= 25 ):
            time_23to25_PointSet.append(single_point)

        elif (single_point[0] >= 31  and single_point[0] <= 33):
            time_31to33_PointSet.append(single_point)

        elif (single_point[0] >= 38  ):
            time_38More_PointSet.append(single_point)

    mean_PointSet=[get_mean(time_0_PointSet),get_mean(time_7to9_PointSet),get_mean(time_15to17_PointSet),get_mean(time_23to25_PointSet),get_mean(time_31to33_PointSet),get_mean(time_38More_PointSet)]
    mean_PointSet=[single_point for single_point in mean_PointSet if single_point is not None]
    ret=[]

    for i in range(1,len(mean_PointSet)):
        ret.append([mean_PointSet[i][0],mean_PointSet[i][1]-mean_PointSet[i-1][1]])
    return ret
    # return ZscoreNorm_PointY(ret)



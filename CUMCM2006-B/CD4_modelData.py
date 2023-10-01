'''
Created by Han Xu
email:736946693@qq.com
'''
import dataProcessing
from repairData import repaired_total
point_total=[]
for individual in repaired_total:
    for stage_data in individual["data"]:
        if (stage_data["CD4Date"]!=-1):
            point_total.append([stage_data["CD4Date"],stage_data["CD4Count"]])
        else:
            continue

point_total.sort()

# print(point_total)

final_points=dataProcessing.process_PointSet_txt1(point_total)
# print(final_points)


# final_points=dataProcessing.get_ln(final_points)
# final_points=dataProcessing.throw_MaxAndMin(final_points)
# final_points=dataProcessing.MaxMinNorm_PointY(final_points)
# print(final_points)

# final_points=dataProcessing.ZscoreNorm_PointY(final_points)


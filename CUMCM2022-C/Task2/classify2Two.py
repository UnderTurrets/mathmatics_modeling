import classify2Four
import pandas as pd
import numpy as np
Al_glass=pd.concat([classify2Four.Al_weathering_simples,classify2Four.Al_noWeathering_simples])
Al_glass_data=Al_glass.to_numpy()
Al_glass_mean=np.mean(a=Al_glass_data,axis=0)
# print(Al_glass)

highK_glass=pd.concat([classify2Four.highK_weathering_simples,classify2Four.highK_noWeathering_simples])
highK_glass_data=highK_glass.to_numpy()
highK_glass_mean=np.mean(a=highK_glass_data,axis=0)
# print(highK_glass_mean)
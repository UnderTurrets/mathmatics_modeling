#将附件二中的样本分为四类，高钾无风化,高钾风化,铅钡无风化,铅钡风化
import Task1.processSheet2
import numpy as np
#高钾无风化文物编号：01,03,04,05,06,13,14,15,16,17,18,21
highK_noWeathering_simples=Task1.processSheet2.excel_df.loc[['01','03部位1','03部位2','04','05','06部位1','06部位2','13','14','15','16','17','18','21']]
highK_noWeathering_data=highK_noWeathering_simples.to_numpy()
highK_noWeathering_mean=np.mean(a=highK_noWeathering_data,axis=0)
highK_noWeathering_std=np.std(a=highK_noWeathering_data,axis=0)
# print(highK_noWeathering_simples)




#高钾风化文物编号：07,09,10,12,22,27
highK_weathering_simples=Task1.processSheet2.excel_df.loc[['07','09','10','12','22','27']]
highK_weathering_data=highK_weathering_simples.to_numpy()
highK_weathering_mean=np.mean(a=highK_weathering_data,axis=0)
highK_weathering_std=np.std(a=highK_weathering_data,axis=0)



#铅钡无风化文物编号：20,24,30,31,32,33,35,37,45,46,47,55
Al_noWeathering_simples=Task1.processSheet2.excel_df.loc[['20','24','30部位1','30部位2','31','32','33','35','37','45','46','47','55']]
Al_noWeathering_data=Al_noWeathering_simples.to_numpy()
Al_noWeathering_mean=np.mean(a=Al_noWeathering_data,axis=0)
Al_noWeathering_std=np.std(a=Al_noWeathering_data,axis=0)


#铅钡风化文物编号：02,08,11,19,23,25,26,28,29,34,36,38,39,40,41,42,43,44,48,49,50,51,52,53,54,56,57,58
Al_weathering_simples=Task1.processSheet2.excel_df.loc[['02','08','08严重风化点','11','19','23未风化点','25未风化点','26','26严重风化点','28未风化点',
                                                        '29未风化点','34','36','38','39','40','41','42未风化点1','42未风化点2','43部位1','43部位2','44未风化点',
                                                        '48','49','49未风化点','50','50未风化点','51部位1','51部位2','52','53未风化点','54','54严重风化点','56','57','58']]
Al_weathering_data=Al_weathering_simples.to_numpy()
Al_weathering_mean=np.mean(a=Al_weathering_data,axis=0)
Al_weathering_std=np.std(a=Al_weathering_data,axis=0)
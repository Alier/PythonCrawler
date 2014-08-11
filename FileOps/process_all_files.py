import insert_feature
import sys
import os

directory = sys.argv[1]
#inputfile = sys.argv[1]

for file in os.listdir(directory):
    if file.endswith(".eds"):
        print file

#insert_feature.insert_ethlnk_param(inputfile,'317','319','sample_files/ethlnk_Param_319.txt')
#insert_feature.insert_ethlnk_param(inputfile+'_ethParam','319','320','sample_files/ethlnk_Param_320.txt')
#insert_feature.insert_global_feature(inputfile+'_ethParam_ethParam','31205','sample_files/param_31206_31213.txt',True)
#insert_feature.insert_global_feature(inputfile+'_ethParam_ethParam_param','31012','sample_files/assem_31013_31014.txt',False)

#insert_feature.insert_ethlnk_assem(inputfile,'006','007','ethlnk_Assem_007.txt')

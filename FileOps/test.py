import insert_feature
import sys

#t = insert_feature.get_first_digits('orig_file.txt','317')
#print t
#print insert_feature.get_intfNames('orig_file.txt',t,'317'):q

#print insert_feature.generate_section('ethlnk_320_IPDTNumDevices.txt','5317','05','Fa1/5')

#insert_feature.insert_ethlnk_feature.'orig_file.txt','317','319','ethlnk_319_IPDTMax.txt')


#insert_feature.insert_ethlnk_feature.'orig_file2.txt','319','320','ethlnk_320_IPDTNumDevices.txt')

#insert_feature.insert_global_feature('orig_file2.txt','17319','param_31206_31213_IPDT_LICENSE.txt',True)
#insert_feature.insert_global_feature('orig_file.txt_new','31014','assem_31013_31014_IPDT_LICENSE.txt',False)
#insert_feature.insert_global_feature('orig_file.txt','17317','assem_31013_31014_IPDT_LICENSE.txt',False)

inputfile = sys.argv[1]

#insert_feature.insert_ethlnk_feature(inputfile,'317','319','ethlnk_319_IPDTMax.txt')
#insert_feature.insert_ethlnk_feature(inputfile+'_eth','319','320','ethlnk_320_IPDTNumDevices.txt')
#insert_feature.insert_global_feature(inputfile+'_eth_eth','31205','param_31206_31213_IPDT_LICENSE.txt',True)

insert_feature.insert_ethlnk_assem(inputfile,'006','007','ethlnk_Assem_007.txt')

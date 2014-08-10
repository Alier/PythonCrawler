
#parameter starting digit mapping to interface number
def get_intfNum(firstDigit):
	val = hex(firstDigit).split('x')[1]
	if(firstDigit < 16):
		return ("0"+val).upper()
	else:
		return val.upper()

#print get_intfNum(4)

#!!!!!INCOMPLETE !!!!! mapping between SKU and interface map it should use
sku_to_intfmap = {"1783-BMS10"}

#!!!!!INCOMPLETE !!!!! interface number to interface string mapping.

intf_map_6 = {"01":"Fa1/1","02":"Fa1/2","03":"Fa1/3","04":"Fa1/4","05":"Fa1/5","06":"Fa1/6","1B":"SVI1"}

intf_map_6g = {"01":"Fa1/1","02":"Fa1/2","03":"Fa1/3","04":"Fa1/4","05":"Gi1/1","06":"Gi1/2","1B":"SVI1"}

intf_map_10 = {"01":"Fa1/1","02":"Fa1/2","03":"Fa1/3","04":"Fa1/4","05":"Fa1/5","06":"Fa1/6","07":"Fa1/7","08":"Fa1/8","09":"Fa1/9","0A":"Fa1/10","1B":"SVI1"}

intf_map_10g = {"01":"Fa1/1","02":"Fa1/2","03":"Fa1/3","04":"Fa1/4","05":"Fa1/5","06":"Fa1/6","07":"Fa1/7","08":"Fa1/8","09":"Gi1/1","0A":"Gi1/2","1B":"SVI1"}

intf_map_18 = {"01":"Fa1/1","02":"Fa1/2","03":"Fa1/3","04":"Fa1/4","05":"Fa1/5",
"06":"Fa1/6","07":"Fa1/7","08":"Fa1/8","09":"Fa1/9","0A":"Fa1/10","0B":"Fa1/11","0C":"Fa1/12","0D":"Fa1/13","0E":"Fa1/14","0F":"Fa1/15","10":"Fa1/16","13":"Gi1/1","14":"Gi1/2","1B":"SVI1"}

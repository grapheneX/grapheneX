from core.utils.helpers import get_modules_2
from core.utils.helpers import get_modules

#get_modules
a = get_modules_2()
#read_json_data()
obj = a['firewall']['Disable_File_Sharing']
print(dir(obj))
obj.execute_command()
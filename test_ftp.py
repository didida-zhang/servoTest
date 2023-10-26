'''
	
查询控制器FTP目录
'''
# import sys
# import jkrc
# import time

# robot = jkrc.RC("192.168.164.183")#VMmodel
# robot.login()
# dir= "/program/"
# robot.init_ftp_client()
# result = robot.get_ftp_dir("/program/", 0)
# # print(result)
# robot.close_ftp_client()
# robot.logout()
'''
下载FTP文件
'''


import sys
import jkrc
import time

robot = jkrc.RC("192.168.164.183")#VMmodel
robot.login()
remote = "/track/test/"
local= "C:\\Users\\JAKA\\Desktop\\jaka\\"
robot.init_ftp_client()
result = robot.download_file(local, remote, 2)
print(result)
robot.close_ftp_client()
robot.logout()




# import jkrc

# robot = jkrc.RC("172.30.1.153")#VMmodel
# robot.login()
# remote = "/program/"
# local= "C:\\Users\\JAKA\\Desktop\\jaka\\test"
# robot.init_ftp_client()
# result = robot.upload_file(local, remote, 2)
# print(result)
# robot.close_ftp_client()
# robot.logout()

# import sys
# import jkrc
# import time

# robot = jkrc.RC("172.30.1.153")#VMmodel
# robot.login()
# dir= "/program/"
# robot.init_ftp_client()
# result = robot.del_ftp_file("/program/", 2)
# print(result)
# robot.close_ftp_client()
# robot.logout()

# import sys
# import jkrc
# import time

# robot = jkrc.RC("172.30.1.153")#VMmodel
# robot.login()
# remote = "/lxxpro/"
# des = "renamedemo"
# robot.init_ftp_client()
# result = robot.rename_ftp_file(remote, des, 2)
# print(result)
# robot.close_ftp_client()
# robot.logout()

##############


###########
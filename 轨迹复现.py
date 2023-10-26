import jkrc
import time


demo = jkrc.RC("192.168.164.183")
demo.login()
demo.power_on()
# time.sleep(8)
demo.enable_robot()

ret = demo.get_exist_traj_file_name()
print(ret)

# demo.generate_traj_exe_file()
demo.program_load('track/test')
demo.program_run()

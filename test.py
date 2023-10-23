import socket
import jkrc
import time

demo = jkrc.RC("10.5.5.100")
demo.login()
demo.power_on()
demo.enable_robot()


with open("./data_1.0.csv",'r') as f:
    lines = f.readlines()

# demo.servo_speed_foresight(5,0.03)
# demo.servo_move_use_none_filter()

demo.servo_move_use_joint_LPF(0.5)
demo.servo_move_enable(True)
time.sleep(0.5)

for i in range(len(lines)):
    value = lines[i].split(' ')[0:6]  #每一列数据，列表
    #print(len(value))
    for num in range(6):
        value[num] = float(value[num])
    # demo.servo_j(value,0)
    demo.servo_j_extend(value,0,2)

demo.servo_move_enable(False)

demo.logout()

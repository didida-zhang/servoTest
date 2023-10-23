import jkrc
import time
from threading import Thread
robot = jkrc.RC("10.5.5.100")   #返回机器人对象
robot.login()               #登录

robot.power_on()            #上电
# time.sleep(8)
robot.enable_robot()        #上使能
# robot.servo_move_enable(True
PI = 3.1415926

i=0
while i<5:
        
    joint_pos=[PI/2,PI/3,-PI/3,PI/2,PI/2,0]
    robot.joint_move_extend(joint_pos, 0, False , 1 , 10 ,10)
    joint_pos_m = [154*PI/180,61*PI/180, -61*PI/180, 92*PI/180, PI/2, 36*PI/180]
    robot.joint_move_extend(joint_pos_m, 0, False, 1,10, 10 )
    joint_pos_m2 = [160*PI/180,80*PI/180, -90*PI/180, 120*PI/180, PI/2, 36*PI/180]
    robot.joint_move_extend(joint_pos_m2, 0, False, 1,10, 10 )
    joint_pos2 = [179*PI/180 , PI/2, -100*PI/180, 100*PI/180,PI/2, 28*PI/180]
    robot.joint_move_extend(joint_pos2, 0, False , 1 , 10 ,10)
    i+=1
# start = [286.352 , 187.586, 436.641,(170.626/180)*PI , (-3.078/180)*PI , (-89.492/180)*PI ]
# robot.linear_move()
# end = [389.552, 325.186, 434.641, (170.626/180)*PI , (-3.078/180)*PI , (-89.492/180)*PI]
# mid = [286.352, 187.586, 434.641, (170.626/180)*PI , (-3.078/180)*PI , (-89.492/180)*PI]
# robot.circular_move(end , mid, 0, False, 90, 200, 0)


# def listen_is_pos():
#     while True:
#         ret = robot.get_robot_status()
#         ret = ret[1][1]
#         print("is——pos:", ret)
#         time.sleep(0.1)
        

# t = Thread(target=listen_is_pos)
# t.start()


# while True:
#     ret = robot.get_robot_status()
#     print("=========",ret[1][21])
#     time.sleep(0.05)




# robot.joint_move(joint_pos,0,False,0.2)
# robot.set_digital_output(0,2,1)
# print(robot.get_robot_status())
# robot.program_load("hh")
# ret = robot.get_loaded_program()
# print(ret)
# robot.program_run()
# robot.get_analog_input(0,1)

# robot.set_rapidrate(1)
# robot.joint_move()

# robot.set_rapidrate(1)
# robot.set_tool_id(9)

# joint = robot.get_joint_position()
# print(joint)

# robot.jog(5, 0, 1, 5, 0.480724427)
# robot.jog(5, 0, 1, 5, -2.121877659)
# robot.jog(5, 0, 1, 5, -3.691763153)


# robot.jog(5, 0, 1, 5, 0.480724427)
# robot.jog(5, 0, 1, 5, 0.480724427)


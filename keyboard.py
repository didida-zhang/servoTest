import pynput
from pynput import keyboard
import time
import jkrc

global a
a =0
robot = jkrc.RC("192.168.164.183")
robot.login()
robot.power_on()
robot.servo_move_enable(1)

def test_push(key):
    
    if key == keyboard.Key.up:       
        robot.servo_j(joint_pos= [0.01,0,0,0,0,0], move_mode = 1)
        print("===按键向上===", a)
        time.sleep(0.006)
    if key == keyboard.Key.down:
        print("===按键向下===")
        robot.servo_j(joint_pos= [-0.01,0,0,0,0,0], move_mode = 1)

    if key == keyboard.Key.left:
        robot.servo_p(cartesian_pose = [1,0,0,0,0,0] , move_mode = 1)
        print("===按键向左===")

    if key == keyboard.Key.right:
        robot.servo_p(cartesian_pose = [-1,0,0,0,0,0] , move_mode = 1)
        print("===按键向右===")

def exit_listen(key):
    if key == keyboard.Key.esc:
        print("===退出===")
        return False

with keyboard.Listener(on_press=test_push, on_release=exit_listen) as listener:

    print('=======')
    listener.join()

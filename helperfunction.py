import rospy
import rospkg

rospack = rospkg.RosPack()
path = rospack.get_path('ur5_notebook') + '/'
ur_mp = path + 'ur5_mp.py'
ur_vision = path + 'ur5_vision.py'
ur_gripper = path + 'ur5_gripper'
launchfile = path + 'launch/initialize.launch'
killer = path + 'block_killer.py'
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose
from visualization_msgs.msg import Marker
import std_msgs.msg as stm
from multiprocessing import Process



def callback(data):
    #rospy.init_node("mark")
    
    # Creates Marker object named marker
    marker = Marker()

    # Define marker parameters
    marker.header.frame_id = "/world1"
    marker.header.stamp = rospy.Time.now()
    marker.type = Marker.CUBE
    marker.action = Marker.ADD
    marker.scale.x = 1
    marker.scale.y = 1
    marker.scale.z = 1
    marker.id = 10
    marker.pose.position.x = data.x;
    marker.pose.position.y = data.y;
    marker.pose.position.z = 0;
    marker.pose.orientation.x = 0.0;
    marker.pose.orientation.y = 0.0;
    marker.pose.orientation.z = 0.0;
    marker.pose.orientation.w = 1.0;
    marker.color = stm.ColorRGBA(r=0.0, g=1.0, b=0.0, a=0.8)
    marker.lifetime.secs = 10

    #Create Publisher called 'process_test' of type Marker
    pub = rospy.Publisher("TurtleMark", Marker, queue_size=10)

    #Publish marker
    pub.publish(marker)


    
def listener():


    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/turtle1/pose", Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

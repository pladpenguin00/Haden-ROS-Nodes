#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#ROBOT_MOVE_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def ROBOT_MOVE_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('ROBOT_MOVE_NODE', anonymous=True)
   
   #DIRECTIONS TOPIC (XYR POSITION

	rospy.Subscriber("DIRECTIONS_Topic", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

  
	

def ROBOT_MOVE_Pub():

   #CURRENT LOCATION TOPIC (XYR POSITION)

	pub1 = rospy.Publisher('DIRECTION_TOPIC', String, queue_size=10)
	rospy.init_node('NAVIGATION NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****CURRENT_LOCATION = "hello world %s" % rospy.get_time()
		rospy.loginfo(CURRENT_LOCATION)
		pub1.publish(CURRENT_LOCATION)
		rate.sleep()


  
if __name__ == '__main__':
 	ROBOT_MOVE_Sub()
	ROBOT_MOVE_Pub()
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#DEPTH_ORGANIZER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def DEPTH_ORGANIZER_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('DEPTH_ORGANIZER_NODE', anonymous=True)
   
   #POSITION_DEPTH_TOPIC (DEPTH IMAGE)

	rospy.Subscriber("POSITION_DEPTH_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

   #NEW_DEPTH_TOPIC (DEPTH IMAGE)

	rospy.Subscriber("NEW_DEPTH_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

   #UPDATED_LOCATION_TOPIC (XYR POSITION)

	rospy.Subscriber("UPDATED_LOCATION_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	

def DEPTH_ORGANIZER_Pub():

   #DEPTH_FOLDER_TOPIC (DEPTH IMAGE AND LABEL)

	pub1 = rospy.Publisher('DEPTH_FOLDER_TOPIC', String, queue_size=10)
	rospy.init_node('POSITION_ORGANIZER_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****DEPTH_FOLDER = "hello world %s" % rospy.get_time()
		rospy.loginfo(DEPTH_FOLDER)
		pub1.publish(DEPTH_FOLDER)
		rate.sleep()



  
if __name__ == '__main__':
 	DEPTH_ORGANIZER_Sub()
	DEPTH_ORGANIZER_Pub()
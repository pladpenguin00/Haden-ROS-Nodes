#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#POSITION_ORGANIZER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def POSITION_ORGANIZER_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('POSITION_ORGANIZER_NODE', anonymous=True)
   
   #CURRENT_LOCATION_TOPIC (XYR POSITION)

	rospy.Subscriber("CURRENT_LOCATION_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

   #NEW_XYR_TOPIC (XYR POSITION)

	rospy.Subscriber("NEW_XYR_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

	

def POSITION_ORGANIZER_Pub():

   #POSITION_FOLDER_TOPIC (XYR POSITION AND LABEL)

	pub1 = rospy.Publisher('POSITION_FOLDER_TOPIC', String, queue_size=10)
	rospy.init_node('POSITION_ORGANIZER_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****POSITION_FOLDER = "hello world %s" % rospy.get_time()
		rospy.loginfo(POSITION_FOLDER)
		pub1.publish(POSITION_FOLDER)
		rate.sleep()



  
if __name__ == '__main__':
 	POSITION_ORGANIZER_Sub()
	POSITION_ORGANIZER_Pub()
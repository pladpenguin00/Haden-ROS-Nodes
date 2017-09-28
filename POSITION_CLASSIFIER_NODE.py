#!/usr/bin/env python
import rospy
import tensorflow
from std_msgs.msg import String

#POSITION_CLASSIFIER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def POSITION_CLASSIFIER_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('POSITION_CLASSIFIER_NODE', anonymous=True)
   
   #CURRENT_POSITION_TOPIC (XYR POSITION)

	rospy.Subscriber("CURRENT_POSITION_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()


   #LOCATION_OBJECTIVE_TOPIC (XYR POSITION)

	rospy.Subscriber("LOCATION_OBJECTIVE_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()


   #TEST_TOPIC (1 OR 0)

	rospy.Subscriber("TEST_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	


def POSITION_CLASSIFIER_Pub():

   #POSITION_CONFIDENCE_TOPIC (%)

	pub1 = rospy.Publisher('POSITION_CONFIDENCE_TOPIC', String, queue_size=10)
	rospy.init_node('POSITION_CLASSIFIER_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****POSITION_CONFIDENCE = "hello world %s" % rospy.get_time()
		rospy.loginfo(POSITION_CONFIDENCE)
		pub1.publish(POSITION_CONFIDENCE)
		rate.sleep()

   #TEST_TOPIC (1 OR 0)

	pub1 = rospy.Publisher('UPDATED_LOCATION_TOPIC', String, queue_size=10)
	rospy.init_node('POSITION_CLASSIFIER_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****TEST = "hello world %s" % rospy.get_time()
		rospy.loginfo(TEST)
		pub1.publish(TEST)
		rate.sleep()


  
if __name__ == '__main__':
 	POSITION_CLASSIFIER_Sub()
	POSITION_CLASSIFIER_Pub()
#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#BUILD_LOCATION_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def BUILD_LOCATION_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('BUILD_LOCATION_NODE', anonymous=True)
   
   #LOCATION_CONFIRMED_TOPIC (XYR POSITION)

	rospy.Subscriber("LOCATION_CONFIRMED_TOPIC", String, callback)


	

def BUILD_LOCATION_Pub():

   #TAKE_PICTURE_TOPIC (1 OR 0)

	pub1 = rospy.Publisher('TAKE_PICTURE_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****TAKE_PICTURE = "hello world %s" % rospy.get_time()
		rospy.loginfo(TAKE_PICTURE)
		pub1.publish(TAKE_PICTURE)
		rate.sleep()

   #NEW_XYR_TOPIC (XYR POSITION)

	pub2 = rospy.Publisher('NEW_XYR_TOPIC', String, queue_size=10)
	rospy.init_node('BUILD_LOCATION_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():

						*****NEW_XYR = "hello world %s" % rospy.get_time()
		rospy.loginfo(NEW_XYR)
		pub2.publish(NEW_XYR)
		rate.sleep()

   #NEW_DEPTH_TOPIC (DEPTH IMAGE)

	pub3 = rospy.Publisher('NEW_DEPTH_TOPIC', String, queue_size=10)
	rospy.init_node('BUILD_LOCATION_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():

						*****NEW_DEPTH = "hello world %s" % rospy.get_time()
		rospy.loginfo(NEW_DEPTH)
		pub2.publish(NEW_DEPTH)
		rate.sleep()

   #NEW_PIC_TOPIC (RGB IMAGE)

	pub4 = rospy.Publisher('NEW_PIC_Topic', String, queue_size=10)
	rospy.init_node('BUILD_LOCATION_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():

						*****NEW_PIC = "hello world %s" % rospy.get_time()
		rospy.loginfo(NEW_PIC)
		pub2.publish(NEW_PIC)
		rate.sleep()

   #TRAIN_TOPIC (1 OR 0)

	pub5 = rospy.Publisher('TRAIN_Topic', String, queue_size=10)
	rospy.init_node('BUILD_LOCATION_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():

						*****TRAIN = "hello world %s" % rospy.get_time()
		rospy.loginfo(TRAIN)
		pub2.publish(TRAIN)
		rate.sleep()

  
if __name__ == '__main__':
 	BUILD_LOCATION_Sub()
	BUILD_LOCATION_Pub()

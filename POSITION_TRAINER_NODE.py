#!/usr/bin/env python
import rospy
import tensorflow
from std_msgs.msg import String

#POSITION_TRAINER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def POSITION_TRAINER_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('POSITION_TRAINER_NODE', anonymous=True)
   
   #POSITION_FOLDER_TOPIC (POSITION FOLDER WITH POSITIONS)

	rospy.Subscriber("POSITION_FOLDER_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

   #TRAIN_TOPIC (1 OR 0)

	rospy.Subscriber("TRAIN_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	


def POSITION_TRAINER_Pub():

   #UPDATED_LOCATION_TOPIC (XYR POSITION)

	pub1 = rospy.Publisher('UPDATED_LOCATION_TOPIC', String, queue_size=10)
	rospy.init_node('POSITION_TRAINER_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****UPDATED_LOCATION = "hello world %s" % rospy.get_time()
		rospy.loginfo(UPDATED_LOCATION)
		pub1.publish(UPDATED_LOCATION)
		rate.sleep()



  
if __name__ == '__main__':
 	POSITION_TRAINER_Sub()
	POSITION_TRAINER_Pub()
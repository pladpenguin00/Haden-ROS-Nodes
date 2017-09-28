#!/usr/bin/env python
import rospy
from destination_pose import String
from is_training import String
from std_msgs.msg import String
from current_location import String
from location_objective import String

#CHECK_LOCATION_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() , data.data)


def CHECK_LOCATION_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
   
   #CURRENT_LOCATION_TOPIC (XYR POSITION)

	current_location = rospy.Subscriber("CURRENT_LOCATION_TOPIC", String, callback)

   #LOCATION_OBJECTIVE_TOPIC (XYR POSITION)

	location_objective = rospy.Subscriber("LOCATION_OBJECTIVE_TOPIC", String, callback)
   
   #LOCATION_OBJECTIVE_TOPIC (XYR POSITION)

	is_training = rospy.Subscriber("IS_TRAINING_TOPIC", string, callback)

	

def CHECK_LOCATION_Pub():

   #TAKE PICTURE TOPIC (1 OR 0)

	pub1 = rospy.Publisher('Take_Picture_Topic', int32, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		rospy.loginfo(Take_Picture)
		pub1.publish(Take_Picture)
		rate.sleep()

   #TEST TOPIC (1 OR 0)

	pub2 = rospy.Publisher('Test_Topic', int32, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():

		rospy.loginfo(Test)
		pub2.publish(Test)
		rate.sleep()
		
		
	#TEST TOPIC (1 OR 0)
	
	pub3 = rospy.Publisher('Build_Topic', int32, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():

		rospy.loginfo(Build)
		pub3.publish(Build)
		rate.sleep()	

  
if __name__ == '__main__':
	rospy.init_node('CHECK_LOCATION_NODE', anonymous=True)
	
 	Check_Location_Sub()
	
	if current_location == location_objective
		Test = 0  
		Build = 1
		Take_Picture = 1
		
		else
		
		Test = 1
		Build = 0
		Take_Picture = 1
		
	Check_Location_Pub()

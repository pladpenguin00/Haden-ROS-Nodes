#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#RGB_ORGANIZER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def RGB_ORGANIZER_Sub():

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
	rospy.init_node('RGB_ORGANIZER_NODE', anonymous=True)
   
   #POSITION_PIC_TOPIC (RGB IMAGE)

	rospy.Subscriber("POSITION_PIC_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

   #NEW_PIC_TOPIC (RGB IMAGE)

	rospy.Subscriber("NEW_PIC_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

   #UPDATED_LOCATION_TOPIC (XYR POSITION)

	rospy.Subscriber("UPDATED_LOCATION_TOPIC", String, callback)
   
	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	

def RGB_ORGANIZER_Pub():

   #RGB_FOLDER_TOPIC (RGB IMAGE AND LABEL)

	pub1 = rospy.Publisher('RGB_FOLDER_TOPIC', String, queue_size=10)
	rospy.init_node('RGB_ORGANIZER_NODE', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
						*****RGB_FOLDER = "hello world %s" % rospy.get_time()
		rospy.loginfo(RGB_FOLDER)
		pub1.publish(RGB_FOLDER)
		rate.sleep()



  
if __name__ == '__main__':
 	RGB_ORGANIZER_Sub()
	RGB_ORGANIZER_Pub()
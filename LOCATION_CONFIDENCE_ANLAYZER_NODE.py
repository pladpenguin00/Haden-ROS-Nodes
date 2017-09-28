from std_msgs.msg import String
import numpy as np

#LOCATION_CONFIDENCE_ANLAYZER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() , data.data)


def LOCATION_CONFIDENCE_ANLAYZER_Sub():
   #DEPTH_CONFIDENCE_TOPIC (%)
	depth_conf = rospy.Subscriber("DEPTH_CONFIDENCE_TOPIC", int32, callback)
   

   #RGB_CONFIDENCE_TOPIC (%)
	rgb_conf = rospy.Subscriber("RGB_CONFIDENCE_TOPIC", int32, callback)
   

   #POSITION_CONFIDENCE_TOPIC (%)
	pos_conf = rospy.Subscriber("POSITION_CONFIDENCE_TOPIC", int32, callback)
	

def LOCATION_CONFIDENCE_ANLAYZER_Pub():
   #LOCATION_CONFIRMED_TOPIC (1 or 0)

	pub1 = rospy.Publisher('LOCATION_CONFIRMED_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		if (depth_conf + rgb_conf + pos_conf)/3 >= 90
			LOCATION_CONFIRMED = 1
			else 
			LOCATION_CONFIRMED = 0
		rospy.loginfo(LOCATION_CONFIRMED)
		pub1.publish(LOCATION_CONFIRMED)
		rate.sleep()



  
if __name__ == '__main__':
	rospy.init_node('LOCATION_CONFIDENCE_ANLAYZER_NODE', anonymous=True)
 	LOCATION_CONFIDENCE_ANLAYZER_Sub()
	LOCATION_CONFIDENCE_ANLAYZER_Pub()
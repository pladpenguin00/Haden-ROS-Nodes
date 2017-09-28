#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from current_location import String

#LOCATION_OBJECTIVE_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() , data.data)

def Location_Objective_Sub():

   #UPDATED LOCATION (XYR POSITION)

	# In ROS, nodes are uniquely named. If two nodes with the same
	# node are launched, the previous one is kicked off. The
	# anonymous=True flag means that rospy will choose a unique
	# name for our 'listener' node so that multiple listeners can
	# run simultaneously.
   
	rospy.Subscriber("current_location", string, callback)
	

	
   

def Location_Objective_Pub():

   #LOCATION OBJECTIVE TOPIC (XYR POSITION)

	pub1 = rospy.Publisher('Location_Objective_Topic', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		#location_objective = "Objective is: %s" % rospy.get_current_location()
		rospy.loginfo(location_objective)
		rostopic pub destination_pose/String location_objective
		rate.sleep()
  
if __name__ == '__main__':
	
	rospy.init_node('LOCATION OBJECTIVE NODE', anonymous=True)
	
	try:
		Location_Objective_Sub()
		
			if callback == location_objective:
            rospy.loginfo("Location Objective Found")
			
			#MAKE A NEW LOCATION OBJECTIVE
			newloc = np.random.randint(3, size=(1,1))
			r = np.random.randint(4, size=(1,1))
				if newloc == 0
					location_objective = "x:5 y:5 r:%s" % r
				elif newloc == 1
					location_objective = "x:5 y:0 r:%s" % r
				elif newloc == 2
					location_objective = "x:0 y:5 r:%s" % r
				
        else:
            rospy.loginfo("Location Not Found")
			
		rospy.sleep(.25)
		
		Location_Objective_Pub()


    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")
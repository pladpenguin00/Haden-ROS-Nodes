#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import os

#DEPTH_CNN_TRAINER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def DEPTH_CNN_TRAINER_Sub():
  
   #TRAIN_TOPIC (1 OR 0)
	onoff = rospy.Subscriber("TRAIN_TOPIC", String, callback)
   
	
def retrain_file():
	if onoff == 1
		os.system(r'python retrain.py --output_graph=retrained_graph.pb --output_labels=retained_labels.txt --image_dir=C:\Users\Haden\Desktop\Tensorflow_tutorials\retraining_a_network\byinch_photos')

def DEPTH_CNN_TRAINER_Pub():

   #TRAINED_DEPTH_CNN_TOPIC (RGB CNN)

	pub1 = rospy.Publisher('TRAINED_DEPTH_CNN_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		if onoff == 1
			TRAINED_DEPTH_CNN = "training depth %s" % rospy.get_time()
			else:
			TRAINED_DEPTH_CNN = "not training depth %s" % rospy.get_time()
		rospy.loginfo(TRAINED_DEPTH_CNN)
		pub1.publish(TRAINED_DEPTH_CNN)
		rate.sleep()

  
if __name__ == '__main__':
	rospy.init_node('RGB_CNN_TRAINER_NODE', anonymous=True)
 	DEPTH_CNN_TRAINER_Sub()
	retrain_file()
	DEPTH_CNN_TRAINER_Pub()
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import os

#RGB_CNN_TRAINER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def RGB_CNN_TRAINER_Sub():

   #TRAIN_TOPIC (1 OR 0)
	onoff = rospy.Subscriber("TRAIN_TOPIC", int32, callback)
   
	
def retrain_file():
	if onoff == 1
		os.system(r'python retrain.py --output_graph=retrained_graph.pb --output_labels=retained_labels.txt --image_dir=C:\Users\Haden\Desktop\Tensorflow_tutorials\retraining_a_network\byinch_photos')

	
def RGB_CNN_TRAINER_Pub():

   #TRAINED_RGB_CNN_TOPIC (RGB CNN)

	pub1 = rospy.Publisher('TRAINED_RGB_CNN_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		if onoff == 1
			TRAINED_RGB_CNN = "training rgb %s" % rospy.get_time()
			else:
			TRAINED_RGB_CNN = "not training rgb %s" % rospy.get_time()
		rospy.loginfo(TRAINED_RGB_CNN)
		pub1.publish(TRAINED_RGB_CNN)
		rate.sleep()


if __name__ == '__main__':
	rospy.init_node('RGB_CNN_TRAINER_NODE', anonymous=True)
 	RGB_CNN_TRAINER_Sub()
	retrain_file()
	RGB_CNN_TRAINER_Pub()
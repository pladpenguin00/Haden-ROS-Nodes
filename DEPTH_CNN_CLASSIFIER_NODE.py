#!/usr/bin/env python
import rospy
import tensorflow
from std_msgs.msg import String
#DEPTH_CNN_CLASSIFIER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def DEPTH_CNN_CLASSIFIER_Sub():

   #TRAINED_DEPTH_CNN_TOPIC (DEPTH CNN)
	rospy.Subscriber("TRAINED_DEPTH_CNN_TOPIC", int32, callback)
   

   #TEST_TOPIC (1 OR 0)
	onoff = rospy.Subscriber("TEST_TOPIC", int32, callback)
	
def classify():
	if onoff == 1
		os.system(r'python label_image.py --graph=retrained_graph.pb --labels=retrained_labels.txt --image=C:\Users\Haden\Desktop\Tensorflow_tutorials\retraining_a_network\test\inch2test.jpg')
   
def DEPTH_CNN_CLASSIFIER_Pub():

   #DEPTH_CONFIDENCE_TOPIC (%)

	pub1 = rospy.Publisher('DEPTH_CONFIDENCE_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		if onoff == 1
			DEPTH_CONFIDENCE = "%s depth location and confidence: %s - %s  %s - %s " % rospy.get_time() %resultlocation1 %conf_loc1 %resultlocation2 %conf_loc2
			else:
			DEPTH_CONFIDENCE = "not testing depth %s" % rospy.get_time()
		rospy.loginfo(DEPTH_CONFIDENCE)
		pub1.publish(DEPTH_CONFIDENCE)
		rate.sleep()


  
if __name__ == '__main__':
	rospy.init_node('DEPTH_CNN_CLASSIFIER_NODE', anonymous=True)
 	DEPTH_CNN_CLASSIFIER_Sub()
	classify()
	DEPTH_CNN_CLASSIFIER_Pub()
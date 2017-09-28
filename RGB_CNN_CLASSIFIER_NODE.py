#!/usr/bin/env python
import rospy
import tensorflow
from std_msgs.msg import String
#RGB_CNN_CLASSIFIER_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def RGB_CNN_CLASSIFIER_Sub():

   #POSITION_PIC_TOPIC (RGB IMAGE)
	rospy.Subscriber("POSITION_PIC_TOPIC", String, callback)


   #TEST_TOPIC (1 OR 0)
	onoff = rospy.Subscriber("TEST_TOPIC", String, callback)
   
def classify():
	if onoff == 1
		os.system(r'python label_image.py --graph=retrained_graph.pb --labels=retrained_labels.txt --image=C:\Users\Haden\Desktop\Tensorflow_tutorials\retraining_a_network\test\inch2test.jpg')
		
def RGB_CNN_CLASSIFIER_Pub():

   #RGB_CONFIDENCE_TOPIC (% NUMBER)

	pub1 = rospy.Publisher('RGB_CONFIDENCE_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
			if onoff == 1
			RGB_CONFIDENCE = "%s rgb location and confidence: %s - %s  %s - %s " % rospy.get_time() %resultlocation1 %conf_loc1 %resultlocation2 %conf_loc2
			else:
			RGB_CONFIDENCE = "not testing depth %s" % rospy.get_time()
		rospy.loginfo(RGB_CONFIDENCE)
		pub1.publish(RGB_CONFIDENCE)
		rate.sleep()


  
if __name__ == '__main__':
	rospy.init_node('RGB_CNN_CLASSIFIER_NODE', anonymous=True)
 	RGB_CNN_CLASSIFIER_Sub()
	classify()
	RGB_CNN_CLASSIFIER_Pub()
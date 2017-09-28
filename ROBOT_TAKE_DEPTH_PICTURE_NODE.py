#!/usr/bin/env python
import rospy
from __future__ import print_function
import sys
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String

#ROBOT_TAKE_DEPTH_PICTURE_NODE


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


def ROBOT_TAKE_DEPTH_PICTURE_Sub():
   #TAKE PICTURE TOPIC (1 OR 0)
	onoff = rospy.Subscriber("TAKE PICTURE_Topic", String, callback)
   

def ROBOT_TAKE_DEPTH_PICTURE_Pub():
   #POSITION_PIC_TOPIC (DEPTH IMAGE)

	pub1 = rospy.Publisher('POSITION_DEPTH_TOPIC', String, queue_size=10)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		if onoff == 1
			POSITION_DEPTH = depth_picture % rospy.get_time()
			else:
				POSITION_DEPTH = "no depth picture %s" % rospy.get_time()
		rospy.loginfo(POSITION_DEPTH)
		pub1.publish(POSITION_DEPTH)
		rate.sleep()
		

class TakeDepth:  ****************** NEED TO ADJUST FOR DEPTH MESSENGER 
    def __init__(self):

        self.bridge = CvBridge()
        self.image_received = False

        # Connect image topic
        img_topic = "/camera/rgb/image_raw"
        self.image_sub = rospy.Subscriber(img_topic, Image, self.callback)

        # Allow up to one second to connection
        rospy.sleep(1)

    def callback(self, data):

        # Convert image to OpenCV format
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "depth")
        except CvBridgeError as e:
            print(e)

        self.image_received = True
        self.image = cv_image

    def take_picture(self, img_title):
        if self.image_received:
            # Save an image
            cv2.imwrite(img_title, self.image)
            return True
        else:
            return False

if __name__ == '__main__':

    # Initialize
    rospy.init_node('take_photo', anonymous=False)
	ROBOT_TAKE_DEPTH_PICTURE_Sub()
    camera = TakePhoto()

    # Take a photo

    # Use '_image_title' parameter from command line
    # Default value is 'photo.jpg'
    img_title = rospy.get_param('~image_title', 'photo.jpg')

	if camera.take_picture(img_title):
		rospy.loginfo("Saved image " + img_title)
		else:
			rospy.loginfo("No images received")

			# Sleep to give the last log messages time to be sent
	rospy.sleep(1)
	ROBOT_TAKE_DEPTH_PICTURE_Pub()

	

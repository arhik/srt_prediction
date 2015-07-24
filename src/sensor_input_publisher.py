#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Float64

from sensor import Sensor
import numpy
import math
def sensor_input_publisher():
	pub = rospy.Publisher('sensor_stream', Float64, queue_size=10)
	rospy.init_node('sensor_input_publisher', anonymous=True)
	#r = rospy.Rate(1)
	x = [3,33,146,227,342,351,353,444,556,571,709,759,836,860,968,1056,1726,1846,1872,1986,2311,2366,2608,2676,3098,3278,3288,4434,5034,5049,5085,5089,5089,5097,5324,5389,5565,5623,6080,6380,6477,6740,7192,7447,7644,7837,7843,7922,8738]#,10089,10237,10258,10491,10625,10982,11175,11411,11442,11811,12559,12559,12791,13121,13486,14708,15251,15261,15277,15806,16185,16229,16358,17168,17458,17758,18287,18568,18728,19556,20567,21012,21308,23063,24127,25910,26770,27753,28460,28493,29361,30085,32408,35338,36799,37642,37654,37915,39715,40580,42015,42045,42188,42296,42296,45406,46653,47596,48296,49171,49416,50145,52042,52489,52875,53321,53443,54433,55381,56463,56485,56560,57042,62551,62651,62661,63732,64103,64893,71043,74364,75409,76057,81542,82702,84566,88682]
	#gen = Sensor()
	#x = [math.sin(i) for i in numpy.arange(1,2*math.pi,0.1)]
	while not rospy.is_shutdown():
		for i in x:
			time.sleep(0.5)
			val = math.fabs(i) 
			#val = 1000*gen.nxt_val_gen.next()
			rospy.loginfo("Sent %f at %s" %(val,rospy.get_time()))
			pub.publish(val)
		

if __name__=='__main__':
	try:
		sensor_input_publisher()
	except rospy.ROSInterruptException:
		pass

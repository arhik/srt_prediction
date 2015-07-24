#!/usr/bin/env python

import rospy
import numpy

from nupic.encoders import ScalarEncoder
from nupic.research.spatial_pooler import SpatialPooler

enc = ScalarEncoder(n=10000, w=21, minval = 0, maxval=10000)

from std_msgs.msg import String, Float64
t =[]
for i in range(10000):
    t.append(enc.encode(i))

print("Encoding is done")

sp = SpatialPooler(inputDimensions=(10000,),
                   columnDimensions=(20,),
                   potentialRadius=15,
                   numActiveColumnsPerInhArea=1,
                   globalInhibition=True,
                   synPermActiveInc=0.03,
                   potentialPct=1.0)
output = numpy.zeros((20,),dtype="int")
for _ in range(10):
    for i in xrange(10000):
        sp.compute(t[i], learn=True, activeArray=output)

print("Spatial pooler strengthened")

from nupic.research.TP import TP

tp = TP(numberOfCols=10000, cellsPerColumn=20,
        initialPerm=0.5, connectedPerm=0.5,
        minThreshold=10, newSynapseCount=10,
        permanenceInc=0.1, permanenceDec=0.0,
        activationThreshold=8,
        globalDecay=0, burnIn=1,
        checkSynapseConsistency=False,
        pamLength=10)

pub = rospy.Publisher("prediction_stream", Float64, queue_size=10)	

learn_steps = 10

learn_count = 0

def callback(data):
	global learn_steps
	global learn_count
	enc_x = enc.encode(data.data)
	while(learn_count < learn_steps):
		print("Learning Please be patient %d",learn_count)
		learn_count = learn_count + 1
		tp.compute(enc_x, enableLearn=True, computeInfOutput = False)
		continue
	
	if learn_count ==11:
		print("Lets test my learning capability")
	#tp.reset()
	tp.compute(enc_x, enableLearn=True, computeInfOutput= True)
	prediction = enc.decode(tp.getPredictedState())
	val = prediction[0]["[0:10000]"][1]
	print repr(val)
	val = list(val)
	predict = float(val[0])
	rospy.loginfo("Sensor Input : %s, its prediction : \n %f" %(data.data, predict))
	#type(prediction)
	pub.publish(predict)

def sensory_input_subscriber():
	rospy.init_node("sensory_input_subscriber",anonymous=True)
	rospy.Subscriber("sensor_stream", Float64, callback)
	rospy.spin()



if __name__=="__main__":
	sensory_input_subscriber()

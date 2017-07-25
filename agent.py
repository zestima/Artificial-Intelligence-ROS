#!/usr/bin/env python
# encoding: utf8
# Artificial Intelligence, UBI 2016
# Modified by: Luis Duarte, José Santos a34247 a33622

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import numpy as np
import math


x_ant = 0
y_ant = 0
obj_ant = ''
obj_list = []
x_list = []
y_list = []
room_visited = [0] * 12
room_visited[0] = 1


# ---------------------------------------------------------------
# odometry callback
def callback(data):
	global x_ant, y_ant
	global x, y
	global actual_room 
	x=data.pose.pose.position.x
	y=data.pose.pose.position.y
	# show coordinates only when they change
	if x != x_ant or y != y_ant:
		print " x=%.1f y=%.1f" % (x,y)

		if(x > -0.8 and x < 3.6 and y > -3.2 and y < 1.2):
			room_visited[0] = 1
			actual_room = 1
		if(x < -1.4 and x > -5.8 and y > -3.2 and y < 1.2):
			room_visited[1] = 1
			actual_room = 2
		if(x < -6.4 and x > -10.8 and y > -3.2 and y < 1.2):
			room_visited[2] = 1
			actual_room = 3
		if(x < -11.4 and x > -15.8 and y > -3.2 and y < 1.2):
			room_visited[3] = 1
			actual_room = 4
		if(x > -0.8 and x < 3.6 and y > 1.8 and y < 6.2):
			room_visited[4] = 1
			actual_room = 5
		if(x < -1.4 and x > -5.8 and y > 1.8 and y < 6.2):
			room_visited[5] = 1
			actual_room = 6
		if(x < -6.4 and x > -10.8 and y > 1.8 and y < 6.2):
			room_visited[6] = 1
			actual_room = 7
		if(x < -11.4 and x > -15.8 and y > 1.8 and y < 6.2):
			room_visited[7] = 1
			actual_room = 8
		if(x > -0.8 and x < 3.6 and y > 6.8 and y < 11.2):
			room_visited[8] = 1
			actual_room = 9
		if(x < -1.4 and x > -5.8 and y > 6.8 and y < 11.2):
			room_visited[9] = 1
			actual_room = 10
		if(x < -6.4 and x > -10.8 and y > 6.8 and y < 11.2):
			room_visited[10] = 1
			actual_room = 11
		if(x < -11.4 and x > -15.8 and y > 6.8 and y < 11.2):
			room_visited[11] = 1
			actual_room = 12

	x_ant = x
	y_ant = y

# ---------------------------------------------------------------
# object_recognition callback
def callback1(data):
	global obj_ant
	obj = data.data
	if obj != obj_ant:
		print "object is %s" % data.data
		if(findObj(data.data) == -1):
			obj_list.append(data.data)
			x_list.append(x)
			y_list.append(y)
	obj_ant = obj
		
# ---------------------------------------------------------------
# questions_keyboard callback
def callback2(data):
	print "question is %s" % data.data

	if(data.data == 'a'):
		questionA()
	if(data.data == 'b'):
		questionB()
	if(data.data == 'c'):
		questionC()
	if(data.data == 'd'):
		questionD()
	if(data.data == 'e'):
		questionE()
	if(data.data == 'f'):
		questionF()
	if(data.data == 'g'):
		questionG()
	if(data.data == 'h'):
		questionH()
	if(data.data == 'i'):
		questionI()
	if(data.data == 'j'):
		questionJ()
	if(data.data == 'k'):
		questionK()
	if(data.data == 'l'):
		questionL()
	if(data.data == 'm'):
		questionM()
	if(data.data == 'n'):
		questionN()
	if(data.data == 'o'):
		questionO()
	if(data.data == 'p'):
		questionP()
# ---------------------------------------------------------------
def agent():
	rospy.init_node('agent')

	rospy.Subscriber("questions_keyboard", String, callback2)
	rospy.Subscriber("object_recognition", String, callback1)
	rospy.Subscriber("odom", Odometry, callback)

	rospy.spin()

# ---------------------------------------------------------------
def findObj(data):
	i = 0
	for i in range(0,len(obj_list)):
		if(obj_list[i] == data):
			return i

	return -1
# ---------------------------------------------------------------
def findObjCoord(xmin,xmax,ymin,ymax):
	retList = []
	for i in range(0,len(x_list)):
		if(x_list[i] < xmax and x_list[i] > xmin and y_list[i] > ymin and y_list[i] < ymax):
			retList.append(obj_list[i])

	return retList	
# ---------------------------------------------------------------
def findRoomCoord(room):

	if(room == 1):
		return (-0.8, 3.6, -3.2, 1.2)
	if(room == 2):
		return (-5.8, -1.4, -3.2, 1.2)
	if(room == 3):
		return (-10.8, -6.4, -3.2, 1.2)
	if(room == 4):
		return (-15.8, -11.4, -3.2, 1.2)
	if(room == 5):
		return (-0.8, 3.6, 1.8, 6.2)
	if(room == 6):
		return (-5.8, -1.4, 1.8, 6.2)
	if(room == 7):
		return (-10.8, -6.4, 1.8, 6.2)
	if(room == 8):
		return (-15.8, -11.4, 1.8, 6.2)
	if(room == 9):
		return (-0.8, 3.6, 6.8, 11.2)
	if(room == 10):
		return (-5.8, -1.4, 6.8, 11.2)
	if(room == 11):
		return (-10.8, -6.4, 6.8, 11.2)
	if(room == 12):
		return (-15.8, -11.4, 6.8, 11.2)
	
# ---------------------------------------------------------------
def closest_obj(Xcmp, Ycmp):
	minimum = 99999
	index = -1
	x2 = x_list
	y2 = y_list
	
	if Xcmp in x2:
		x2.remove(Xcmp)
	if Ycmp in y2:
		y2.remove(Ycmp)

	#print x2
	#print y2

	for i in range(0,len(x2)):
		dist = math.hypot(x2[i] - Xcmp, y2[i] - Ycmp)
		if(dist < minimum):
			minimum = dist
			index = i

	print obj_list[index] 
	print minimum	
	


# ---------------------------------------------------------------
def recognize_room(room_obj_list):
	ccount = 0
	tcount = 0
	bcount = 0
	compcount = 0
	

	for i in range(0,len(room_obj_list)):
		if "table" in room_obj_list[i]:
			tcount = tcount + 1
		if "chair" in room_obj_list[i]:
			ccount = ccount + 1
		if "book" in room_obj_list[i]:
			bcount = bcount + 1
		if "computer" in room_obj_list[i]:
			compcount = compcount + 1

	if(ccount > 0 and tcount == 0 and bcount == 0 and compcount == 0):
		return 2 #Waiting Room
	if(ccount > 0 and tcount > 0 and bcount > 0 and compcount == 0):
		return 3 #Study Room
	if(ccount > 0 and tcount > 0 and bcount == 0 and compcount > 0):
		return 4 #Computer Room
	if(ccount > 0 and tcount == 1 and bcount == 0 and compcount == 0):
		return 5 #Meeting Room
	else:
		return 1 #Generic Room



# ---------------------------------------------------------------
def closest_obj_list(Xcmp, Ycmp, sx_list, sy_list):
	minimum = 99999
	index = -1
	x2 = sx_list
	y2 = sy_list
	
	if Xcmp in x2:
		x2.remove(Xcmp)
	if Ycmp in y2:
		y2.remove(Ycmp)

	#print x2
	#print y2

	for i in range(0,len(x2)):
		dist = math.hypot(x2[i] - Xcmp, y2[i] - Ycmp)
		if(dist < minimum):
			minimum = dist
			index = i

	return index

# ---------------------------------------------------------------
def create_cordlist(axis):
	retlist = []
	if(axis == 'x'):
		for i in range(0,len(obj_list)):
			retlist.append(obj_list[i].pose.pose.position.x)

	else:
		if(axis == 'y'):
			for i in range(0,len(obj_list)):
				retlist.append(obj_list[i].pose.pose.position.y)

	return retlist
		

# ---------------------------------------------------------------
def questionA():
	if(len(obj_list) == 0):
		print "I Haven't seen an object yet"
	else:
		print "The last object that i saw was %s" % obj_ant
	

#---------------------------------------------------------------
def questionB():
	print "I Have saw a total of %d objects" % len(obj_list)

#----------------------------------------------------------------
def questionC():
	#print obj_list
	#print x_list
	#print y_list
	if(len(obj_list) == 0):
		print "I Haven't seen an object yet"
	else:
		closest_obj(x, y)

#-----------------------------------------------------------------
def questionD():
	index = findObj("person_joe")
	if(index == -1):
		print "I Haven't seen Joe yet"
	else:
		closest_obj(x_list[index],y_list[index])
		

#-----------------------------------------------------------------
def questionE():
	conta = 0; 
	for i in range(0,len(obj_list)):
		if "book" in obj_list[i]:
			conta = conta + 1
	

	print "I have saw a total of %d books" % conta


#-----------------------------------------------------------------
def questionF():
	index = findObj("person_mary")
	if(index == -1):
		print "No"
	else:
		print "Yes"
	

#-----------------------------------------------------------------
def questionG():
	index = findObj("person_joe")
	if(index == -1):
		print "I Haven't seen Joe yet"
	else:
		xfind = x_list[index]
		yfind = y_list[index]

		if(xfind > -0.8 and xfind < 3.6 and yfind > -3.2 and yfind < 1.2):
			print "Joe is in room 1" 
		if(xfind < -1.4 and xfind > -5.8 and yfind > -3.2 and yfind < 1.2):
			print "Joe is in room 2" 
		if(xfind < -6.4 and xfind > -10.8 and yfind > -3.2 and yfind < 1.2):
			print "Joe is in room 3" 
		if(xfind < -11.4 and xfind > -15.8 and yfind > -3.2 and yfind < 1.2):
			print "Joe is in room 4"
		if(xfind > -0.8 and xfind < 3.6  and yfind > 1.8 and yfind < 6.2):
			print "Joe is in room 5"
		if(xfind < -1.4 and xfind > -5.8 and yfind > 1.8 and yfind < 6.2):
			print "Joe is in room 6" 
		if(xfind < -6.4 and xfind > -10.8 and yfind > 1.8 and yfind < 6.2):
			print "Joe is in room 7" 
		if(xfind < -11.4 and xfind > -15.8 and yfind > 1.8 and yfind < 6.2):
			print "Joe is in room 8" 
		if(xfind > -0.8 and xfind < 3.6  and yfind > 6.8 and yfind < 11.2):
			print "Joe is in room 9" 
		if(xfind < -1.4 and xfind > -5.8 and yfind > 6.8 and yfind < 11.2):
			print "Joe is in room 10" 
		if(xfind < -6.4 and xfind > -10.8 and yfind > 6.8 and yfind < 11.2):
			print "Joe is in room 11"
		if(xfind < -11.4 and xfind > -15.8 and yfind > 6.8 and yfind < 11.2):
			print "Joe is in room 12" 

	


#-----------------------------------------------------------------
def questionH():
	conta = 0; 
	for i in range(0,len(obj_list)):
		if "table" in obj_list[i]:
			conta = conta + 1
	
	
	if(conta == 0):
		print "No"
	else:
		print "Yes"


#-----------------------------------------------------------------
def questionI():
	for i in range(0,len(room_visited)):
		if(room_visited[i] == 1):
			val = i+1
			print "I have been in room: %d" % val


#-----------------------------------------------------------------
def questionJ():
	flagc = 0
	flagt = 0
	flagp = 0
	div = 0
	den = 0

	for j in range(0,len(room_visited)):
		if(room_visited[j] == 1):
			send = j + 1
			minX, maxX, minY, maxY = findRoomCoord(send)
			modlist = findObjCoord(minX, maxX, minY, maxY)
			for p in range(0,len(modlist)):
				if(flagc == 1 and flagt== 1):
					break
				if "chair" in modlist[p]:
					if(flagc == 1):
						break
					else:
						flagc = 1
				if "table" in modlist[p]:
					flagt = 1
				if "person" in modlist[p]:
					flagp = 1

			if(flagc == 1 and flagt == 0):
				div = div + 1
			if(flagc == 1 and flagt == 0 and flagp == 1):
				den = den + 1

	
	if(den == 0):
		print "Its 0 since there is no person in a room with a chair and no tables"
	else:
		if(div == 0):
			print "Its 0 since there is no room with those conditions"	
		else:
			result = float(den)/div
			print "Its %d " % result
	

#-----------------------------------------------------------------
def questionK():
	conta = 0
	containt = 0
	flagt = 0
	flagp = 0
 
	for i in range(0,len(obj_list)):
		if "table" in obj_list[i]:
			conta = conta + 1

	for j in range(0,len(room_visited)):
		if(room_visited[j] == 1):
			send = j + 1
			minX, maxX, minY, maxY = findRoomCoord(send)
			modlist = findObjCoord(minX, maxX, minY, maxY)
			for p in range(0,len(modlist)):
				if(flagt == 1 and flagp == 1):
					containt = containt + 1
					flagt = 0
					flagp = 0
				if "table" in modlist[p]:
					flagt = 1
				if "person" in modlist[p]:
					flagp = 1	
				
	print "%d" % len(obj_list)
	if(conta == 0 or containt == 0):
		print "Its 0, since i haven't saw a table or a person"
	else: 	
		tablprob = float(conta)/len(obj_list)
		#print "table prob %f" % tablprob
		interprob = float(containt)/len(obj_list)
		#print "inter prob %f" % interprob
		result = interprob/tablprob
		print "Acording to my state its about %f" % result

#-----------------------------------------------------------------
def questionL():

	send_list = []
	#print actual_room
	minX, maxX, minY, maxY = findRoomCoord(actual_room)
	#print minX
	#print maxX
	#print minY
	#print maxY
	send_list = findObjCoord(minX, maxX, minY, maxY)
	#print send_list
	if (len(send_list) < 1):
		print("I dont have enough information about the room")
	else:
		ret = recognize_room(send_list)
	
		if(ret == 1):
			print "Im in a generic room"
		if(ret == 2):
			print "Im in a waiting room"
		if(ret == 3):
			print "Im in a study room"
		if(ret == 4):
			print "Im in a computer room"	
		if(ret == 5):
			print "Im in a meeting room"

#-----------------------------------------------------------------
def questionM():
	check_list = []
	free_list = room_visited
	for i in range(0,len(room_visited)):
		if(room_visited[i] == 1):
			minX, maxX, minY, maxY = findRoomCoord(i+1)
			check_list = findObjCoord(minX, maxX, minY, maxY)
			for j in range(0,len(check_list)):
				if "person" in check_list[j]:
					free_list[i] = 0



	for p in range(0,len(free_list)):
		if(free_list[p] == 1):
			print "Room %d is free" % (p+1)		
			

#-----------------------------------------------------------------
def questionN():
	temp_obj = []	
	temp_x = []
	temp_y = []
	index = findObj("person_mary")
	if(index == -1):
		print "I Haven't saw Mary so i can't answer that question"
	else:
		for i in range(0,len(obj_list)):
			if "computer" in obj_list[i]: 
				temp_x.append(x_list[i])
				temp_y.append(y_list[i])
				temp_obj.append(obj_list[i])

		
		
		ret = closest_obj_list(x_list[index], y_list[index], temp_x, temp_y)
		if "Apple" in obj_list[ret]:
			print "Mary is an Apple fan of course"
		else:
			print "Its a Microsoft fan"	
		

#-----------------------------------------------------------------
def questionO():
	if(actual_room == 7):
		print "Yes, because im Room 7"
	else:
		if(actual_room == 4 or actual_room == 8 or actual_room == 12):
			print "Yes"
		else:
			print "No"



#-----------------------------------------------------------------
def questionP():
	flagr = 0
	c_room = 0

	for i in range(0,len(room_visited)):
		if(room_visited[i] == 1):
			minX, maxX, minY, maxY = findRoomCoord(i+1)
			send_list = findObjCoord(minX, maxX, minY, maxY)
			ret = recognize_room(send_list)
			if(ret == 4):
				flagr = 1
				c_room = i + 1

	if(flagr == 0):
		print "I Haven't found the Computer Room"
	else:
		if(actual_room == 5 or actual_room == 10):
			print "None because its the one next to me"
		if(actual_room == 6):
			print "Rooms 5 or 10"
		if(actual_room == 1):
			print "Room 5"
		if(actual_room == 2):
			print "Rooms 5 and 6"
		if(actual_room == 3):
			print "Rooms 2 -> 6 -> 5"
		if(actual_room == 4):
			print "Rooms 8 -> 7 -> 6 -> 10"
		if(actual_room == 7):
			print "Rooms 6 and 10"
		if(actual_room == 8):
			print "Rooms 7 -> 6 -> 10"
		if(actual_room == 9):
			print "Im in the computer room"
		if(actual_room == 11):
			print "Room 10"
		if(actual_room == 12):
			print "Rooms 8 -> 7 -> 11 -> 10"

#-----------------------------------------------------------------

if __name__ == '__main__':
	agent()

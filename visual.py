import matplotlib.pyplot as plt
import matplotlib.patches as patches
from math import sqrt


# base receiver
base_receiver = [200, 150]
# the [x, y] to be added to the the receiver
# x distance on the x axis between each receiver, same for y
receiver_adder = [150, 75]
# number of receivers
receiver_num = 10

# senders points
senders = [[102, 105], [78, 77], [68, 119]]


# basic functions for plotting on the graph

def plt_circle(x, y, radius):
	circle = plt.Circle((x, y), radius, fill = False)
	ax.add_artist(circle)

def plt_point(x, y, c):
	if c == 'r+':
		plt.plot(x, y, 'r+')
	elif c == 'b+':
		plt.plot(x, y, 'b+')

def plt_text(x, y, text):
	ax.text(x, y, text)


# creates a list of [x, y] for each receiver using the base and the adder

def receiver_points(base_receiver, receiver_adder, receiver_num):
	
	# empty output list
	receiver_points = []

	for i in range(receiver_num):

		# appends the receiver points to list
		receiver_points.append([base_receiver[0], base_receiver[1]])

		# adds [x, y] from the adder to the [x, y] of the receiver 
		base_receiver[0] += receiver_adder[0]
		base_receiver[1] += receiver_adder[1]
	
	return receiver_points


#functions to plot the necessary points

# plots every [x, y] in the receiver list

def plt_receiver(receivers):
	for i in receivers:
		plt_point(i[0], i[1], 'r+')

# plots the sender points

def plt_sender(senders):
	for i in senders:
		plt_point(i[0], i[1], 'b+')


# gets distance between two points

def point_distance(x1, y1, x2, y2):
	return sqrt((x2 - x1)**2 + (y2 - y1)**2)


# function to plot circles around senders

def plt_signal(receivers, senders):
	for i in receivers:
		for j in senders:
			plt_circle(j[0], j[1], point_distance(i[0], i[1], j[0], j[1]))


# function to find the average position of the senders

def average_position(senders):
	x, y = 0, 0
	for i in senders:
		x += i[0]
		y += i[1]
	x = x / len(senders)
	y = y / len(senders)
	return [x, y]


# function to add text to each receiver

def text_receiver(receivers, senders):
	average_pos = average_position(senders)
	for i in receivers:
		plt_text(i[0], i[1], round(point_distance(i[0], i[1], average_pos[0], average_pos[1]), 1))






fig, ax = plt.subplots()
ax.set(xlim=(0, 1600), ylim = (0, 900))



receivers = receiver_points(base_receiver, receiver_adder, receiver_num)
plt_receiver(receivers)
plt_sender(senders)
plt_signal(receivers, senders)
text_receiver(receivers, senders)


plt.show()
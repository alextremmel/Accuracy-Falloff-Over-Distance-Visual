import matplotlib.pyplot as plt
import matplotlib.patches as patches
from math import sqrt


# base receiver
base_receiver = [150, 125]
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
		plt.plot(x, y, 'r+', markersize=8)
	elif c == 'b+':
		plt.plot(x, y, 'b+', markersize=8)

def plt_text(x, y, text, size):
	ax.text(x, y, text, size=size)


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
		plt_text(i[0], i[1], round(point_distance(i[0], i[1], average_pos[0], average_pos[1]), 1), 10)


# function for the legend or the description

def description():
	ax.add_patch(patches.Rectangle((1200, 50), 350, 200, color="w", zorder=2, ec="r"))
	plt_point(1220, 220, 'r+')
	plt_text(1220, 220, "  distance", 10)
	plt_text(1205, 160, "red + is a space ship, distance is the distance from\n the space ship to the average satellite position", 12)
	plt_point(1220, 120, 'b+')
	plt_text(1210, 70, "blue + is a satellite", 12)
	circle = plt.Circle((1375, 120), 15, fill = False, zorder=3)
	ax.add_artist(circle)
	plt_text(1400, 60, "there are 3 circles\n intersecting at each\n ship each with\n a center at a\n different satellite", 12)

# function to explain the goal of the visual

def goal():
	ax.add_patch(patches.Rectangle((50, 680), 350, 170, color="w", zorder=2, ec="r"))
	text = '''
This visual shows that the further the space ship
gets from the satellites, the lower the location
accuracy is, or if the red + was not there, the
harder it would be to see its exact position.
As the visual shows, with the closest space ship,
even without the red +, it is easy to tell where the
circles intersect, but as the distance increases,
the red + is more and more needed
to show exactly were the circles intersect.'''
	plt_text(55, 690, text, 12)



fig, ax = plt.subplots()
ax.set(xlim=(0, 1600), ylim = (0, 900))
plt.title("Accuracy Fall-off Over Distance")
plt.xlabel("Arbitrary Unit")
plt.ylabel("Arbitrary Unit")

receivers = receiver_points(base_receiver, receiver_adder, receiver_num)
plt_receiver(receivers)
plt_sender(senders)
plt_signal(receivers, senders)
text_receiver(receivers, senders)
description()
goal()
plt.show()
# Accuracy-Falloff-Over-Distance-Visual

Python script to visualize how the accuracy of a positioning system is affected by the distance between objects.

This script uses the terms senders and receivers, which are general terms for satellite and phone, or ground station and space ship.

senders having a known position and receivers having and unknown position.


## The general relation can be described as :

location_accuracy = time_accuracy * (average_sender_distance / receiver_distance)


## Where :

average_sender_position = (average x value of each sender, average y value of each sender)

average_sender_distance = average distance from each sender to the average_sender_position

receiver_distance = distance from the receiver to the average_sender_position

time_accuracy = accuracy of the clock on the receiver, higher is more accurate

location_accuracy = accuracy of the position, higher is more accurate

![Alt text](Accuracy-Falloff-Over-Distance.png?raw=true "Title")

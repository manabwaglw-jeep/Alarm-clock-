# Alarm Clock in Python

A simple alarm clock i made using Python while practicing OOP concepts like 
classes, inheritance and objects.

## Concepts I practiced

- Classes
- Inheritance
- Objects
- Methods
- Constructor ( __init__ )

## What I used

- Python
- pygame library
- datetime module

## How it works

I made two classes alarm and Clock. Clock inherits from alarm so it gets 
all the properties of alarm class. The program keeps checking the current 
time every second and when it matches the alarm time it plays a sound.
You can stop the sound by typing o and pressing enter.

## How to run it

First install pygame by running this in your terminal

    pip install pygame

Then make sure you have a file called alarm.mp3 in the same folder as the code.

Then run the file

    python alarm.py

## What it asks you

    enter your alarm time(HH:MM:SS):

Just type the time like this 20:12:00 and press enter.

## What happens after

The program prints the current time every second.
When the alarm time hits it plays the sound.
You type o to stop the alarm and it wishes you a energetic day.

## Files needed

- alarm.py
- alarm.mp3

## Note

Make sure alarm.mp3 is in the same folder otherwise it will give an error.
This is one of my early projects where i tried to use oops in a real project.

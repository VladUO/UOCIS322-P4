# UOCIS322 - Project 4 #
Brevet time calculator.

Author: Vladimir Shatalov
Address: vvs@uoregon.edu



This is a program for calculating checkpoint open and close times for brevets (bicycle races) of various lengths.

There are a total of 5 possible lengths of brevets, they are: 200, 300, 400, 600 and 1000km. The rules for setting checkpoints and calculating their open and close times are described here https://rusa.org/pages/acp-brevet-control-times-calculator 

The program uses an HTML page to take in your input in the form of your chosen brevet length, starting date/time for the race, and the checkpoint/control distance. Once your checkpoint/control distance is entered, a JSON request is sent to “flask_brevets.py” with those three pieces of data. There it is formatted and sent to two separate functions in acp_times.py, “open_time” and “close_time”, the functions calculate the open and close times for this checkpoint/control location…

Within those two functions are some special cases: a bias for checkpoints set within the first 60km, every brevet length has a set closing time that is not calculated, and the checkpoints are allowed up to 20% over brevet distance but their open and closing times do not change past those set closing times. 

The current design of “acp_times.py” functions deals with the special cases using separate if statements. All the other cases are calculated by taking the high and the low values for a given brevet “bracket”, and if the checkpoint falls in between those values or within 120% of the high value, the low value is subtracted from the checkpoint distance and divided by the speed for that brevet bracket. This produces the time for that stretch of the race which is added to the total time. Then the remaining checkpoint distance is automatically within the next bracket down and the process repeats until its 0. At that point the total time is rounded and the opening/closing time is shifted by that amount in minutes.

In simple terms the method I have chosen the method of “chopping down” the distance, starting from the top and going down through all the brevet “brackets” to calculate the individual times for that stretch of the race based on the speeds allowed on that stretch. Once all those times are added up you get your minimum and maximum allowed times for the given checkpoint and those values are used to shift the starting time and get the output.  

"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

#making tupples for speed brackets and for set closing times
MAXSPEEDS = [(1000, 600, 28), (600, 400, 30), (400, 300, 32), (300, 200, 32), (200, 0, 34)]
MINSPEEDS = [(1000, 600, 11.428), (600, 400, 15), (400, 300, 15), (300, 200, 15), (200, 0, 15)]
MAXTIMES = [(200, 810), (300, 1200), (400, 1620), (600, 2400), (1000, 4500)]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):

   print("Entered open time calculation.")            #a marker to know when entering this function
   print("Brevet start time:", brevet_start_time)     #printing out start time just for reference

   #special case for trying to set a checkpoint over brevet + 20%
   if control_dist_km > (1.2 * brevet_dist_km) :
      # raise ValueError("Checkpoint over max allowed distance.")
      return "Checkpoint over max allowed distance."

   #special case for trying to use a negative number as checkpoin
   if (control_dist_km < 0):
      # raise ValueError("Checkpoint has to be a positive number.")    
      return "Checkpoint has to be a positive number."   

   # assign opening time to a new variable, set it to start time to begin with
   otime = brevet_start_time
   checkpoint_dist = control_dist_km     #variable to keep track of remaining distance   
   minutes = 0                           #variable to keep track of time to shift by             

   for item in MAXSPEEDS:
      brevet_high, brevet_low, speed = item 
      
      #checking for special case when our checkpoint is at or past the length of the brevit
      if ((checkpoint_dist >= brevet_dist_km) and (brevet_high == brevet_dist_km)):
         minutes += (((brevet_high - brevet_low)/speed) * 60)
         remove = (checkpoint_dist - brevet_low)
         checkpoint_dist -= remove      
   
      #this is the regular calculation for the opening time
      if ((checkpoint_dist <= brevet_high * 1.2) and (brevet_high <= brevet_dist_km) and (control_dist_km > brevet_low)):
         minutes += (((checkpoint_dist - brevet_low)/speed) * 60)
         checkpoint_dist -= (checkpoint_dist - brevet_low)

   minutes = round(minutes)   
   otime = otime.shift(minutes = +minutes)              

   print("OPENING TIME", otime)
   return otime


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   print("Entered close time calculation.")             #a marker to know when entering this function          
   print("Brevet start time:", brevet_start_time)       #printing out start time just for reference 

   #special case for trying to set a checkpoint over brevet + 20%
   if control_dist_km > (1.2 * brevet_dist_km):
      # raise ValueError("Checkpoint over max allowed distance.")     
      return "Checkpoint over max allowed distance."

   #special case for trying to use a negative number as checkpoint
   if (control_dist_km < 0):
      # raise ValueError("Checkpoint has to be a positive number.")    
      return "Checkpoint has to be a positive number."    

   # assign opening time to a new variable, set it to start time to begin with
   ctime = brevet_start_time
   checkpoint_dist = control_dist_km
   minutes = 0

   #special case for checkpoint at or above the brevet distance
   for item in MAXTIMES:
      dist, min = item
      if ((dist == brevet_dist_km) and (checkpoint_dist >= brevet_dist_km)):
         minutes = min
         ctime = ctime.shift(minutes = + minutes)
         return ctime    

   #special case, offset for checkpoint under 60km out, addit offset
   if control_dist_km < 60:
      minutes += round(60 - control_dist_km)    
         
   #calculating the closing time for all normal cases
   for item in MINSPEEDS:
      brevet_high, brevet_low, speed = item 
      if ((checkpoint_dist <= brevet_high * 1.2) and (brevet_high <= brevet_dist_km) and (control_dist_km > brevet_low)):
         minutes += (((checkpoint_dist - brevet_low)/speed) * 60)           
         checkpoint_dist -= (checkpoint_dist - brevet_low)
      
   minutes = round(minutes)   
   ctime = ctime.shift(minutes = +minutes)              


   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  A date object (arrow)
   Returns:
      A date object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """
   print("CLOSING TIME", ctime)
   return ctime

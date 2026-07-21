## Convert time entered in hh,min and sec into seconds.
  
hours = float(input('Enter Hours:'))
minutes = float(input('Enter minutes:'))
seconds = float(input('Enter Seconds:')) 

Total_seconds = (hours * 3600) + (minutes * 60) + seconds
print('Converted Time  in Seconds:',Total_seconds)

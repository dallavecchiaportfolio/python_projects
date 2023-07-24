import datetime
 
# using now() to get current time
current_time = datetime.datetime.now()
 
# Printing value of now.
#print("Time now at greenwich meridian is:", current_time)

#print(type(current_time))

tmpTime = current_time.strftime('%H%M%S')
tmpDate = current_time.strftime("%D%m")
tmpDate = tmpDate.replace("/","")

#tmpTime = strcurrent_time.replace("-","")

print(tmpTime)
print(tmpDate)

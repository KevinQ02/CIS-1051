# part 4

seconds =input("Enter seconds, I'll tell you how many how many hours and minutes that is ")
seconds =int(seconds)

hours = seconds//(60*60)
Second = seconds % 3600
#print(Second)
Minutes = (Second//60)
Second = Second%(60)

print(seconds, "seconds is",hours,"hours", Minutes, "minutes and",Second,"seconds")

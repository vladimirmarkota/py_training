#print("hello world".ljust(15, "-"))

#print("hello world".center(30, "*"))

#strip removes, rlstrip
#print("hello world!1111111".lstrip("1"))

#replace searches for and replaces string
#print("good morning.".replace("morning", "evening"))

the_string = "North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17, "*"))

center_plus = the_string.center(16, "+")
print(center_plus)

print(the_string.lstrip("North"))
print(center_plus.strip("+"))
print(the_string.replace("North", "South"))

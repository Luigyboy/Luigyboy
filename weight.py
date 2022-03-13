#client interactive project, input earth's weight and output user's mars weight.
#introduction message & prompts
intro = "Welcome to 'know your weight'.com" + "\nWe're happy to see you back here!"
print(intro)
prompt1 = "\tPlease write your body weight:\n\t"
prompt2 = "\tWrite your name:\n\t"
#dictionary to display the message
weights = {
}
#flag statement
flag = True
while flag:
	#inputs
	#dictionary storage
	earth_w = input(prompt1)
	name = input(prompt2)
	#if statement to break
	weights[name] = earth_w
	stop = input("Is there somebody else wondering to know their weight in mars and the moon? (yes/no) ")
	if stop == 'no':
		flag = False
#This are the results
print("!----RESULTS----!")
#for loop in order to display results
for key,value in weights.items():
	#values convertion
	mars = (float(value)*float(3.711))/float(9.81)
	moon = (float(value)*float(1.622))/float(9.81)
	#print section
	print("Name: " + key.title())
	print("Earth weight: " + str(value) +'N')
	print("Mars weight: " + str(mars) +'N')
	print("Moon weight: "+ str(moon) +'N')
	print("************")
#DONE!
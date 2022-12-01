mySubject = "Computer Science"

#print(mySubject[0:len(mySubject)])        # in this whole string is printed For ex- ComputerScience
#print(mySubject[-7:-1])                   # in this negative indecies starts from last word of the string For ex- Scienc
#print(mySubject[::2])                     # in this the integer take 1 time gap and print for ex- Cmu etc.
#print(mySubject[len(mySubject)-1])        # in this -1 print the last chasreacter of the string for ex- e.
#print(2*mySubject)                        # in this the integer *2 print 2 times the string For ex- ComputerScienceComputerScience.
#print(mySubject[::-2])                    # it is same as no5 but in this negative indecies are there so it is counted by backward  For ex- eniSrtpo.
#print(mySubject[:3]+mySubject[3:])        # it is so tricky but the logic is [:3]+[3:]=Com puter Science.
#print(mySubject.swapcase())               # in this swapcase minimize or small the first character of every single word gioven in the string  For ex- cOMPUTER sCIENCE.
#print(mySubject.startswith('Comp'))       # in this the startswith function find that the starting word of the given line is true or not  For ex- ('comp') this is true.
#print(mySubject.isalpha())                # Return True if the string is an alphabetic string, False otherwise.




myAddress = "WZ-1,New Ganga Nagar,New Delhi"

#print(myAddres.lower())                   #Return a copy of the string converted to lowercase For ex- wz-1,new ganga nagar, new delhi.
#print(myAddres.upper())                   #Return a copy of the string converted to uppercase For ex- WZ-1,NEW GANGA NAGAR, NEW DELHI.
#print(myAddres.count('New'))              #Count the specific word how many times the word given in the string For ex- 2.
#print(myAddress.find('New'))              #finds the occurance or position of the word if the word is not in the string it returns -1.
#print(myAddress.rfind('New'))             #Returns the highest occurance or position of the same word given in the string For ex 22.
#print(myAddress.split(','))               #Return a list of the substrings in the string, using sep as the separator string. For ex- ['WZ-1', 'New Ganga Nagar', ' New Delhi'].
#print(myAddress.split(' '))               #Return a list of the substrings in the string, using sep as the separator string. For ex- ['WZ-1', 'New Ganga Nagar', 'New Delhi'].
#print(myAddress.replace('New','Old'))     #Return a copy with all occurrences of substring old replaced by new For ex- WZ-1,Old Ganga Nagar,Old Delhi.
#print(myAddress.partition(','))           #Partitions the given string at the first occurance of the sub string(seprator) and returns the string partitioned into 3 parts For ex- ('WZ-1', ',', 'New Ganga Nagar,New Delhi').
#print(myAddress.index('Agra'))            #Same as find() but raises an exception if the substring is not present in the given string it will give ValueError: substring not found.


 



a=str("786")
b="Python"*4
print(a,b)
a=a+b
print(len(a))













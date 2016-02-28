import random
zahl = random.randrange(1000); tipp = 0; i = 0
while tipp != zahl:
    tipp = input("Dein Tipp:")
    if zahl < tipp:
        print "Die gesuchte Zahl ist kleiner als ", tipp

    if zahl > tipp:
        print "Die gesuchte zahl ist gößer als ", tipp
                            
    i += 1
print "Du hast die Zahl beim ",i," Tipp erraten"  

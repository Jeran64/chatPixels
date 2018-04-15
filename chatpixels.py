from PIL import Image
from itertools import islice

print "working."
im= Image.open("chatImage.png")
uniqueColors=[]

offset=[30,30]

imPixels=im.load()#load our .png

def chunk(it, size):#https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

#get a list of our unique colors.
for x in range (0,im.size[0]):
    for y in range (0,im.size[1]):  
        if((imPixels[x,y] in uniqueColors)==0):#if we dont already have this color in our list, then add it.
            uniqueColors.append(imPixels[x,y])#add it.
            #print imPixels[x,y]
colorPlaces=[[] for i in range(len(uniqueColors))]#now that we have all of our unique colors, we need another list to store all of thier locations.

#add our colors names to the start of this list.
for a in range(len(uniqueColors)):
    colorPlaces[a].append('#%02x%02x%02x' % uniqueColors[a])#https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python

#add our locations, by going throught he image again.
for x in range (0,im.size[0]):
    for y in range (0,im.size[1]):
        colorPlaces[uniqueColors.index(imPixels[x,y])].append(str(x+offset[0])+","+str(y+offset[1])+";")#this formats our data into the string format that the script expects. x1,y1;x2,y2;x3,y3;

#output in a copy and pastable format
for a in range(len(uniqueColors)):
    print "New Color"
    if(len(colorPlaces[a])<21):#if we have less than 10 entries, just shove it out there.
        print " ".join(colorPlaces[a])#this converts our list into a hand string, separated by spaces. handy!
    else:
        tunaFish=list(chunk(colorPlaces[a],20))#returns a bunch of lists to use.
        print "Long one!"
        print " ".join(tunaFish[0])#paste the first one as is, as it will contain the color hex at the start.
        for c in range(1,len(tunaFish)):
            print colorPlaces[a][0]+" "+"".join(tunaFish[c])#add the colors name, which is at the start of the jagged array, and then add the .joined value of the remaining fish.
  

import requests
import myLaunch

# Making a GET request
r = requests.get('https://spaceflightnow.com/launch-schedule/')

# check status code for response received
print(r)
contents = str(r.content)

#list to store synthesized launch data in "myLaunch" objects
launches = []

#step through each character in the html
for i in range(0, len(contents)):
    #find the data once you find this trigger
    if contents[i:i+14] == ">Launch time:<":
        #step back to find the date
        slashNs = 0
        dateEnd = i
        while slashNs < 2:
            dateEnd -= 1
            if contents[dateEnd:dateEnd+2] == '\\n':
                slashNs += 1
        dateStart = dateEnd - 1
        while contents[dateStart:dateStart+2] != '\\n':
            dateStart -= 1
        dateStart += 2

        #step back to get launch title
        titleEnd = i
        while contents[titleEnd:titleEnd+7] != "</span>":
            titleEnd -= 1
        titleStart = titleEnd - 1
        while contents[titleStart] != '>':
            titleStart -= 1
        titleStart += 1

        #step forward to find launch time
        timeEnd = i
        while contents[timeEnd:timeEnd+4] != "<BR>":
            timeEnd += 1
        timeStart = timeEnd-1
        while contents[timeStart:timeStart+2] != "\\n":
            timeStart -= 1
        timeStart += 2

        launches.append(myLaunch.myLaunch(contents[titleStart:titleEnd], contents[timeStart:timeEnd], contents[dateStart:dateEnd]))

saveFile = open("out.txt", 'w')
for launch in launches:
    #save launches to a file
    saveFile.write(myLaunch.myLaunch.launchToString(launch))
saveFile.close()
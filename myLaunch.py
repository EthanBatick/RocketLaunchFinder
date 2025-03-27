class myLaunch:
    def __init__(self, title, time, date):
        self.title = title
        self.time = time
        self.date = date
        self.title = self.cleanTitle()
        self.time = self.cleanTime()

    #cleans up title of stupid metadata \xx\yy\zz
    def cleanTitle(self):
        return self.title.split("\\")[0] + "- " + self.title.split("\\")[-1][4:len(self.title.split("\\")[-1])]
    
    #cleans up time if its TBD
    def cleanTime(self):
        if self.time[0:3] == 'TBD':
            return "a time yet to be determined"
        else:
            return self.time

    #print conents of 
    def launchToString(self):
        str1 = self.title + " launches on " + self.date + " at " + self.time
        if self.time[len(self.time)-3:len(self.time)] != "\\n":
            str1 += '\n'
        return str1
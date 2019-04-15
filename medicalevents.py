import urllib.request
import http.cookiejar

#set up cookie opener
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

URLprefix="https://www.nrc.gov/reading-rm/doc-collections/event-status/event/"
URLsuffix="en.html"
outfilename = "medicalevents.csv"
outfile = open(outfilename, "w", encoding="utf-8")

for year in range(2016,2019):
    yearstring = str(year)
    for month in range(1,13):
        healthcount = 0
        if (month <10):
            monthstring = "0"+str(month)
        else:
            monthstring = str(month)
        for day in range(1,32):
            if (day < 10):
                daystring = "0"+str(day)
            else:
                daystring = str(day)

            datestring = yearstring + monthstring + daystring
            webURL = URLprefix + yearstring + '/'+ datestring + URLsuffix
            #print (webURL)

            try:
                infile = opener.open(webURL,timeout = 3)
                wholepage = infile.read().decode("utf-8")
            except:
                # print ('Page not found.')
                wholepage = ''

            targetstring = "35.3045(a)"
            
            lowerpage = wholepage.lower()
            stringfound = lowerpage.find(targetstring.lower())
            if (stringfound >=0):
                healthcount += lowerpage.count(targetstring.lower())
                print (datestring,"Medical Event Found.")
            healthstring = str(healthcount)
        print (yearstring+','+monthstring+','+healthstring+',', file = outfile)

print ()
print ("done.")
print ()

outfile.close()
        

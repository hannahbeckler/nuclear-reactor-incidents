import urllib.request
import http.cookiejar

##set up cookie opener
cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

search = input ("Give me a search phrase: ")
stringsearch = str(search)

URLprefix="https://www.nrc.gov/reading-rm/doc-collections/event-status/event/2017/2017"
URLsuffix="en.html"
outfilename = "output.txt"
outfile = open(outfilename, "w", encoding="utf-8")


for month in range(1,13):
    if (month <10):
        monthstring = "0"+str(month)
    else:
        monthstring = str(month)
    for day in range(1,32):
        if (day < 10):
            daystring = "0"+str(day)
        else:
            daystring = str(day)

        datestring = monthstring + daystring
        webURL = URLprefix + datestring + URLsuffix
        ##print (webURL)

        try:
            infile = opener.open(webURL, timeout=3)
            webpage = infile.read().decode("utf-8")
        except:
            ##print ('Page not found.')
            webpage = ''

        stringfound = webpage.find(stringsearch)

        if stringfound != -1:
            print (datestring+'2017',file = outfile)
            print (stringsearch,"found.")
   
print ()
print ("done.")

outfile.close()
        
    
    

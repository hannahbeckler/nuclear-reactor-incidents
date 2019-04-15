# nuclear-reactor-incidents

medicalevents.py is designed to snag meaningful nuclear reactor incident reports from www.nrc.gov . This web scraper locates the code "35.3045(a)" identifying a serious medical event involving nuclear materials and tallies the number of such events in each given month from 2016 to present. 

eventdetect.py is designed to search for specific incident codes or a specific nuclear reactor location from www.nrc.gov reports on nuclear reactor incidents within a year (right now 2017, but could easily be updated). The code then prints the date to screen when the incident report is found. Incident codes may be: "35.3045(a)" for a serious medical event; "Indian Point" is the closest nuclear power plant to New York City; M/R' and 'A/R', in which a reactor is "Scrammed" -- rapidly shut down -- either manually or automatically; "50.72(b)(1)" -- the most serious class of non-emergency problems.

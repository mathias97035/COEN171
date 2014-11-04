import json, httplib, time, datetime


requestData = {
        "Major" : "COEN",
        "APCredits" : { 
            "Calculus BC" : 4 
        },
        "IBCredits" : { 
            "Chemistry" : 6 
        },
        "NeedMath9" : False,
        "PreviousCodingExperience" : True,
        "TransferCredits" : [ 
            { 
                "subject" : "phys", 
                "course" : "31" 
            },
            { 
                "subject" : "coen", 
                "course" : "11" 
            }, 
            #{ 
            #    "subject" : "MATH", 
            #    "course" : "14" 
            #} 
        ]
    }

connection = httplib.HTTPConnection('students.engr.scu.edu', 80)
time.sleep(.1)
x = datetime.datetime.now()

connection.connect()
connection.request('POST', '/~achung1/coen174/projectNew.cgi', json.dumps(requestData), {})


response = connection.getresponse()
responseText = response.read()
print "Elapsed Time:", datetime.datetime.now() - x
print "Response Status: " + str(response.status)
try:
    print json.dumps(json.loads(responseText), indent=4)
except:
    print responseText


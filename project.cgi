#!/usr/bin/python
'''
Aaron Chung, Matt Bellisu, Nick Fong, Josh 

COEN 174 Lab

Schedule Creator 
Python CGI

'''

# Import modules for CGI handling 
import sys, json, ScheduleConfig, ScheduleFunctions

# Define paramaters to accept
JsonFormatDefinition = {
    "APCredits" : dict, 
    "Major" : str,
    "IBCredits" : dict,
    "TransferCredits" : list
}

# Display header as json response type
print "Content-type:application/json\r\n\r\n"

'''
Encase in try-except block
    Have Response handlers for except:
        raise KeyError for Missing Param
        raise ValueError for JSON Error
        raise AttributeError for Invalid Type
'''
try:

    # Get data from sys.stdin (data is sent in POST request)

    #requestData = json.load(sys.stdin)
    
    requestData = {
        "APCredits" : { "Calculus BC" : 4 },
        "Major" : "COEN",
        "IBCredits" : { "Chemistry (standard)" : 6 },
        "TransferCredits" : [ { "subject" : "MATH", "course" : "11" } ]
     }

    # Verify types in form are correct
    for key in JsonFormatDefinition:
        if not isinstance( requestData[key] , JsonFormatDefinition[key] ):
            raise AttributeError(key)

    # get starting schedule dictionary of dictionaries 
    try:
        #desiredMajor = "COEN"
        schedule = ScheduleConfig.STARTING_SCHEDULES[ requestData["Major"] ]
    except KeyError:
        raise Exception(desiredMajor + " is not a currently supported major.")

    for apClassRaw in requestData["APCredits"]:
        apClass = apClassRaw.lower().strip()
        try:
            apScore = int(requestData["APCredits"][apClassRaw])
        except:
            raise AttributeError("Score for " + apClassRaw + " is not interpretable as an int.")
        try:
            shiftingScheduleData = ScheduleConfig.AP_SCORE_CONFIG[ apClass ][ apScore ]
        except KeyError:
            continue # continue on iterating through APCredits

        #print shiftingScheduleData
        for quarter in shiftingScheduleData["remove"] :
            #print quarter
            for i, removeThisCourse in enumerate( shiftingScheduleData["remove"][quarter] ):
                for classInSchedule in schedule[quarter]:

                    if classInSchedule["subject"].lower().strip() == \
                        removeThisCourse["subject"].lower().strip() and \
                        classInSchedule["course"].lower().strip() == \
                        removeThisCourse["course"].lower().strip():
                        schedule[quarter][i] = shiftingScheduleData["add"][quarter][i] 
                        break
                        '''
                        print "    REPLACED", removeThisCourse["subject"], removeThisCourse["course"]
                        try:
                            print "    WITH", shiftingScheduleData["add"][quarter][i]["subject"], shiftingScheduleData["add"][quarter][i]["course"]
                        except:
                            print "    WITH WILDCARD"
                        '''

    # schedule = AP_SCORE_CONFIG

    # output response json
    
    print json.dumps({ 
        "error" : False , 
        "schedule" : schedule 
    }, indent=4)
    

# Error Handling Except Block
except AttributeError as e:
    print json.dumps({ "error" : "Invalid Type: " + str(e) })
except KeyError as e:
    print json.dumps({ "error" : "Missing Param: " + str(e) })
except ValueError as e:
    print json.dumps({ "error" : "JSON Error: " + str(e) })
except Exception as e:
    print json.dumps({ "error" : "Misc. Error: " + str(e) })


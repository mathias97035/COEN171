#!/usr/bin/python
'''
Aaron Chung, Matt Bellisu, Nick Fong, Paul Thurston 

COEN 174 Lab

Schedule Creator 
Python CGI

'''

# Import modules for CGI handling 

import sys, json, copy
#sys.path.insert(0, '/~achung1/coen174/')
import ScheduleConfigV2 as ScheduleConfig 

# Define paramaters to accept
JsonFormatDefinition = {
    "APCredits" : dict, 
    "Major" : basestring,
    "IBCredits" : dict,
    "TransferCredits" : list,
    "NeedMath9" : bool,
    "PreviousCodingExperience" : bool

}

def coursesAreSame( course1, course2 ):
    if course1 is None and course2 is None:
        return True
    try:
        return course1["subject"].lower().strip() == \
               course2["subject"].lower().strip() and \
               course1["course"].lower().strip() == \
               course2["course"].lower().strip()
    except:
        return False


def indexOfCourseFromCourseLine( removeThisCourse, courseLine ):
    removeThisIndex = None
    for j, course in enumerate(courseLine):
        #if course == removeThisCourse:
        if coursesAreSame( removeThisCourse,course):
            removeThisIndex = j
            break
    return removeThisIndex


# Display header as json response type
print "Content-type:application/json\r\n\r\n"

'''
Encase in try-except block
    Have Response handlers for except:
        raise KeyError for Missing Param
        raise ValueError for JSON Error
        raise AttributeError for Invalid Type
'''
#print "SUCCESS"
#exit()
try:

    #''' <-- uncomment the pound sign to test, i'm a genus! LOL

    # Get data from sys.stdin (data is sent in POST request)
    requestData = json.load(sys.stdin)

    ''' #hard code for time being
    requestData = {
        "Major" : "COEN",
        "APCredits" : { 
            "Calculus BC" : 4 ,
            #"computer science a" : 5
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
            #{ 
            #    u"subject" : u"math", 
            #    u"course" : "11" 
            #}, 
            #{ 
            #    "subject" : "MATH", 
            #    "course" : "12" 
            #} ,
            #{ 
            #    "subject" : "MATH", 
            #    "course" : "13" 
            #} ,
            #{ 
            #    "subject" : "MATH", 
            #    "course" : "14" 
            #} 
        ]
    }
    #'''

    # Verify types in form are correct
    for key in JsonFormatDefinition:
        if not isinstance( requestData[key] , JsonFormatDefinition[key] ):
            raise AttributeError(key)

    # get starting schedule lines 
    try:
        major = requestData["Major"].lower().strip()
        mutable_course_lines = ScheduleConfig.STARTING_SCHEDULE_LINES[major]["mutable"]
        immutable_course_lines = ScheduleConfig.STARTING_SCHEDULE_LINES[major]["immutable"]
    except KeyError:
        raise Exception(desiredMajor + " is not a currently supported major.")

    coursesSatisfied = requestData["TransferCredits"]
    
    if not requestData["NeedMath9"]:
        coursesSatisfied.append({"subject" : "MATH","course" : "9"})

    if requestData["PreviousCodingExperience"]:
        #since comp sci a is same thing
        #requestData["APCredits"].update( {"computer science a":3} )
        coursesSatisfied.append({"subject" : "COEN","course" : "10"})

    creditToScoreConfig = { 
        "APCredits" : ScheduleConfig.AP_SCORE_CONFIG,
        "IBCredits" : ScheduleConfig.IB_SCORE_CONFIG
    }

    for creditType in ["APCredits", "IBCredits"]:
        
        for creditClassNameRaw in sorted(requestData[creditType].keys(), reverse=True):
            creditClassName = creditClassNameRaw.lower().strip()

            try:
                creditClassScore = int(requestData[creditType][creditClassNameRaw])
            except:
                raise AttributeError("Score for " + creditClassNameRaw + " is not interpretable as an int.")
            
            try:
                coursesSatisfied.extend( creditToScoreConfig[creditType][ creditClassName ][ creditClassScore ] )
            except KeyError:
                continue # credit is not an accepted credit, continue on iterating through credits

    #remove from mutable class lines
    for removeThisCourse in coursesSatisfied:
        for i, courseLine in enumerate( mutable_course_lines ):
            removeThisIndex = indexOfCourseFromCourseLine( removeThisCourse, courseLine )
            if removeThisIndex is not None:
                mutable_course_lines[i].pop(removeThisIndex)
                break

    #remove from immutable class lines
    for removeThisCourse in coursesSatisfied:
        for i, courseLine in enumerate( immutable_course_lines ):
            nullifyThisIndex = indexOfCourseFromCourseLine( removeThisCourse, courseLine )
            if nullifyThisIndex is not None:
                immutable_course_lines[i][nullifyThisIndex] = None
                break

    schedule = {"fall":list(),"winter":list(),"spring":list()}
    for courseLineList in [immutable_course_lines, mutable_course_lines]:
        for courseLine in courseLineList:
            for i, quarter in enumerate(["fall", "winter", "spring"]):
                try:
                    schedule[quarter].append(courseLine[i])
                except:
                    pass # pass if len(courseLine) < 3

    #adding priority courses: C&I 
    try: 
        winterIndex = schedule["winter"].index(None)
        try:
            #try winter and spring first -> it might save room for modulo3 immutable classes
            springIndex = schedule["spring"].index(None)
            schedule["winter"][winterIndex] = { 
                        "subject" : "C&I",
                        "course" : "I",
                        "title" : "Cultures and Ideas I",
                        "hasLab" : False
                    }
            schedule["spring"][springIndex] = { 
                        "subject" : "C&I",
                        "course" : "II",
                        "title" : "Cultures and Ideas II",
                        "hasLab" : False
                    }
        except ValueError:
            fallIndex = schedule["fall"].index(None)
            schedule["fall"][fallIndex] = { 
                        "subject" : "C&I",
                        "course" : "I",
                        "title" : "Cultures and Ideas I",
                        "hasLab" : False
                    }
            schedule["winter"][winterIndex] = { 
                        "subject" : "C&I",
                        "course" : "II",
                        "title" : "Cultures and Ideas II",
                        "hasLab" : False
                    }
    except ValueError:
        pass

    #adding the modulo 3 courses 
    for courseLine in immutable_course_lines:
        length = len(courseLine)
        numStubs = int(length/3)
        remainder = length % 3
        if not numStubs:
            continue
        for i in xrange(numStubs):
            #if all three in this triplet stub are fulfilled for this immutable course list
            if tuple(courseLine[i*3:(i+1)*3]).count(None) == 3:
                #FOR EACH COURSE IN THE NEXT STUB, ADD IT IN
                rangeSize = remainder if i == numStubs - 1 else 3
                for j in xrange(rangeSize):
                    quarter = ("fall", "winter", "spring")[j]
                    for k in range( len(schedule[quarter])-1,-1,-1): #iterate backwards, fills in better
                        if schedule[quarter][k] is None:
                            schedule[quarter][k] = courseLine[((i+1)*3)+j]
                            break

    for quarter in ["fall", "winter", "spring"]:
        for i, course in enumerate(schedule[quarter]):
            if course is None:
                schedule[quarter][i] = { 
                    "subject" : "Core",
                    "course" : "",
                    "title" : "University Core",
                    "hasLab" : False
                }

    schedule["fall"].append({
                "subject" : "ENGR",
                "course" : "1",
                "title" :"Introduction to Engineering",
                "hasLab" : False
            })

    print json.dumps({ 
        "error" : False , 
        "schedule" : schedule
        #,"requestData" : requestData 
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


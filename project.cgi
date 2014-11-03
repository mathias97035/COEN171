#!/usr/bin/python
'''
Aaron Chung, Matt Bellisu, Nick Fong, Paul Thurston 

COEN 174 Lab

Schedule Creator 
Python CGI

'''

# Import modules for CGI handling 
import sys, json, copy, ScheduleConfig 

# Define paramaters to accept
JsonFormatDefinition = {
    "APCredits" : dict, 
    "Major" : str,
    "IBCredits" : dict,
    "TransferCredits" : list,
    "NeedMath9" : bool,
    "PreviousCodingExperience" : bool

}

def quarterWithMaxNones(noneIndicesInQuarter, ignoreQuarterList=[] ):

    quartersList = [x for x in ["fall", "winter", "spring"] if x not in ignoreQuarterList]
    maxQuarterNameList = list()
    maxQuarterLen = 0
    for quarter in quartersList:
        thisQuarterLen = len(noneIndicesInQuarter[quarter])
        if thisQuarterLen > maxQuarterLen :
            maxQuarterLen = thisQuarterLen
            maxQuarterNameList = [ quarter ]
        elif thisQuarterLen == maxQuarterLen:
            maxQuarterNameList.append(quarter)
    return maxQuarterNameList

'''
def addToDictOfSetsIfExists( theSet, subject , course ):
    #update the set of fulfilled classes
    try:
        theSet[ subject ].update([ course ])
    except KeyError:
        theSet[ subject ] = set()
        theSet[ subject ].update([ course ])
''' 

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
    
    #hard code for time being
    requestData = {
        "Major" : "COEN",
        "APCredits" : { 
            "Calculus BC" : 4 
        },
        "IBCredits" : { 
            #"chemistry" : 6 
        },
        "NeedMath9" : False,
        "PreviousCodingExperience" : True,
        "TransferCredits" : [ 
            { 
                "subject" : "MATH", 
                "course" : "13" 
            }, 
            { 
                "subject" : "MATH", 
                "course" : "14" 
            } 
        ]
     }

    # Verify types in form are correct
    for key in JsonFormatDefinition:
        if not isinstance( requestData[key] , JsonFormatDefinition[key] ):
            raise AttributeError(key)

    # get starting schedule dictionary of dictionaries 
    try:
        schedule = ScheduleConfig.STARTING_SCHEDULES[ requestData["Major"] ]
    except KeyError:
        raise Exception(desiredMajor + " is not a currently supported major.")


    #format: { subject : set( courses ) }
    fulfilledClasses = dict() 

    creditToScoreConfig = { 
        "APCredits" : ScheduleConfig.AP_SCORE_CONFIG,
        "IBCredits" : ScheduleConfig.IB_SCORE_CONFIG
    }


    if requestData["PreviousCodingExperience"]:
        requestData["APCredits"].update( {"computer science a":3} )
        pass


    for creditType in ["APCredits", "IBCredits"]:
        
        for creditClassNameRaw in requestData[creditType]:
            creditClassName = creditClassNameRaw.lower().strip()

            try:
                creditClassScore = int(requestData[creditType][creditClassNameRaw])
            except:
                raise AttributeError("Score for " + creditClassNameRaw + " is not interpretable as an int.")
            
            try:
                shiftingScheduleData = creditToScoreConfig[creditType][ creditClassName ][ creditClassScore ]
            except KeyError:
                continue # credit is not an accepted credit, continue on iterating through credits
            
            for quarter in shiftingScheduleData["remove"] :

                for i, removeThisClass in enumerate( shiftingScheduleData["remove"][quarter] ):


                    '''
                    If an AP class is fulfulled by an AP credit, but the class is not on the list 
                        Then the class should be added to the fulfulled class list
                        Our code does not currently guarantee an add to the list 
                        Our code only adds to the list if the class is removed.
                        *** We need to guarantee that the class will be added to the fulfilled class list.

                    '''

                    for j, classInSchedule in enumerate( schedule[quarter] ):

                        try:
                            subjectOfClassInSchedule = classInSchedule["subject"].lower().strip()
                            courseOfClassInSchedule = classInSchedule["course"].lower().strip()
                        except (AttributeError, TypeError) as e:
                            continue # classInSchedule is of type 'NoneType', pass

                        subjectOfClassToRemove = removeThisClass["subject"].lower().strip()
                        courseOfClassToRemove = removeThisClass["course"].lower().strip()

                        if subjectOfClassInSchedule == subjectOfClassToRemove and \
                           courseOfClassInSchedule == courseOfClassToRemove:

                            #update the set of fulfilled classes
                            try:
                                fulfilledClasses[ subjectOfClassInSchedule ].update([ courseOfClassInSchedule ])
                            except KeyError:
                                fulfilledClasses[ subjectOfClassInSchedule ] = set()
                                fulfilledClasses[ subjectOfClassInSchedule ].update([ courseOfClassInSchedule ])
                            
                            #add the replacement course to the schedule
                            schedule[quarter][j] = shiftingScheduleData["add"][quarter][i] 

                            #remove added class from set of fulfilled classes
                            try:
                                subjectOfAddedClass = schedule[quarter][i]["subject"].lower().strip()
                                courseOfAddedClass = schedule[quarter][i]["course"].lower().strip()
                                try:
                                    fulfilledClasses[ subjectOfAddedClass ].remove( courseOfAddedClass )
                                except Exception as e:
                                    pass
                            except TypeError:
                                pass # class is None
                            break
    
    for transferClass in requestData["TransferCredits"]:
        try:
            subjectOfClassToRemove = transferClass["subject"].lower().strip()
            courseOfClassToRemove = transferClass["course"].lower().strip()
        except:
            raise AttributeError( "A course in the 'TransferCredits' list is formated incorrectly.")
        
        for quarter in schedule:

            for i, classInSchedule in enumerate( schedule[quarter] ):

                try:
                    subjectOfClassInSchedule = classInSchedule["subject"].lower().strip()
                    courseOfClassInSchedule = classInSchedule["course"].lower().strip()
                except (AttributeError, TypeError) as e:
                    continue # classInSchedule is of type 'NoneType', pass

                if subjectOfClassInSchedule == subjectOfClassToRemove and \
                   courseOfClassInSchedule == courseOfClassToRemove:

                    #update the set of fulfilled classes
                    try:
                        fulfilledClasses[ subjectOfClassInSchedule ].update([ courseOfClassInSchedule ])
                    except KeyError:
                        fulfilledClasses[ subjectOfClassInSchedule ] = set()
                        fulfilledClasses[ subjectOfClassInSchedule ].update([ courseOfClassInSchedule ])
                    
                    #add the replacement course to the schedule
                    schedule[quarter][i] = None 
                    break


    '''
    ex:
        look at fall quarter
        count them as we fulfilled them in the fall quarter list



    '''

    if requestData["NeedMath9"]:
        if "11" not in fulfilledClasses["math"]:
            for quarter in ScheduleConfig.NEED_MATH_9:
                pass 
                ''' 
                ADD CODE HERE
                '''
        pass

    # Add Classes to None
    noneIndicesInQuarter = {}
    for quarter in schedule:
        noneIndicesInQuarter[quarter] = dict()
        noneIndicesInQuarter[quarter] = [i for i, x in enumerate(schedule[quarter]) if x == None]

    #print noneIndicesInQuarter
    #print fulfilledClasses
    print noneIndicesInQuarter
    print quarterWithMaxNones( noneIndicesInQuarter, ["spring"] )

    # C&I code

    #quarterToListOfClassesSatisfiedByThisQuarter 
    classesSatisfiedByThisQuarter = dict()
    classesSatisfiedByThisQuarter["fall"] = fulfilledClasses 
    classesSatisfiedByThisQuarter["winter"] = copy.deepcopy( fulfilledClasses )
    
    for aClass in schedule["fall"]:
        if aClass is None:
            continue
        subjectOfClass = aClass["subject"].lower().strip()
        courseOfClass = aClass["course"].lower().strip()
        try:
            classesSatisfiedByThisQuarter["winter"][ subjectOfClass ].update([ courseOfClass ])
        except KeyError:
            classesSatisfiedByThisQuarter["winter"][ subjectOfClass ] = set()
            classesSatisfiedByThisQuarter["winter"][ subjectOfClass ].update([ courseOfClass ])

    classesSatisfiedByThisQuarter["spring"] = copy.deepcopy( classesSatisfiedByThisQuarter["winter"] )

    for aClass in schedule["winter"]:
        if aClass is None:
            continue
        subjectOfClass = aClass["subject"].lower().strip()
        courseOfClass = aClass["course"].lower().strip()
        try:
            classesSatisfiedByThisQuarter["spring"][ subjectOfClass ].update([ courseOfClass ])
        except KeyError:
            classesSatisfiedByThisQuarter["spring"][ subjectOfClass ] = set()
            classesSatisfiedByThisQuarter["spring"][ subjectOfClass ].update([ courseOfClass ])


    print "***"
    print classesSatisfiedByThisQuarter
    print "***"


    if len(noneIndicesInQuarter["winter"]):
        if len(noneIndicesInQuarter["fall"]):
            try:
                if "i" not in fulfilledClasses["c&i"]:
                    CnI1Flag = True
                else:
                    CnI1Flag = False
                if "ii" not in fulfilledClasses["c&i"]:
                    CnI2Flag = True
                else:
                    CnI1Flag = False
            except KeyError:
                #c&i key not in fulfilled classes
                CnI1Flag = True
                CnI2Flag = True

            if CnI1Flag:
                fallIndexOfNone = noneIndicesInQuarter["fall"].pop()
                schedule["fall"][fallIndexOfNone] = { 
                    "subject" : "C&I",
                    "course" : "I",
                    "title" : "Cultures and Ideas I",
                    "hasLab" : False
                }
            if CnI2Flag:
                winterIndexOfNone = noneIndicesInQuarter["winter"].pop()
                schedule["winter"][winterIndexOfNone] =  { 
                    "subject" : "C&2",
                    "course" : "II",
                    "title" : "Cultures and Ideas II",
                    "hasLab" : False
                }

        elif len(noneIndicesInQuarter["spring"]):
            pass

    _ignoreQuarterList = ["fall"]
    for quarter in ["winter", "spring"]:
        try:
            if "13" in classesSatisfiedByThisQuarter[quarter]["math"]:
                freeQuarterList = quarterWithMaxNones( noneIndicesInQuarter, ignoreQuarterList=_ignoreQuarterList )
                if freeQuarterList:
                    freeQuarter = freeQuarterList[0]
                    index = noneIndicesInQuarter[freeQuarter].pop()
                    schedule[freeQuarter][index] = { 
                        "subject" : "MATH",
                        "course" : "53",
                        "title" : "Linear Algebra",
                        "hasLab" : False
                    }
                break
            else:
                _ignoreQuarterList.append(quarter)
        except KeyError: 
            pass

    _ignoreQuarterList = []
    for quarter in ["fall", "winter", "spring"]:
        try:
            if "33" in classesSatisfiedByThisQuarter[quarter]["phys"]:
                freeQuarterList = quarterWithMaxNones( noneIndicesInQuarter, ignoreQuarterList=_ignoreQuarterList )
                if freeQuarterList:
                    freeQuarter = freeQuarterList[0]
                    index = noneIndicesInQuarter[freeQuarter].pop()
                    schedule[freeQuarter][index] = { 
                        "subject" : "ELEN",
                        "course" : "50",
                        "title" : "Electric Circuits I",
                        "hasLab" : True
                    }
                break
            else:
                _ignoreQuarterList.append(quarter)
        except KeyError: 
            pass

    _ignoreQuarterList = ["fall", "winter"]
    for quarter in ["spring"]:
        try:
            if "12" in classesSatisfiedByThisQuarter[quarter]["coen"]:
                freeQuarterList = quarterWithMaxNones( noneIndicesInQuarter, ignoreQuarterList=_ignoreQuarterList )
                if freeQuarterList:
                    freeQuarter = freeQuarterList[0]
                    index = noneIndicesInQuarter[freeQuarter].pop()
                    schedule[freeQuarter][index] = { 
                        "subject" : "COEN",
                        "course" : "20",
                        "title" : "Embedded Systems",
                        "hasLab" : True
                    }
                break
            else:
                _ignoreQuarterList.append(quarter)
        except KeyError: 
            pass


    _ignoreQuarterList = []
    for quarter in ["fall", "winter", "spring"]:
        try:
            if "14" in classesSatisfiedByThisQuarter[quarter]["coen"]:
                freeQuarterList = quarterWithMaxNones( noneIndicesInQuarter, ignoreQuarterList=_ignoreQuarterList )
                if freeQuarterList:
                    freeQuarter = freeQuarterList[0]
                    index = noneIndicesInQuarter[freeQuarter].pop()
                    schedule[freeQuarter][index] = { 
                        "subject" : "AMTH",
                        "course" : "106",
                        "title" : "Differential Equations",
                        "hasLab" : True
                    }
                break
            else:
                _ignoreQuarterList.append(quarter)
        except KeyError: 
            pass

    #PRIORITY

    #C&I
    #Math13
    #physics33 
    #Math14
    #Coen20
    #amth 108 106

    for quarter in schedule:
        print quarter
        for thisClass in schedule[quarter]:
            print "    ",thisClass


    # output response json  
    #print json.dumps({ 
    #    "error" : False , 
    #    "schedule" : schedule 
    #}, indent=4)
    

# Error Handling Except Block
except AttributeError as e:
    print json.dumps({ "error" : "Invalid Type: " + str(e) })
except KeyError as e:
    print json.dumps({ "error" : "Missing Param: " + str(e) })
except ValueError as e:
    print json.dumps({ "error" : "JSON Error: " + str(e) })
except Exception as e:
    print json.dumps({ "error" : "Misc. Error: " + str(e) })


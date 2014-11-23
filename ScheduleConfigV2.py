import json
coursesSatisfied = ["math 9", "math 11", "chem 11", "phys 31", "phys 32", "coen 10", "coen 11"]

mutable_course_lines = [ 
    ["math 9", "math 11", "math 12", "math 13", "math 14"]
]

immutable_course_lines = [
    ["coen 10", "coen 11", "coen 12"],
    ["ctw 1", "ctw 2", "coen 19"],
    ["chem 11", "phys 31", "phys 32", "phys 33", "elen 50"]
]

'''
def coursesAreSame( course1, course2 ):
    return course1["subject"].lower().strip() == \
           course2["subject"].lower().strip() and \
           course1["course"].lower().strip() == \
           course2["course"].lower().strip()
'''

def indexOfCourseFromCourseLine( course, courseLine ):
    removeThisIndex = None
    for j, course in enumerate(courseLine):
        if course == removeThisCourse:
            removeThisIndex = j
            break
    return removeThisIndex

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
            schedule[quarter].append(courseLine[i])

#adding priority courses: C&I 
try: 
    winterIndex = schedule["winter"].index(None)
    try:
        #try winter and spring first -> it might save room for modulo3 immutable classes
        springIndex = schedule["spring"].index(None)
        schedule["winter"][winterIndex] = "C&I 1"
        schedule["spring"][springIndex] = "C&I 2"
    except ValueError:
        fallIndex = schedule["fall"].index(None)
        schedule["fall"][fallIndex] = "C&I 1"
        schedule["winter"][winterIndex] = "C&I 2"
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
                quarter = ("fall", "winter","spring")[j]
                for k in range( len(schedule[quarter])-1,-1,-1): #iterate backwards, fills in better
                    if schedule[quarter][k] is None:
                        schedule[quarter][k] = courseLine[((i+1)*3)+j]
                        break

for quarter in ["fall", "winter", "spring"]:
    for i, course in enumerate(schedule[quarter]):
        if course is None:
            schedule[quarter][i] = "core"

print json.dumps(schedule, indent=4)


'''
if (None, None, None) == tuple(immutable_course_lines[-1][:3]):
    print "holyshit"
'''


#add cni, ctw
#add any possible classes to mutable class line

#print mutable_class_lines






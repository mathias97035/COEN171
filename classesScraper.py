from bs4 import BeautifulSoup
import urllib2, re
url="http://www.scu.edu/engineering/cse/ugrad/bulletin.cfm"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
divTag = soup.find_all("div", {"id":"cs_control_2572213"} )
coenClasses = divTag[0].find_all("p")

listOfClasses = []
COENCourseToDict = {}

'''
entire outer list is AND
"co-requisites" : [
    
    /* list inside this list indicates an "or" */
    [   
        {
            "major" : "COEN", 
            "class" : "11",
        },
        {
            "major" : "CSCI",
            "class" : "60"
        }
    ],
    [
        {
            "major" : "COEN"
            "major" : "20"
        }
    ]
        
    
]

{
    "major" : "COEN"

    "class" : <str>,

    "co-requisites" : [
        [ ],
        [ ]
    ]
}

'''
for coenClassDOM in coenClasses:

    coenClass = {"major":"COEN", "course" : 0, "prerequisites":[],"corequisites":[] }
    titleAndNumberDOM = coenClassDOM.find_all("strong")[0]
    titleAndNumberResults = re.search('(.*)\.\s(.*)', titleAndNumberDOM.text)

    if titleAndNumberResults is None:
        continue

    coenClass["course"] = titleAndNumberResults.group(1).encode("utf-8")
    coenClass["title"] = titleAndNumberResults.group(2).encode("utf-8")

    # find prerequesites
    prereq = re.search('Prerequisite[s]*:(.*)\.', coenClassDOM.text)
    if prereq:
        if " and " in prereq.group(1).strip():
            andTokens = prereq.group(1).strip().encode("utf-8").split(" and ")
            removeTheCommas = andTokens[0].split(",")
            removeTheCommas.append(andTokens[-1])
            andTokens = removeTheCommas
        else:
            andTokens = [ prereq.group(1).strip().encode("utf-8") ]

        #remove period from sentence
        if "." in andTokens[-1]:
            andTokens[-1] = andTokens[-1][:andTokens[-1].find(".")]
        #print andTokens
        for andToken in andTokens:
            orTokens = re.findall('[A-Z]{4}\s[0-9Ll]{1,4}', andToken)

            orClassList = []
            for orToken in orTokens:
                prereqClassTokens = orToken.split()
                orClassList.append({"major" : prereqClassTokens[0], 
                                    "course" : prereqClassTokens[1] })

            coenClass["prerequisites"].append(orClassList)

    # find prerequesites
    coreq = re.search('Co-requisite[s]*:(.*)\.', coenClassDOM.text)
    if coreq:
        if " and " in coreq.group(1).strip():
            andTokens = coreq.group(1).strip().encode("utf-8").split(" and ")
            removeTheCommas = andTokens[0].split(",")
            removeTheCommas.append(andTokens[-1])
            andTokens = removeTheCommas
        else:
            andTokens = [ coreq.group(1).strip().encode("utf-8") ]
        #remove period from sentence
        if "." in andTokens[-1]:
            andTokens[-1] = andTokens[-1][:andTokens[-1].find(".")]
        #print andTokens
        for andToken in andTokens:
            orTokens = re.findall('[A-Z]{4}\s[0-9Ll]{1,4}', andToken)

            orClassList = []
            for orToken in orTokens:
                coreqClassTokens = orToken.split()
                orClassList.append({"major" : coreqClassTokens[0], 
                                    "course" : coreqClassTokens[1] })

            coenClass["corequisites"].append(orClassList)
    listOfClasses.append(coenClass)
    COENCourseToDict[coenClass["course"]] = coenClass

#print COENCourseToDict["145"]
import json
print json.dumps(COENCourseToDict , indent=4)

'''
import pickle

# write python dict to a file
output = open('coenClassDict.pkl', 'wb')
pickle.dump(COENCourseToDict, output)
output.close()
'''

exit()

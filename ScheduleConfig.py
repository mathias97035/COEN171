

STARTING_SCHEDULES = {
    "COEN" : { 
        "fall" : [
            {
                "subject" : "COEN",
                "course" : "10",
                "title" : "Introduction To Programming",
                "hasLab" : True
            },
            {
                "subject" : "University Core",
                "course" : None,
                "title" :"Critial Thinking and Writing I",
                "hasLab" : False
            } ,
            {
                "subject" : "MATH",
                "course" : "11",
                "title" :"Calculus I",
                "hasLab" : False
            },
            {
                "subject" : "CHEM",
                "course" : "11",
                "title" : "Introduction to Programming",
                "hasLab" : True
            } ,
            {
                "subject" : "ENGR",
                "course" : "1",
                "title" :"Introduction to Engineering",
                "hasLab" : False
            }
        ],
        "winter" : [

        ],
        "spring" : [

        ]
    }
}


# None means wild card
AP_SCORE_CONFIG = {
    "calculus bc" : {
        3 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "MATH",
                        "course" : "11"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "12"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "13"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    {
                        "subject" : "MATH",
                        "course" : "12"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "13"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "14"
                    }
                ]
            }
        },
        4 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "MATH",
                        "course" : "11"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "12"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "13"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    {
                        "subject" : "MATH",
                        "course" : "13"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "14"
                    }
                ],
                "spring" : [
                    None
                ]
            }
        },
        5 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "MATH",
                        "course" : "11"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "12"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "13"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    {
                        "subject" : "MATH",
                        "course" : "13"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "14"
                    }
                ],
                "spring" : [
                    None
                ]
            }
        }
    }
}

# minimumScore and maximumScore @ -1 means N/A
IB_SCORE_CONFIG = {

}


REQUIRED_CLASSES = {
    "COEN" : [
            {
                "classInfo" : {
                        "subject" : "ENGR",
                        "course" : "1",
                        "name" : "asdasdasda"
                        "hasLab" : False
                    },
                "quartersOffered" : [
                    "fall", "winter", "spring"
                ]
            }    
        ]
}


'''
Dictionary: Key-Value pairs

SCU_MAJORS = {
        "COEN" : {
            <course_num> : {
                "quarters" : [
                        <quarter>,
                        <quarter>,
                        ...
                    ] , 
                "prereq" : [
                        ["COEN 50"],
                        ["ELEN 33", "COEN 100"]

                    ]
            }
        }
    }

'''

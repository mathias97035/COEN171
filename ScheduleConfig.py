

STARTING_SCHEDULES = {
    "COEN" : { 
        "fall" : [
                {
                    "subject" : "COEN",
                    "course" : "10",
                    "title" : "Introduction To Programming"
                },
                {
                    "subject" : "COEN",
                    "course" : "10L",
                    "title" : "Introduction To Programming"
                }, 
                {
                    "subject" : "CTW",
                    "course" : "1",
                    "title" :"Introduction To Programming"
                } ,
                {
                    "subject" : "MATH",
                    "course" : "11",
                    "name" :"Introduction To Programming"
                },
                {
                    "subject" : "CHEM",
                    "course" : "11",
                    "name" :"Introduction To Programming"
                } , 
                {
                    "subject" : "CHEM",
                    "course" : "11L",
                    "name" :"Introduction To Programming"
                },
                {
                    "subject" : "ENGR",
                    "course" : "1",
                    "name" :"Introduction To Programming"
                }
            ],

        "winter" : [

            ],
        "spring" : [

            ]
        }
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

SCU_MAJORS = {
    
    "ELEN" : {
        "50"
    },

    "COEN" : {

        "174L": {
            "prerequisites": [], 
            "course": "174L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "174", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 174"
        }, 
        "150": {
            "prerequisites": [
                []
            ], 
            "course": "150", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Introduction to Information Security"
        }, 
        "152": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ], 
                [
                    {
                        "course": "20", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "152", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "152L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Computer Forensics"
        }, 
        "199": {
            "prerequisites": [], 
            "course": "199", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Directed Research/Reading"
        }, 
        "145L": {
            "prerequisites": [], 
            "course": "145L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "145", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 145"
        }, 
        "194": {
            "prerequisites": [], 
            "course": "194", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Design Project I"
        }, 
        "127": {
            "prerequisites": [
                [
                    {
                        "course": "21", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "127L", 
                        "major": "COEN"
                    }
                ], 
                [
                    {
                        "course": "115", 
                        "major": "ELEN"
                    }
                ]
            ], 
            "course": "127", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "127L", 
                        "major": "COEN"
                    }
                ], 
                [
                    {
                        "course": "115", 
                        "major": "ELEN"
                    }
                ]
            ], 
            "title": "Advanced Logic Design"
        }, 
        "193": {
            "prerequisites": [], 
            "course": "193", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Undergraduate Research"
        }, 
        "172L": {
            "prerequisites": [], 
            "course": "172L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "172", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 172"
        }, 
        "175L": {
            "prerequisites": [], 
            "course": "175L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "175", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 175"
        }, 
        "160L": {
            "prerequisites": [], 
            "course": "160L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "160", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 160"
        }, 
        "179": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ], 
                [
                    {
                        "course": "19", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "51", 
                        "major": "MATH"
                    }
                ]
            ], 
            "course": "179", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Theory of Algorithms"
        }, 
        "129": {
            "prerequisites": [], 
            "course": "129", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Current Topics in Computer Science and Engineering"
        }, 
        "177": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ], 
                [
                    {
                        "course": "20", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "177", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "177L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Operating Systems"
        }, 
        "164L": {
            "prerequisites": [], 
            "course": "164L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "164", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 164"
        }, 
        "175": {
            "prerequisites": [
                [
                    {
                        "course": "20", 
                        "major": "COEN"
                    }
                ], 
                [
                    {
                        "course": "70", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "175", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "175L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Formal Language Theory and Compiler Construction"
        }, 
        "174": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "174", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "174L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Software Engineering"
        }, 
        "173": {
            "prerequisites": [
                [
                    {
                        "course": "70", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ], 
                [
                    {
                        "course": "19", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "51", 
                        "major": "MATH"
                    }
                ]
            ], 
            "course": "173", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Logic Programming"
        }, 
        "172": {
            "prerequisites": [
                [
                    {
                        "course": "19", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "51", 
                        "major": "MATH"
                    }, 
                    {
                        "course": "70", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "172", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Structure and Interpretation of Computer Programs"
        }, 
        "165": {
            "prerequisites": [
                [
                    {
                        "course": "14", 
                        "major": "MATH"
                    }, 
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "165", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Introduction to 3D Animation & Modeling/Modeling & Control of Rigid Body Dynamics"
        }, 
        "60L (NEW)": {
            "prerequisites": [], 
            "course": "60L (NEW)", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "60", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 60"
        }, 
        "177L": {
            "prerequisites": [], 
            "course": "177L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "177", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 177"
        }, 
        "20": {
            "prerequisites": [
                [
                    {
                        "course": "11", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "60", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "20", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "20L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Embedded Systems"
        }, 
        "21": {
            "prerequisites": [], 
            "course": "21", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "21L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Logic Design"
        }, 
        "10L": {
            "prerequisites": [], 
            "course": "10L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "10", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 10"
        }, 
        "163L": {
            "prerequisites": [], 
            "course": "163L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "163", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 163"
        }, 
        "44": {
            "prerequisites": [
                [
                    {
                        "course": "13", 
                        "major": "MATH"
                    }
                ]
            ], 
            "course": "44", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "44L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Applied Programming"
        }, 
        "45": {
            "prerequisites": [
                [
                    {
                        "course": "13", 
                        "major": "MATH"
                    }
                ]
            ], 
            "course": "45", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "45L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Applied Programming in MATLAB"
        }, 
        "12L": {
            "prerequisites": [], 
            "course": "12L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 12"
        }, 
        "29": {
            "prerequisites": [], 
            "course": "29", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Current Topics in Computer Science and Engineering"
        }, 
        "178": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "178", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "178L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Database Systems"
        }, 
        "180": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "180", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Introduction to Information Storage"
        }, 
        "127L": {
            "prerequisites": [], 
            "course": "127L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "127", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Advanced Logic Design Laboratory"
        }, 
        "171": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "171", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Principles of Design and Implementation of Programming Languages"
        }, 
        "44L": {
            "prerequisites": [], 
            "course": "44L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "44", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 44"
        }, 
        "178L": {
            "prerequisites": [], 
            "course": "178L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "178", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 178"
        }, 
        "188": {
            "prerequisites": [], 
            "course": "188", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Co-op Education"
        }, 
        "189": {
            "prerequisites": [], 
            "course": "189", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Co-op Technical Report"
        }, 
        "20L": {
            "prerequisites": [], 
            "course": "20L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "20", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Embedded Systems Laboratory"
        }, 
        "196": {
            "prerequisites": [
                [
                    {
                        "course": "195", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "196", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Design Project III"
        }, 
        "146": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "146", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "146L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Computer Networks"
        }, 
        "146L": {
            "prerequisites": [], 
            "course": "146L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "146", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 146"
        }, 
        "145": {
            "prerequisites": [
                [
                    {
                        "course": "11", 
                        "major": "COEN"
                    }
                ], 
                []
            ], 
            "course": "145", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "145L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Parallel Programming"
        }, 
        "152L": {
            "prerequisites": [], 
            "course": "152L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "152", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 152"
        }, 
        "148": {
            "prerequisites": [
                [
                    {
                        "course": "53", 
                        "major": "MATH"
                    }, 
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "148", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "148L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Computer Graphics Systems"
        }, 
        "120": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "120", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "120L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Real-Time Systems"
        }, 
        "122": {
            "prerequisites": [
                [
                    {
                        "course": "20", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "33", 
                        "major": "ELEN"
                    }
                ], 
                [
                    {
                        "course": "21", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "21", 
                        "major": "ELEN"
                    }
                ]
            ], 
            "course": "122", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "122L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Computer Architecture"
        }, 
        "168": {
            "prerequisites": [
                [
                    {
                        "course": "20", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "70", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "168", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Mobile Application Development"
        }, 
        "173L": {
            "prerequisites": [], 
            "course": "173L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "173", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 173"
        }, 
        "70": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ], 
                [
                    {
                        "course": "19", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "51", 
                        "major": "MATH"
                    }
                ]
            ], 
            "course": "70", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "70L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Formal Specification and Advanced Data Structures"
        }, 
        "164": {
            "prerequisites": [
                [
                    {
                        "course": "161", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "164", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "164L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Web Programming II"
        }, 
        "60 (NEW)": {
            "prerequisites": [], 
            "course": "60 (NEW)", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "60L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Web Technologies"
        }, 
        "166": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ], 
                [
                    {
                        "course": "19", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "51", 
                        "major": "MATH"
                    }
                ]
            ], 
            "course": "166", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Artificial Intelligence"
        }, 
        "160": {
            "prerequisites": [
                [
                    {
                        "course": "70", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "160", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "160L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Object-Oriented Analysis, Design, and Programming"
        }, 
        "161": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "161", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "161L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Web Programming I"
        }, 
        "162": {
            "prerequisites": [
                [
                    {
                        "course": "146", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "162", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Web Infrastructure"
        }, 
        "163": {
            "prerequisites": [
                [
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "163", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "163L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Web Usability"
        }, 
        "11": {
            "prerequisites": [
                [
                    {
                        "course": "10", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "10", 
                        "major": "CSCI"
                    }, 
                    {
                        "course": "30", 
                        "major": "OMIS"
                    }
                ]
            ], 
            "course": "11", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "11L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Advanced Programming"
        }, 
        "10": {
            "prerequisites": [], 
            "course": "10", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "10L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Introduction to Programming"
        }, 
        "12": {
            "prerequisites": [
                [
                    {
                        "course": "11", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "44", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "12", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "12L", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Abstract Data Types and Data Structures"
        }, 
        "169 (NEW)": {
            "prerequisites": [
                [
                    {
                        "course": "108", 
                        "major": "AMTH"
                    }, 
                    {
                        "course": "122", 
                        "major": "MATH"
                    }, 
                    {
                        "course": "12", 
                        "major": "COEN"
                    }, 
                    {
                        "course": "61", 
                        "major": "CSCI"
                    }
                ]
            ], 
            "course": "169 (NEW)", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Web Information Management"
        }, 
        "195": {
            "prerequisites": [
                [
                    {
                        "course": "194", 
                        "major": "COEN"
                    }
                ]
            ], 
            "course": "195", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Design Project II"
        }, 
        "19": {
            "prerequisites": [], 
            "course": "19", 
            "major": "COEN", 
            "corequisites": [], 
            "title": "Discrete Mathematics"
        }, 
        "11L": {
            "prerequisites": [], 
            "course": "11L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "11", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 11"
        }, 
        "161L": {
            "prerequisites": [], 
            "course": "161L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "161", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 161"
        }, 
        "148L": {
            "prerequisites": [], 
            "course": "148L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "148", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 148"
        }, 
        "70L": {
            "prerequisites": [], 
            "course": "70L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "70", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 70"
        }, 
        "120L": {
            "prerequisites": [], 
            "course": "120L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "120", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Real-Time Systems Laboratory"
        }, 
        "45L": {
            "prerequisites": [], 
            "course": "45L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "45", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 45"
        }, 
        "21L": {
            "prerequisites": [], 
            "course": "21L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "21", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Logic Design Laboratory"
        }, 
        "122L": {
            "prerequisites": [], 
            "course": "122L", 
            "major": "COEN", 
            "corequisites": [
                [
                    {
                        "course": "122", 
                        "major": "COEN"
                    }
                ]
            ], 
            "title": "Laboratory for COEN 122"
        }
    }
}
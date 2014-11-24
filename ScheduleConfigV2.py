'''
first three indexes of each course line represent quarters

line[0] -> fall quarter
line[1] -> winter quarter
line[2] -> spring quarter
'''

STARTING_SCHEDULE_LINES = {
    "coen" : {
        "mutable" : [
            [
                {
                    "subject" : "MATH",
                    "course" : "9",
                    "title" :"Pre-Calculus",
                    "hasLab" : False
                },
                {
                    "subject" : "MATH",
                    "course" : "11",
                    "title" :"Calculus I",
                    "hasLab" : False
                },
                {
                    "subject" : "MATH",
                    "course" : "12",
                    "title" :"Calculus II",
                    "hasLab" : False
                },
                {
                    "subject" : "MATH",
                    "course" : "13",
                    "title" :"Calculus III",
                    "hasLab" : False
                },
                {
                    "subject" : "MATH",
                    "course" : "14",
                    "title" :"Calculus IV",
                    "hasLab" : False
                },
                {
                    "subject" : "AMTH",
                    "course" : "106",
                    "title" :"Differential Equations",
                    "hasLab" : False
                },
                {
                    "subject" : "AMTH",
                    "course" : "108",
                    "title" :"Probability and Statistics",
                    "hasLab" : False
                },        
                {
                    "subject" : "MATH",
                    "course" : "53",
                    "title" :"Linear Algebra",
                    "hasLab" : False
                }
            ] 
        ],
        "immutable" : [
            [            
                {
                    "subject" : "COEN",
                    "course" : "10",
                    "title" : "Introduction To Programming",
                    "hasLab" : True
                },                
                {
                    "subject" : "COEN",
                    "course" : "11",
                    "title" : "Advanced Programming",
                    "hasLab" : True
                },                 
                {
                    "subject" : "COEN",
                    "course" : "12",
                    "title" : "Data Structures",
                    "hasLab" : True
                }
            ],
            [            
                {
                    "subject" : "CTW",
                    "course" : "I",
                    "title" :"Critical Thinking and Writing I",
                    "hasLab" : False
                },                
                {
                    "subject" : "CTW",
                    "course" : "II",
                    "title" :"Critical Thinking and Writing II",
                    "hasLab" : False
                },                 
                {
                    "subject" : "COEN",
                    "course" : "19",
                    "title" : "Discrete Mathmatics",
                    "hasLab" : False
                }
            ],
            [
                {
                    "subject" : "CHEM",
                    "course" : "11",
                    "title" : "Chemistry I",
                    "hasLab" : True
                }, 
                {
                    "subject" : "PHYS",
                    "course" : "31",
                    "title" : "Physics I",
                    "hasLab" : True
                }, 
                {
                    "subject" : "PHYS",
                    "course" : "32",
                    "title" :"Physics II",
                    "hasLab" : True
                }, 
                {
                    "subject" : "PHYS",
                    "course" : "33",
                    "title" : "Physics III",
                    "hasLab" : True
                }, 
                {
                    "subject" : "ELEN",
                    "course" : "50",
                    "title" : "Electric Circuits I",
                    "hasLab" : True
                } 
            ]

        ]
    }
}

# None means wild card
AP_SCORE_CONFIG = {
    "calculus ab" : {
        4 : [
                {
                    "subject" : "MATH",
                    "course" : "11"
                }
        ],
        5 : [
                {
                    "subject" : "MATH",
                    "course" : "11"
                }
        ]
    },

    "calculus bc" : {
        3 : [
                {
                    "subject" : "MATH",
                    "course" : "11"
                }
        ],
        4 : [
                {
                    "subject" : "MATH",
                    "course" : "11"
                }
                ,
                {
                    "subject" : "MATH",
                    "course" : "12"
                }
        ],
        5 : [
                {
                    "subject" : "MATH",
                    "course" : "11"
                }
                ,
                {
                    "subject" : "MATH",
                    "course" : "12"
                }
        ]
        
    },

    "physics c: mechanics" : {
        4 : [
                {
                    "subject" : "PHYS",
                    "course" : "31",
                }
        ],
        5 : [
                {
                    "subject" : "PHYS",
                    "course" : "31"
                }
        ]
    },

 "physics c: electricity and magnetism" : {
        4 : [
                {
                    "subject" : "PHYS",
                    "course" : "33"
                }
        ],
        5 : [
                {
                    "subject" : "PHYS",
                    "course" : "33"
                }
        ]
    },


    "computer science a" : {
        3 : [
                {
                    "subject" : "COEN",
                    "course" : "10"
                }
        ],
        4 : [
                {
                    "subject" : "COEN",
                    "course" : "10"
                },
                {
                    "subject" : "COEN",
                    "course" : "11"
                }
        ],
        5 : [
                {
                    "subject" : "COEN",
                    "course" : "10"
                },
                {
                    "subject" : "COEN",
                    "course" : "11"
                }
        ]
  
    },

    "chemistry" : {
        3 : [
                {
                    "subject" : "CHEM",
                    "course" : "11"
                }
        ],
        4 : [
                {
                    "subject" : "CHEM",
                    "course" : "11"
                }
        ],
        5 : [
                {
                    "subject" : "CHEM",
                    "course" : "11"
                }
        ]
    }
}

IB_SCORE_CONFIG = {
    "chemistry" : {
        6 : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
        ],
        7 : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
        ]
    },

    "computer science" : {
        6 : [
                    {
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ,
                
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
        ],
        7 : [
                    {
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ,
                
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
        ]
    }
}


'''
if (None, None, None) == tuple(immutable_course_lines[-1][:3]):
    print "holyshit"
'''






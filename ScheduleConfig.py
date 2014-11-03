

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
        {
                "subject" : "COEN",
                "course" : "11",
                "title" : "Advance Programming",
                "hasLab" : False
            },
            {
                "subject" : "University Core",
                "course" : None,
                "title" :"Critial Thinking and Writing II",
                "hasLab" : False
            } ,
            {
                "subject" : "MATH",
                "course" : "12",
                "title" :"Calculus II",
                "hasLab" : False
            },
            {
                "subject" : "PHYS",
                "course" : "31",
                "title" : "Physics I",
                "hasLab" : True
            } 

        ],
        "spring" : [
        {
                "subject" : "COEN",
                "course" : "12",
                "title" : "Data Structures",
                "hasLab" : True
            },
            {
                "subject" : "MATH",
                "course" : "19",
                "title" :"Discrete Math",
                "hasLab" : False
            } ,
            {
                "subject" : "PHYS",
                "course" : "32",
                "title" :"Physics II",
                "hasLab" : True
            },
            {
                "subject" : "MATH",
                "course" : "13",
                "title" : "Calculus III",
                "hasLab" : False
            } 

        ]
    }
}


# None means wild card
AP_SCORE_CONFIG = {
    "calculus ab" : {
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
                        "course" : "12",
                        "title" :"Calculus II",
                        "hasLab" : False
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "13",
                        "title" :"Calculus III",
                        "hasLab" : False
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "14",
                        "title" :"Calculus IV",
                        "hasLab" : False
                    }
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
                        "course" : "12",
                        "title" :"Calculus II",
                        "hasLab" : False
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "13",
                        "title" :"Calculus III",
                        "hasLab" : False
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "14",
                        "title" :"Calculus IV",
                        "hasLab" : False
                    }
                ]
            }
        }
    },

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
                        "course" : "12",
                        "title" :"Calculus II",
                        "hasLab" : False
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "13",
                        "title" :"Calculus III",
                        "hasLab" : False
                    }
                ],
                "spring" : [
                    {
                        "subject" : "MATH",
                        "course" : "14",
                        "title" :"Calculus IV",
                        "hasLab" : False
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
                        "course" : "13",
                        "title" :"Calculus III",
                        "hasLab" : False
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "14",
                        "title" :"Calculus IV",
                        "hasLab" : False
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
                        "course" : "13",
                        "title" :"Calculus III",
                        "hasLab" : False
                    }
                ],
                "winter" :[
                    {
                        "subject" : "MATH",
                        "course" : "14",
                        "title" :"Calculus IV",
                        "hasLab" : False
                    }
                ],
                "spring" : [
                    None
                ]
            }
        }
    },

    "Physics C: Mechanics" : {
        4 : {
            "remove" : {
                "winter" :[
                    {
                        "subject" : "PHYS",
                        "course" : "31",
                    }
                ]
            },
          "add" : {
                "winter" :[
                        None
                ]
            }  
        },
        5 : {
            "remove" : {
                "winter" :[
                    {
                        "subject" : "PHYS",
                        "course" : "31"
                    }
                ]
            },
          "add" : {
                "winter" :[
                        None
                ]
            }
        }
    },

 "Physics C: Electricity & Magnetism" : {
        4 : {
            "remove" : {
                "spring" :[
                    {
                        "subject" : "PHYS",
                        "course" : "33"
                    }
                ]
            },
          "add" : {
                "spring" :[
                        None
                ]
            }  
        },
        5 : {
            "remove" : {
                "spring" :[
                    {
                        "subject" : "PHYS",
                        "course" : "33"
                    }
                ]
            },
          "add" : {
                "spring" :[
                        None
                ]
            }
        }
    },


    "computer science a" : {
        3 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "COEN",
                        "course" : "12"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    {
                        "subject" : "COEN",
                        "course" : "11",
                        "title" :"Advance Programming",
                        "hasLab" : True
                    }
                ],
                "winter" :[
                    {
                        "subject" : "COEN",
                        "course" : "12",
                        "title" :"Data Structures",
                        "hasLab" : True
                    }
                ],
                "spring" : [
                    None
                ]
            }
        },
        4 : {
            "remove" : {
                 "fall" : [
                    {
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "COEN",
                        "course" : "12"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    {
                        "subject" : "COEN 12",
                        "course" : "12",
                        "title" :"Data Structures",
                        "hasLab" : True
                    }
                ],
                "winter" :[
                    None
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
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "COEN",
                        "course" : "12"
                    }
                ]
            },
            "add" : {
                 "fall" : [
                    {
                        "subject" : "COEN 12",
                        "course" : "12",
                        "title" :"Data Structures",
                        "hasLab" : True
                    }
                ],
                "winter" :[
                    None
                ],
                "spring" : [
                    None
                ]
            }
        }
    },

    "chemistry" : {
        3 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    None
                ]
            }
        },
        4 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    None
                ]
            }
        },
        5 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    None
                ]
            }
        }
    }
}

# minimumScore and maximumScore @ -1 means N/A
IB_SCORE_CONFIG = {
"chemistry" : {
        6 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    None
                ]
            }
        },
        7 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "CHEM",
                        "course" : "11"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    None
                ]
            }
        }
    },

    "computer science" : {
        6 : {
            "remove" : {
                 "fall" : [
                    {
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "COEN",
                        "course" : "12"
                    }
                ]
            },
            "add" : {
                "fall" : [
                    {
                        "subject" : "COEN 12",
                        "course" : "12",
                        "title" :"Data Structures",
                        "hasLab" : True
                    }
                ],
                "winter" :[
                    None
                ],
                "spring" : [
                    None
                ]
            }
        },
        7 : {
            "remove" : {
                "fall" : [
                    {
                        "subject" : "COEN",
                        "course" : "10"
                    }
                ],
                "winter" :[
                    {
                        "subject" : "COEN",
                        "course" : "11"
                    }
                ],
                "spring" : [
                    {
                        "subject" : "COEN",
                        "course" : "12"
                    }
                ]
            },
            "add" : {
                 "fall" : [
                    {
                        "subject" : "COEN 12",
                        "course" : "12",
                        "title" :"Data Structures",
                        "hasLab" : True
                    }
                ],
                "winter" :[
                    None
                ],
                "spring" : [
                    None
                ]
            }
        }
    }
}


REQUIRED_CLASSES = {
    "COEN" : [
            {
                "classInfo" : {
                        "subject" : "ENGR",
                        "course" : "1",
                        "name" : "asdasdasda",
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

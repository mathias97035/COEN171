#!/usr/bin/python
'''
Aaron Chung, Matt Bellisu, Nick Fong, Josh 

COEN 174 Lab

Schedule Creator 
Python CGI

'''

# Import modules for CGI handling 
import sys, json, ScheduleConfig

# Define paramaters to accept
JsonFormatDefinition = {
	"apCredits" : dict, 
	"major" : str,
	"transferCredits" : dict 
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
	requestData = json.load(sys.stdin)

	# Verify types in form are correct
	for key in JsonFormatDefinition:
		if not isinstance( requestData[key] , JsonFormatDefinition[key] ):
			raise AttributeError(key)

	# get starting schedule dictionary of dictionaries 
	try:
		desiredMajor = "COEN"
		schedule = ScheduleConfig.STARTING_SCHEDULES[desiredMajor]
	except KeyError:
		raise Exception(desiredMajor + " is not a currently supported major.")

	# define notifications list
	notifications = []

	listOfCorusesAlreadySatisfied = []
	# from ap credits and transfer units, we generate a list of courses already satisified

	# remove courses satisfied from starting schedule

	# reposition and add more classes
	#Matt Was here
	# output response json
	print json.dumps({ 
		"error" : False , 
		"request_data" : requestData ,
		"schedule" : schedule ,
		"notifications" : notifications
	})

# Error Handling Except Block
except AttributeError as e:
	print json.dumps({ "error" : "Invalid Type: " + str(e) })
except KeyError as e:
	print json.dumps({ "error" : "Missing Param: " + str(e) })
except ValueError as e:
	print json.dumps({ "error" : "JSON Error: " + str(e) })
except Exception as e:
	print json.dumps({ "error" : "Misc. Error: " + str(e) })


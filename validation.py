#!/usr/bin/env python3

# INFO
# This programm aims at checking json objects ... that are part of a openscience
# community project list.

# StringLang
# Is an object that contains a 'txt' and 'lng' field.
def check_stringlang(obj):
	# check that <obj> is of type 'dict'
	if type(obj) != type(dict()):
		raise Exception("Expected an object not a "+str(type(obj))+"; got: "+str(obj))
	# check field keys
	kWant = sorted(["lng", "txt"])
	kHave = sorted(list(set(obj.keys())))
	if len(set(kWant).difference(set(kHave))) != 0:
		raise Exception( "Expected to find field keys: "+str(kWant) )

	# check field values
	for field in obj:
		if type(obj[field]) != type(str()):
			raise Exception("Expected all fields to contain string values")

# Validates a {List} to contain only {stringlang} objects and
# has only a single entry for each language.
def check_uniq_list_stringlang(obj, uniq=True):
	# check that <obj> is of type 'list'
	if type(obj) != type(list()):
		raise Exception("Expected a list; got "+ str(type(obj)))
	#check that each entry contains a valid {stringlang} object
	for item in obj:
		check_stringlang(item)
	# check unique
	if uniq == True:
		langs = {}
		for item in obj:
			if "lng" in item:
				if item["lng"] in langs:
					raise Exception("Found multiple items where key 'lng' (language) contains '"+ str(item["lng"]) +"' in list"+ str(obj))
				else:
					langs[item["lng"]] = True
			else:
				raise Exception("Expected to find field 'lng' in "+ str(item))



if __name__ == "__main__":
	try:
		print("main")
		check_stringlang( {"lng": "", "txt": ""} )
		check_uniq_list_stringlang(
			[
				{"lng": "ENG", "txt": ""},
				{"lng": "ENG", "txt": ""},
			]
		, uniq=True)
	except Exception as e:
		print(e)

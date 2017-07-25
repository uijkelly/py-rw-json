# Jessica A Kelly
#
# Just a simple program that reads a JSON file, does a transformation on a
# variable and writes back a new item to the JSON file
#
# 20 July 2017

import json
import pprint

# Read JSON file
with open('ex_form_json.json') as data_file:
    jdata = json.load(data_file)

pprint.pprint(jdata) #print it out "pretty"

print("count is ",jdata["count"])
print("getting at one single param name is ", jdata["data"][0]["PARAM"])
print("getting at one single param value is ", jdata["data"][0]["VAL"])

# transform and write back to the same element?
# easy, just change the value and then write the file.
jdata["data"][0]["VAL"] = 51
# Writing JSON data
with open('ex_form_json_updated.json', 'w') as f:
     json.dump(jdata, f, indent=2)

# or transform and write to a new element?
jdata["data"][0]["NEWVAL"] = 51
jdata["data"][0]["VAL"] = 50 #set back to previous
# and write
with open('ex_form_json_new.json', 'w') as f:
    json.dump(jdata,f, indent=2)

# add a totally new element?
# could just make sure that the form sends me all the elements I will need even if they are blank?
#max = jdata["count"]
#jdata["data"].update({"PARAM" = "ADDED_THIS"})
jdata["data"].append({"PARAM":"ADDED_PARAMETER", "VAL":400, "FORTRAN_TYPE":"INTEGER"})
with open('ex_form_json_added', 'w') as f:
    json.dump(jdata,f,indent=2)

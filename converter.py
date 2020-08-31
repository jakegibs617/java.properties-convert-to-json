#!/usr/local/bin/python                                                                                                                                                                                                                                                         
import sys
import json
import requests
import config


if __name__ == '__main__':

    # get code from gitlab repo
    myToken = config.SECRETTOKEN
    myUrl = 'https://gitlab.com/api/v4/projects/:id/repository/files/{{url-encoded-path}}/raw?ref=master'
    head = {'PRIVATE-TOKEN': myToken}

    r = requests.get(myUrl, headers=head)

    # sanity check log
    print(r.status_code, r.reason)

    # set path for where to write the code from the request
    path = "data.properties"

    # write the curl request to the path file
    with open(path, 'w') as outfile:
        outfile.write(str(r.content))

    # convert the java.properties file to a JSON format
    f = open(path)
    lines = f.read().splitlines()
    f.close()

    data = {}

    for i, line in enumerate(lines):
        # ignore the empty lines and commented lines
        if line.strip() == '': continue
        if line.startswith( '#' ): continue

        # format as needed
        arr = line.split("=", 1)
        key = arr[0].strip()
        val = arr[1].strip()
        data[key] = val

    json_data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    # print json_data

    # write JSON data to a new file with .json format
    new_file = open((path + ".json"), "w")
    new_file.write(json_data)
    new_file.close()

    print "converted to", (path + ".json")

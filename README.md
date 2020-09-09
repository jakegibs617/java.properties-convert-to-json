# java.properties-convert-to-json (gitlab)
gitlab to file and convert


# steps to run
1. create file config.py to store your secret token
  `import config` grabs that file and pulls that secret token to use
 
2. Update the myURL to point to the file on gitlab that you need to pull from

3. run the code in terminal `$ python converter.py` 
   you should now see 2 new files, one called data.properties and one called data.properties.json
   
4. Further customize per need the json formatting on line 34 - 45

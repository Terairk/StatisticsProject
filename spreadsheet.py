
# Imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


# Setup everything
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('What is your personality type? (Responses)').sheet1

# Getting specific columns for data
results_gender = sheet.col_values(3)
results_classes = sheet.col_values(4)
results_types = sheet.col_values(6)

# Initialising lists for easy data handling
females = []; males = [];eightJ = [];eightE = [];eightR = [];eightU = [];eightD = [];eightO = [];eightN = []
istj = []; isfj = []; infj = []; intj = []; istp = []; isfp = []; infp =  []; intp = []
estj = []; esfj = []; enfj = []; entj = []; estp = []; esfp = []; enfp =  []; entp = []
femaleTypes = []
malesTypes = []




for values in results_gender:
	if values == "Male":
		males.append(values)
		
	elif values == "Female":
		females.append(values)
		
		
for classes in results_classes:
	if classes == "8J":
		eightJ.append(classes)
	elif classes == "8E":
		eightE.append(classes)
	elif classes == "8R":
		eightR.append(classes)
	elif classes == "8U":
		eightU.append(classes)
	elif classes == "8D":
		eightD.append(classes)
	elif classes == "8O":
		eightO.append(classes)
	elif classes == "8N":
		eightN.append(classes)
	
		
for types in results_types:
	if types == "ISTJ":
		istj.append(types)
	elif types == "ISFJ":
		isfj.append(types)
	elif types == "INFJ":
		infj.append(types)
	elif types == "INTJ":
		intj.append(types)
	elif types == "ISTP":
		istp.append(types)
	elif types == "ISFP":
		isfp.append(types)
	elif types == "INFP":
		infp.append(infp)
	elif types == "INTP":
		intp.append(types)
	elif types == "ESTJ":
		estj.append(types)
	elif types == "ESFJ":
		esfj.append(types)
	elif types == "ENFJ":
		enfj.append(types)
	elif types == "ENTJ":
		entj.append(types)
	elif types == "ESTP":
		estp.append(types)
	elif types == "ESFP":
		esfp.append(types)
	elif types == "ENFP":
		enfp.append(infp)
	elif types == "ENTP":
		entp.append(types)
	
people = []
counter = 1

for i in range (1, len(results_types)-1):
	if (results_gender[i] != ""):
		people.append(str(counter) + " : " + results_gender[i] + " : " + results_classes[i] + " : " + results_types[i])
		counter += 1
		

for x in range (1, len(results_types)-1):
	if (results_gender[x] == "Female"):
		femaleTypes.append(results_types[x])
	elif results_types[x] == "Male":
		malesTypes.append(results_types[x])
		
		
		
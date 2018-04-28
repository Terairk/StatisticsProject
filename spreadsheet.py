import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('What is your personality type? (Responses)').sheet1
results_gender = sheet.col_values(3)
results_classes = sheet.col_values(4)
females = []; males = [];eightJ = [];eightE = [];eightR = [];eightU = [];eightD = [];eightO = [];eightN = []

for values in results_gender:
	if (values == "Male"):
		males.append(values)
	elif (values == "Female"):
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
		
print(len(females)); print(len(males)); print(len(eightJ)); print(len(eightE)); print(len(eightR));
print(len(eightU)); print(len(eightD)); print(len(eightO)); print(len(eightN));


# Imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import matplotlib.pyplot as plt
import numpy as np

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
females = [];
males = [];
eightJ = [];
eightE = [];
eightR = [];
eightU = [];
eightD = [];
eightO = [];
eightN = []
istj = [];
isfj = [];
infj = [];
intj = [];
istp = [];
isfp = [];
infp = [];
intp = []
estj = [];
esfj = [];
enfj = [];
entj = [];
estp = [];
esfp = [];
enfp = [];
entp = []
# Males list
Mistj = [];
Misfj = [];
Minfj = [];
Mintj = [];
Mistp = [];
Misfp = [];
Minfp = [];
Mintp = []
Mestj = [];
Mesfj = [];
Menfj = [];
Mentj = [];
Mestp = [];
Mesfp = [];
Menfp = [];
Mentp = []
# Females List
Fistj = [];
Fisfj = [];
Finfj = [];
Fintj = [];
Fistp = [];
Fisfp = [];
Finfp = [];
Fintp = []
Festj = [];
Fesfj = [];
Fenfj = [];
Fentj = [];
Festp = [];
Fesfp = [];
Fenfp = [];
Fentp = []

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

'''for types in results_types:
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
		enfp.append(types)
	elif types == "ENTP":
		entp.append(types)
'''



people = []
counter = 1

count = 0
for i in range (1, len(results_types)-1):
	if (results_gender[i] != ""):
		people.append(results_gender[i] + " : " + results_classes[i] + " : " + results_types[i])
		counter += 1
		
print("Males: 26")
print("Females: 20")

for i in range(0,len(people)-1):
	test = str(people[i])
	if "8J" in test:
		
print("FeMale Judging: " + str(20-count)) # Not open minded

for x in range (1, len(results_types)):
	if (results_gender[x] == "Female"):
		femaleTypes.append(results_types[x])
	elif results_gender[x] == "Male":
		malesTypes.append(results_types[x])

for types in malesTypes:
	if types == "ISTJ":
		Mistj.append(types)
	elif types == "ISFJ":
		Misfj.append(types)
	elif types == "INFJ":
		Minfj.append(types)
	elif types == "INTJ":
		Mintj.append(types)
	elif types == "ISTP":
		Mistp.append(types)
	elif types == "ISFP":
		Misfp.append(types)
	elif types == "INFP":
		Minfp.append(types)
	elif types == "INTP":
		Mintp.append(types)
	elif types == "ESTJ":
		Mestj.append(types)
	elif types == "ESFJ":
		Mesfj.append(types)
	elif types == "ENFJ":
		Menfj.append(types)
	elif types == "ENTJ":
		Mentj.append(types)
	elif types == "ESTP":
		Mestp.append(types)
	elif types == "ESFP":
		Mesfp.append(types)
	elif types == "ENFP":
		Menfp.append(types)
	elif types == "ENTP":
		Mentp.append(types)
	

for types in femaleTypes:
	if types == "ISTJ":
		Fistj.append(types)
	elif types == "ISFJ":
		Fisfj.append(types)
	elif types == "INFJ":
		Finfj.append(types)
	elif types == "INTJ":
		Fintj.append(types)
	elif types == "ISTP":
		Fistp.append(types)
	elif types == "ISFP":
		Fisfp.append(types)
	elif types == "INFP":
		Finfp.append(types)
	elif types == "INTP":
		Fintp.append(types)
	elif types == "ESTJ":
		Festj.append(types)
	elif types == "ESFJ":
		Fesfj.append(types)
	elif types == "ENFJ":
		Fenfj.append(types)
	elif types == "ENTJ":
		Fentj.append(types)
	elif types == "ESTP":
		Festp.append(types)
	elif types == "ESFP":
		Fesfp.append(types)
	elif types == "ENFP":
		Fenfp.append(types)
	elif types == "ENTP":
		Fentp.append(types)

'''

# Bar Chart Females and Males

 ind = np.arange(16)


men_amount = (len(Mistj), len(Misfj), len(Minfj), len(Mintj), len(Mistp), len(Misfp), len(Minfp), len(Mintp),
           len(Mestj), len(Mesfj), len(Menfj), len(Mentj), len(Mestp), len(Mesfp), len(Menfp), len(Mentp))
female_amount = (len(Fistj), len(Fisfj), len(Finfj), len(Fintj), len(Fistp), len(Fisfp), len(Finfp), len(Fintp),
             len(Festj), len(Fesfj), len(Fenfj), len(Fentj), len(Festp), len(Fesfp), len(Fenfp), len(Fentp))

# width = 0.36
# plt.bar(ind - width / 2, men_amount, width, color='b', label="Male")
# plt.bar(ind + width / 2, female_amount, width, color='r', label="Female")

 plt.ylabel ('Frequency')
 plt.title('Frequency of different Myers Briggs types by type and gender')
 plt.xticks(ind,("ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
           "ESTJ", "ESFJ", "ENFJ", "ENTJ", "ESTP", "ESFP", "ENFP", "ENTP"), rotation="vertical" )
 plt.legend()

'''

# Pie Chart Stuff
'''
labels = ("ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
         "ESTJ", "ESFJ", "ENFJ", "ENTJ", "ESTP", "ESFP", "ENFP", "ENTP")
Together = (len(istj)/46, len(isfj)/46, len(infj)/46, len(intj)/46, len(istp)/46, len(isfp)/46, len(infp)/46, len(intp)/46,
            len(estj)/46, len(esfj)/46, len(enfj)/46, len(entj)/46, len(estp)/46, len(esfp)/46, len(enfp)/46, len(entp)/46)

plt.pie(Together, labels=labels, autopct = "%1.1f%%", startangle = 90)
plt.axis('equal')
'''

# Bar Chart All Genders


label = ("ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
         "ESTJ", "ESFJ", "ENFJ", "ENTJ", "ESTP", "ESFP", "ENFP", "ENTP")
ind = np.arange(len(label))
together = (len(istj), len(isfj), len(infj), len(intj), len(istp), len(isfp), len(infp), len(intp),
            len(estj), len(esfj), len(enfj), len(entj), len(estp), len(esfp), len(enfp), len(entp))

plt.bar(ind, together, color = ['black', 'red', 'gold', 'olivedrab', 'chartreuse', 'darkgreen',
                                'darkcyan', 'deepskyblue', 'navy', 'darkorchid', 'coral', 'pink',
                                'cyan', 'brown', 'yellow', 'y'])

plt.xlabel("Myers Briggs Type")
plt.ylabel("Frequency")
plt.xticks(ind, label, rotation="vertical")
plt.title("Frequency of different Myers Briggs types by type ")

plt.show()

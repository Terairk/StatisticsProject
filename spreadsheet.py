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
		enfp.append(types)
	elif types == "ENTP":
		entp.append(types)


for x in range (1, len(results_types)):
	if (results_gender[x] == "Female"):
		femaleTypes.append(results_types[x])
	elif results_gender[x] == "Male":
		malesTypes.append(results_types[x])
		
total = len(femaleTypes) + len(malesTypes)
totalFemale = len(femaleTypes)
totalMale = len(malesTypes)

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

label = ("ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
         "ESTJ", "ESFJ", "ENFJ", "ENTJ", "ESTP", "ESFP", "ENFP", "ENTP")

# Bar Chart Females and Males

ind = np.arange(16)


men_amount = (len(Mistj), len(Misfj), len(Minfj), len(Mintj), len(Mistp), len(Misfp), len(Minfp), len(Mintp),
           len(Mestj), len(Mesfj), len(Menfj), len(Mentj), len(Mestp), len(Mesfp), len(Menfp), len(Mentp))
female_amount = (len(Fistj), len(Fisfj), len(Finfj), len(Fintj), len(Fistp), len(Fisfp), len(Finfp), len(Fintp),
             len(Festj), len(Fesfj), len(Fenfj), len(Fentj), len(Festp), len(Fesfp), len(Fenfp), len(Fentp))

width = 0.36
plt.bar(ind - width / 2, men_amount, width, color='steelblue', label="Male")
plt.bar(ind + width / 2, female_amount, width, color='r', label="Female")

plt.ylabel ('Frequency')
plt.title('Frequency of different Myers Briggs types by type and gender')
plt.xticks(ind,("ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
           "ESTJ", "ESFJ", "ENFJ", "ENTJ", "ESTP", "ESFP", "ENFP", "ENTP"), rotation="vertical" )
plt.legend()



# Pie Chart Stuff


Together = (len(istj)/total, len(isfj)/total, len(infj)/total, len(intj)/total, len(istp)/total, len(isfp)/total, len(infp)/total, len(intp)/total,
            len(estj)/total, len(esfj)/total, len(enfj)/total, len(entj)/total, len(estp)/total, len(esfp)/total, len(enfp)/total, len(entp)/total)

plt.pie(Together, labels=label, autopct = "%1.1f%%", startangle = 0)
plt.axis('equal')


# Bar Chart All Genders



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


# Pie Chart Boys.

Together = (len(Mistj)/totalMale, len(Misfj)/totalMale, len(Minfj)/totalMale, len(Mintj)/totalMale, len(Mistp)/totalMale, len(Misfp)/totalMale, len(Minfp)/totalMale, len(Mintp)/totalMale,
            len(Mestj)/totalMale, len(Mesfj)/totalMale, len(Menfj)/totalMale, len(Mentj)/totalMale, len(Mestp)/totalMale, len(Mesfp)/totalMale, len(enfp)/totalMale, len(Mentp)/totalMale)
plt.pie(Together, labels=label, autopct = "%1.1f%%", startangle = 0 )
plt.axis('equal')

# Pie Chart Girls.

Together = (len(Fistj)/totalFemale, len(Fisfj)/totalFemale, len(Finfj)/totalFemale, len(Fintj)/totalFemale, len(Fistp)/totalFemale, len(Fisfp)/totalFemale, len(Finfp)/totalFemale, len(Fintp)/totalFemale,
            len(Festj)/totalFemale, len(Fesfj)/totalFemale, len(Fenfj)/totalFemale, len(Fentj)/totalFemale, len(Festp)/totalFemale, len(Fesfp)/totalFemale, len(Fenfp)/totalFemale, len(Fentp)/totalFemale)
plt.pie(Together, labels=label, autopct = "%1.1f%%", startangle = 0 )
plt.axis('equal')




plt.show()

#ProcessData.py
#Name: Aurora Gunubu
#Date: 04/06/25
#Assignment: Lab 8: Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  
  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  
  output1 = "Last name, First Name, UserID, Major-Year" + "\n"
  outFile.write(output1)

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]

    major = data[6]
    year = data[5]
    

    userID = makeUserID(first, last, idNum)
    majorYear = major_Year(major, year)
    #print(userID)
    
    output2 = last + "," + first + "," + userID + "," + majorYear + "\n" 
    outFile.write(output2)
    
  inFile.close()
  outFile.close()


def makeUserID(first, last, idNum):
    #print(first, last, student_ID)
  idLen = len(idNum)
    
  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen -3: ]
    #print(id)

  return id
  #Close files in the end to save and ensure they are not damaged.
  
def major_Year(major, year):
  major = major[:3]
  major_uppercase = major.upper()  

  if year == "Freshman":
    year_short = "FR"
  elif year == "Sophomore":
    year_short = "SO"
  elif year == "Junior":
    year_short = "JR"
  elif year == "Senior":
    year_short = "SR"

  return major_uppercase + "-" + year_short

if __name__ == '__main__':
  main()

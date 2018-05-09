import json
import sys
import urllib2


def sortByLastAndFirstName(stu):
  return (stu['lastName'], stu['firstName'])


if len(sys.argv) != 2:
  print("Give me a file name!")
  sys.exit(1)

sections = {}
with open(sys.argv[1]) as xls:
  current = xls.readline().rstrip()
  current = xls.readline().rstrip()
  while current != "":
    dataArr = current.split("\t")
    title = ' '.join([dataArr[1],dataArr[2]])
    sections[title] = { 'rosterNums': [dataArr[0]] }
    current = xls.readline().rstrip()
  current = xls.readline().rstrip()

  for key in sections:
    sections[key]['name'] = key
    sections[key]['totalStudents'] = 0
    sections[key]['students'] = []

  allStudents = []
  for line in xls.readlines():
    student = line.split()
    for key in sections:
      if student[0] in list(sections[key]['rosterNums']):
        sections[key]['totalStudents'] += 1
        studentObj = {
                'lastName': student[2].split(',')[0],
                'firstName': student[3],
                'email': student[-1],
                'studentID': 0
                }
        sections[key]['students'].append(studentObj)
        allStudents.append(studentObj)

rosters = []
for key in sections:
  rosters.append(sections[key])

examId = 1
for student in sorted(allStudents, key=sortByLastAndFirstName):
  student['studentID'] = examId
  examId += 1


for roster in rosters:
  print(roster['name'])
  students = roster['students']
  sortedStudents = sorted(students, key=sortByLastAndFirstName)
  roster['students'] = []

  for student in sortedStudents:
    roster['students'].append(student)

  print(roster['name'])
  req = urllib2.Request("http://localhost:8000/api/rosters/")
  req.add_header('Content-Type', 'application/json')

  response = urllib2.urlopen(req, json.dumps({'roster': roster}))

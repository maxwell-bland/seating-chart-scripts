import json
import sys
import urllib2

if len(sys.argv) != 2:
    print("Give me a file name!")
    sys.exit(1)

with open(sys.argv[1]) as json_file:
    roster = json.load(json_file)

roster['name'] = roster.pop('sectionName')
roster['totalStudents'] = len(roster['students'])

students = roster[u'students']


def sortByLastAndFirstName(stu):
    return (stu[u'lastName'], stu[u'firstName'])


sortedStudents = sorted(students, key=sortByLastAndFirstName)

examId = 1
for student in sortedStudents:
    student['studentID'] = examId
    examId = examId + 1

roster['students'] = sortedStudents

req = urllib2.Request("http://localhost:8000/api/rosters/")
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps({'roster': roster}))

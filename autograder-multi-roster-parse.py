import json
import sys
import urllib2


def sortByLastAndFirstName(stu):
    return (stu[u'lastName'], stu[u'firstName'])


if len(sys.argv) != 2:
    print("Give me a file name!")
    sys.exit(1)

with open(sys.argv[1]) as json_file:
    rosters = json.load(json_file)

for roster in rosters:
    roster['name'] = roster.pop('sectionName')
    roster['totalStudents'] = len(roster['students'])
    print(roster['name'])

    students = roster['students']
    sortedStudents = sorted(students, key=sortByLastAndFirstName)

    roster['students'] = []

    examId = 1
    for student in sortedStudents:
        student['studentID'] = examId
        roster['students'].append(student)
        examId = examId + 1

    print(roster['name'])

    req = urllib2.Request("http://localhost:8000/api/rosters/")
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req, json.dumps({'roster': roster}))

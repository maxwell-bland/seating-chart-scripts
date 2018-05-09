import json
import sys
import urllib2


def sortByLastAndFirstName(stu):
    return (stu[u'lastName'], stu[u'firstName'])


if len(sys.argv) != 3:
    print("Give me a file name and rostername!")
    sys.exit(1)

with open(sys.argv[1]) as json_file:
    rosters = json.load(json_file)

roster = {'name': sys.argv[2], 'totalStudents': 0, 'students': []}

for partialRoster in rosters:
    roster['students'] += partialRoster['students']
    print(len(partialRoster['students']));
    roster['totalStudents'] += len(partialRoster['students'])

sortedStudents = sorted(roster['students'], key=sortByLastAndFirstName)
roster['students'] = sortedStudents

examId = 1
for student in roster['students']:
    print( student )
    student['studentID'] = examId
    examId = examId + 1


req = urllib2.Request("http://localhost:8000/api/rosters/")
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps({'roster': roster}))

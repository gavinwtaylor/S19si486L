#!/usr/bin/env python3

import cgi
from datetime import *
from collections import deque
import csv
#import cgitb
#cgitb.enable()

calendar=[]
activeAss=[]
today=datetime.now()
today=datetime(2019,1,18,hour=7)

def date2str(date):
  return date.strftime("%a, %b ")+str(date.day)

def topPart():
  print("Content-Type: text/html")
  print()
  print("<link rel=\"stylesheet\" type=\"text/css\" href=\"class.css\" />")
  print("<html><head><title>SI486L: Machine Learning</title></head><body>")
  with open('topPart.html','r') as top:
    for line in top:
      print(line);

def courseInfo():
  with open('courseInfo.txt','r') as info:
    year=int(info.readline().strip()) #year line
    line=info.readline().split() #startdate line
    month=int(line[1])
    day=int(line[2])
    startDate=datetime(year,month,day,hour=6)
    line=info.readline().split() #enddate line
    month=int(line[1])
    day=int(line[2])
    endDate=datetime(year,month,day,hour=6)

    meetDaysCode=info.readline().strip() #meetdays line
    meetDays=[False for i in range(7)] #matching date.weekday() convention
    if 'M' in meetDaysCode:
      meetDays[0]=True
    if 'T' in meetDaysCode:
      meetDays[1]=True
    if 'W' in meetDaysCode:
      meetDays[2]=True
    if 'R' in meetDaysCode:
      meetDays[3]=True
    if 'F' in meetDaysCode:
      meetDays[4]=True

    while ("Holidays" not in line): #Holidays
      line=info.readline().strip()
    
    line=info.readline().split()
    holidays=dict()
    while ("Holidays" not in line):
      month=int(line[0])
      day=int(line[1])
      holDate=datetime(year,month,day,hour=6)
      if meetDays[holDate.weekday()]:
        holidays[holDate]=' '.join(line[2:])
      line=info.readline().split()
    
    while ("Weird" not in line):
      line=info.readline().split()

    weirds=dict()
    line=info.readline().split()
    while ("Weird" not in line):
      month=int(line[0])
      day=int(line[1])
      ofWeek=line[2]
      weirdDate=datetime(year,month,day,hour=6)
      weirds[weirdDate]=ofWeek
      line=info.readline().split()
    
    while ("Other" not in line):
      line=info.readline().split()
    others=dict()
    line=info.readline().split()
    while ("Other" not in line):
      month=int(line[0])
      day=int(line[1])
      note=' '.join(line[2:])
      otherDate=datetime(year,month,day,hour=6)
      others[otherDate]=note
      line=info.readline().split()

    meetings=[]
    current=startDate
    while current<=endDate:
      if (meetDays[current.weekday()] and \
          current not in holidays and \
          current not in weirds) or \
          (current in weirds and weirds[current] in meetDaysCode):
        meetings.append(current)
      current=current+timedelta(days=1)
    for weird in weirds:
      if meetDays[weird.weekday()] and weirds[weird] not in meetDaysCode:
        if weirds[weird] is'M':
          holidays[weird]="Monday Schedule"
        elif weirds[weird] is 'T':
          holidays[weird]="Tuesday Schedule"
        elif weirds[weird] is 'W':
          holidays[weird]="Wednesday Schedule"
        elif weirds[weird] is 'R':
          holidays[weird]="Thursday Schedule"
        elif weirds[weird] is 'F':
          holidays[weird]="Friday Schedule"
    return (meetings, holidays, others)

def closestNotOver(meetings):
  highlight=meetings[0]
  for meeting in meetings:
    if meeting>highlight and meeting<=today:
      highlight=meeting
  return highlight

def printRow(dayInfos,meeting,isHighlight=False):
  if isHighlight:
    calendar.append("<tr class=\"spaceUnder today\">")
  else:
    calendar.append("<tr class=\"spaceUnder\">")
  calendar.append("<td>"+date2str(meeting)+"</td>")

  for col in ['Notes','Exercise','Reading']:
    first=True
    calendar.append("<td>")
    for info in dayInfos:
      if not first:
        calendar.append("<br /><br />")
      if meeting<today and col in info and col+'Link' in info\
        and info[col+'Link'] is not None\
        and len(info[col+'Link'])>1:
        calendar.append("<a href=\""\
            +info[col+'Link']+"\">"+info[col]+"</a>")
      elif col in info:
        calendar.append(info[col])
      first=False
    calendar.append("</td>")
  
  first=True
  calendar.append("<td>")
  for info in dayInfos:
    if not first:
      calendar.append("<br /><br />")
    if meeting<today and 'Assignment' in info and 'AssignmentLink' in info\
        and info['AssignmentLink'] is not None\
        and len(info['AssignmentLink'])>1:
      calendar.append("<a href=\""\
          +info['AssignmentLink']+"\">"+info['Assignment']+"</a>")
    elif col in info:
      calendar.append(info['Assignment'])
    first=False
    if 'AssignmentDue' in info and info['AssignmentDue'] is not ""\
        and info['AssignmentDue'] is not None:
      calendar.append(" due "+date2str(info['AssignmentDue']))
      if today>meeting and info['AssignmentDue']<today:
        activeAss.append("<li>"+info['Assignment']+" due "\
            +date2str(info['AssignmentDue'])+"</li>")
  calendar.append("</td>")


def buildCalendar(meetings,holidays,others):
  calendar.append("<h3>Course Calendar</h3>")
  info=deque()
  with open('cal.csv') as csvfile:
    read=csv.DictReader(csvfile,delimiter='\t')
    for row in read:
      if 'AssignmentDue' in row and row['AssignmentDue'] is not "" and row['AssignmentDue'] is not None:
        m=int(row['AssignmentDue'].split()[0])
        d=int(row['AssignmentDue'].split()[1])
        row['AssignmentDue']=datetime(meetings[0].year,m,d,hour=6)
      info.append(row)
  calendar.append("<table width=100% >")
  calendar.append("<tr class=\"spaceUnder\">")
  calendar.append("<th>Date</th><th>Topic and Notes</th>"\
      +"<th>Exercise</th><th>Reading</th><th>Assignment</th>")
  calendar.append("</tr>")
  hols=deque(sorted(holidays))
  oths=deque(sorted(others))
  highlight=closestNotOver(meetings)
  blank=dict()
  for meeting in meetings:
    while len(hols)>0 and hols[0]<meeting:
      key=hols.popleft()
      blank['Notes']=holidays[key]
      printRow([blank],key)
    while len(oths)>0 and oths[0]<meeting:
      key=oths.popleft()
      blank['Notes']=others[key]
      printRow([blank],key)
    dayInfos=deque()
    if len(info)>0:
      dayInfos.append(info.popleft())
      while len(info)>0 and info[0]['new'] is "":
        dayInfos.append(info.popleft())
    else:
      dayInfos.append(dict())
    printRow(dayInfos,meeting,(meeting is highlight))
  for other in oths:
    calendar.append("<tr class=\"spaceUnder\"><td>"+date2str(other)\
        +"</td><td>"+others[other]+"</td><td></td><td></td></tr>")
  calendar.append("</table>")

def bottomPart():
  print("</div>")#close main
  print("</body>")
  print("</html>")

topPart()
(meetings,holidays,others)=courseInfo()
buildCalendar(meetings,holidays,others)
if len(activeAss)>0:
  print("<p></p><div class=\"boxed\">")
  print("<h3>Active Assignments</h3>")
  print("<ul>")
  for line in activeAss:
    print(line)
  print("</ul>")
  print("</div>")
for line in calendar:
  print(line)
bottomPart()

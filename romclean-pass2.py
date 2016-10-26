#!/usr/bin/env python

import os

mypath = os.getcwd()
kill_file = os.path.join(mypath, 'kill.lis')
error_file = os.path.join(mypath, 'error.lis')
keep_file = os.path.join(mypath, 'keep.lis')

# get files in current path
files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

matches = {}

print "Begin: parsing file list..."
for f in files:
  newf = f.replace("(","||||").replace("[","||||").replace(".","||||")
  k = newf.split("||||")[0].strip()
  v = matches.get(k, [])
  v.append(f)
  matches[k] = v
print "File list parsed."

kill_list = []
error_list = []
keep_list = []

print "Begin: filtering matches"
for k in matches.keys():
  # heuristics:
  # Tier 1: Prefer U > UE > UJ > W > E > J
  # Tier 2: Prefer [!] over non-[!]
  # Tier 3: user intervention required
  v = matches[k]
  if len(v) == 1:
    keep_list.append(v[0])
    continue # only one result for that rom -- keep it
  tempkeeplist = []
  for val in v:
    if '(U)' in val:
      tempkeeplist.append(val)
  if len(tempkeeplist) = 0:
    for val in v:
      if '(UE)' in val or '(EU)' in val:
        tempkeeplist.append(val)
  if len(tempkeeplist) = 0:
    for val in v:
      if '(UJ)' in val or '(JU)' in val:
        tempkeeplist.append(val)
  if len(tempkeeplist) = 0:
    for val in v:
      if '(W)' in val:
        tempkeeplist.append(val)
  if len(tempkeeplist) = 0:
    for val in v:
      if '(E)' in val:
        tempkeeplist.append(val)
  if len(tempkeeplist) = 0:
    for val in v:
      if '(J)' in val:
        tempkeeplist.append(val)
  
  tempkeeplist2 = []
  
  if len(tempkeeplist) > 1:
    for val in tempkeeplist:
      if '[!]' in val:
        tempkeeplist2.append(val)
  tempkeeplist = tempkeeplist2
  
  if len(tempkeeplist) == 1:
    for val in v:
      if val not in tempkeeplist:
        kill_list.append(val)
    keep_list.append(tempkeeplist[0])
  else:
    for val in v:
      error_list.append(val)
print 'Matches filtered.'

with open(kill_file, 'w') as kf:
  kf.write('\n'.join[kill_list])
  kf.write('\n')
print "Kill list saved as %s" % kill_file

with open(error_file, 'w') as ef:
  ef.write('\n'.join[error_list])
  ef.write('\n')
print "Error list saved as %s" % error_file

with open(keep_file, 'w') as keepf:
  keepf.write('\n'.join[keep_list])
  keepf.write('\n')
print "Keep list saved as %s" % keep_file

print "Please edit the error file to only include roms to delete before running pass3"
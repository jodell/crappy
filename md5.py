#!/usr/bin/env python
#
# First python script; writes out md5 sum files for vdi's & vmdk's in directories
# below the current working one.  Nothing like a lack of sudo to prompt ventures 
# into new languages!
# 
# -jf

import os, glob

path = './'
allfiles = []

# Create md5 files for vbox & vmware disk files
#
for root,dir,files in os.walk(path):
    filelist = [ os.path.join(root,fi) for fi in files if fi.endswith(".vdi") or fi.endswith(".vmdk") ]
    for f in filelist:
        allfiles.append(f)

for f in allfiles:
    print "file: " + f
    c = os.system('md5sum ' + f + ' > ' + f + '.md5')
    #print str(c)

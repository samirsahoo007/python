import re
import os
import shutil

drc = '/Users/samirsahoo/learnings/idea/webash'
backup = '/tmp/webash_bk'
#pattern = re.compile('whitelist')
#oldstr = 'whitelist'
#newstr = 'allowlist'

#pattern = re.compile('WHITELIST')
#oldstr = 'WHITELIST'
#newstr = 'ALLOWLIST'

#pattern = re.compile('blacklist')
#oldstr = 'blacklist'
#newstr = 'denylist'

#pattern = re.compile('black_list')
#oldstr = 'black_list'
#newstr = 'deny_list'

pattern = re.compile('master')
oldstr = 'master'
newstr = 'main'

pattern = re.compile('slaveName')
oldstr = 'slaveName'
newstr = 'commonName'

pattern = re.compile('shelladdin')
oldstr = 'shelladdin'
newstr = 'webash'

for dirpath, dirname, files in os.walk(drc):
    for fname in files:
        path = os.path.join(dirpath, fname) 
        #if (path.endswith('.py') or path.endswith('.json') or path.endswith('.groovy')) and '/deprecated/' not in path:
        if os.path.exists(path):
            print(path)
            strg = open(path).read()
            if re.search(pattern, strg):
                #print("path[{}], strg[{}]".format(path, strg))
                shutil.copy2(path, backup) # create a backup of it
                strg = strg.replace(oldstr, newstr) 
                f = open(path, 'w')
                f.write(strg)
                f.close()


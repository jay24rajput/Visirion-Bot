import sys
c = sys.argv[1:]
# print(c)
# import expect
import subprocess
import os
cwd = os.getcwd()
print(cwd)
# os.chdir('testvision')
# cwd=os.getcwd()
# print(cwd)
stdin=None
# git clone https://github.com/sladyn98/Pearl-Programs.git
# process = subprocess.Popen(['ls'],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
# retval = process.stdout.read().decode('utf-8')
# print(retval)

# with open('cred.txt', 'w') as f:
#     lines = ['av06','as']
#     f.writelines(lines)

# process = subprocess.Popen(['ls'],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
# retval = process.stdout.read().decode('utf-8')
# print(retval)

# git config --global user.email "you@example.com"
process = subprocess.Popen(['git','config','--global','user.email','"jay24rajput@gmail.com"'],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)


process = subprocess.Popen(['git','config','--global','user.name','"jay24rajput"'],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)

process = subprocess.Popen(['git','clone',c[0]],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)
os.chdir(c[2])
# RUN git remote add upstream https://github.com/jay24rajput/Pearl-Programs.git
process = subprocess.Popen(['git','remote','add','upstream',c[1]],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)
# git checkout sladyn
process = subprocess.Popen(['git','checkout',c[3]],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)

# git fetch upstream
process = subprocess.Popen(['git','fetch','upstream'],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)
# git rebase upstream/master
process = subprocess.Popen(['git','rebase','upstream/master'],stdout=subprocess.PIPE,stdin=subprocess.PIPE if stdin else None)
retval = process.stdout.read().decode('utf-8')
print(retval)

# with open('/cred.txt','rb') as f:
process = subprocess.Popen(['git','push','-f','origin',c[3]],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
# process.stdin.write(b'sladyn_98')
# out, err = process.communicate()
# process.stdin.flush()
# process.communicate()[0]
# process.stdin.close()
stdout, stderr = process.communicate()
# retval = process.stdout.read().decode('utf-8')
# print(retval)
# process1.wait()
import re
import subprocess

def run_cmd(cmd):
    print('cmd: ' + cmd)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = proc.communicate()
    return out, err

def get_version(string):
    match=re.search(r'Version: (.*)', string)
    return match.group(1)

def construct_module_version(module, version):
    return module + "==" + str(version)

def read_requirements_return_package_with_version(filename):
    with open(filename, 'r') as FH:
        lines = FH.readlines()
    
    module_version_str=""
    for line in lines:
        line = line.strip()
        if line == '--index https://pypi.xyz.com/simple':
            continue
        elif line:
            if '==' in line:
                line = line.split("==")[0]
            cmd='pip show ' + line
            out, err = run_cmd(cmd)
            output = out.decode('utf8')
            version = get_version(output)
            module_version_str += construct_module_version(line, version) + "\n"

    return module_version_str.strip()

print("\n############## xyz-tests/requirements.txt ###############")

fName='/Users/samirsahoo/Projects/xyz-tests/requirements.txt'
package_version=read_requirements_return_package_with_version(fName)
print("\n\n")
print(package_version)

print("\n############# mno-tests/requirements.txt ###########")

fName='/Users/samirsahoo/Projects/mno-tests/requirements.txt'
package_version=read_requirements_return_package_with_version(fName)
print("\n\n")
print(package_version)

print("\n###########################################################")

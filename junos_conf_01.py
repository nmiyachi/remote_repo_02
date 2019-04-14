##### grep set_security_address-book lines from original config

def func():
    pass

ld = open('ty1-gw1a_20190301_set.txt', encoding="utf-8")
lines = ld.readlines()
ld.close()

for line in lines:
    if line.find("set security policies ") >= 0:
        result1_01 = line
        f = open('set_policies_01.csv', 'a')
        f.write(result1_01)
        f.close()
#        print(result_01)
    elif line.find("deactivate security policies ") >= 0:
        result1_02 = line
        f = open('set_policies_01.csv', 'a')
        f.write(result1_02)
        f.close()
#        print(result1_02)
    else:
        pass





##### add csv delimiter ","

def func():
    pass

ld = open('set_policies_01.csv')
lines = ld.readlines()
ld.close()

for line in lines:
    if line.find(" description ") >= 0:
        result2_01 = line.replace(" ", ",", 10)
        f = open('set_policies_02.csv', 'a')
        f.write(result2_01)
        f.close()
    elif line.find(" description ") <= 0:
        result2_02 = line.replace(" ", ",")
        f = open('set_policies_02.csv', 'a')
        f.write(result2_02)
        f.close()
    else:
        pass

# version_0.0.2
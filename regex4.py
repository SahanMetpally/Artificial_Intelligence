import sys
idx = int(sys.argv[1])-60
x = "\\"
myRegexLst = []
myRegexLst.append("/^((?!010)[01])*$/")#60
myRegexLst.append("/^((?!101|010)[01])*$/")#61
myRegexLst.append("/^(0|1)(0*1*"+x+"1)*$/")#62
myRegexLst.append("/(?!(\w)*\w*"+x+"1\\b)\\b\w+/i")#63
myRegexLst.append("/(?=(\w)*\w*"+x+"1)(?=\w*(?!"+x+"1)(\w)\w*"+x+"2)\w+|(\w)(\w*"+x+"3){3}\w*/i")#64
myRegexLst.append("/\\b(?=(\w)*(\w*"+x+"1){2})(?!\w*(?!"+x+"1)(\w)\w*"+x+"3)\w+/i")#65
myRegexLst.append("/(((?![aeiou])\w)*([aeiou])(?!\w*"+x+"3)){5}\w*/i")#66
myRegexLst.append("/^(?=0*(10*10*)*$).(..)*$/")#67
myRegexLst.append("/^(?!00)(0|1(01*0)*1)+$/")#68
myRegexLst.append("/^(?!(0|1(01*0)*1)+$)[01]+$/")#69
print(myRegexLst[idx])
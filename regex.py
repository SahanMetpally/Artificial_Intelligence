import sys
idx = int(sys.argv[1])-30
myRegEx = [
r"/^0$|^10[10]$/",
r"/^[01]*$/",
r"/0\Z/", #/0$/
r"/\w*[aeiou]\w*[aeiou]\w*/i",
r"/^1[01]*0$|^0$/", 
r"/^[01]*110[01]*$/", 
r"/^[^`]{2,4}$/", #/^.{2,4}$/
r"/^ *\d{3} *-? *\d\d *-? *\d{4}$/", #/^\d{3} *-? *\d\d *-? *\d{4}$/
r"/^.*?d\w*/im", 
r"/^[01]?$|^1[01]*1$|^0[01]*0$/"] 
print(myRegEx[idx])
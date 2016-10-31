import run1
import run2
import run3
import run4
import sys

num = sys.argv[1]
query = sys.argv[2]

print num
print query
if num == '1':
	run1.cal(query , True)
elif num == '2':
	run2.cal(query , True)
elif num == '3':
	run3.cal(query , True)
elif num == '4':
	run4.cal(query , True)
elif num == '5':
	result1 = run1.cal(query , False)
	result2 = run2.cal(query , False)
	result3 = run3.cal(query , False)
	result4 = run4.cal(query , False)
	result = {}

	for i in range(10):
		(dis , name) = rseult1[i]
		if name in result:
			result[name] += i
		else:
			result[name] = i

	for i in range(10):
		(dis , name) = rseult2[i]
		if name in result:
			result[name] += i
		else:
			result[name] = i

	for i in range(10):
		(dis , name) = rseult3[i]
		if name in result:
			result[name] += i
		else:
			result[name] = i

	for i in range(10):
		(dis , name) = rseult4[i]
		if name in result:
			result[name] += i
		else:
			result[name] = i

	result = sorted([(v , k) for (k , v) in reault.items()] , reverse = False)
	for i in result[:10]:
		print i

else:
	print "Please using following format:\n python run.py (queryfilename) (the method you want to use)\nEx : python run.py 1 ukbench00000.jpg"



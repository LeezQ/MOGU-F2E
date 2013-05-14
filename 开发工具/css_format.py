# encoding: UTF-8
import re
import sys

for arg in sys.argv[1:]:
	#print arg

	file_object = open(arg)
	try:
		all_the_text = file_object.read( )
		result = re.sub('\s*{\s*', ' { ', all_the_text) #在 { 前后加空格
		result = re.sub('\s*;\s*', '; ', result) #在; 后空格
		result = re.sub('\s*:\s*', ': ', result) #在: 后空格
		#result = re.sub('\s*,\s*', ',  \n  ', result) #在, 后换行

		result = re.sub('\r', '', result) #去掉^M

		#result = re.sub('\  +\.', '.', result) #去除点号前 空格
		result = re.sub('\s*,\s*', ', ', result) #去除点号前 空格
		result = re.sub(': hover', ':hover', result) #去除点号前 空格
		result = re.sub(': first', ':first', result) #去除点号前 空格
		result = re.sub(' DXImageTran', 'DXImageTran', result) #去除点号前 空格
		result = re.sub('http: //', 'http://', result) #去除点号前 空格

	finally:
		file_object.close()


	file_object_write = open(arg, 'w')

	try:
		#print result
		file_object_write.write(result)
	finally:
		file_object_write.close()

	print '格式化完成: ' + arg


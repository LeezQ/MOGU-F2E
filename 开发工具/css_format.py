# encoding: UTF-8
# 用于自动化格式化 css 代码
# 该脚本只用于对格式的format，不对里面的属性顺序做修改
# 使用方式 python ./css_format.py
# 使用前：格式比较乱，排列不整齐
#		.search_tip_box { 
#			width: 450px;
#				min-height: 60px; _height: 60px; 
#			}
# 使用后：
#   .search_tip_box { width: 450px; min-height: 60px; _height: 60px; }
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


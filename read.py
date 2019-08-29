data = []
count = 0
sum = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)		
		count += 1
		if count % 1000 == 0: # %用来求余数
			print(len(data))		
print('档案读取完毕，总共有', len(data), '笔资料')

for d in data:
	length = len(d)
	sum += len(d)

print('留言平均长度为', sum/len(data))
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

print(data[0])

wc = {} # word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('请问你想查什么字： ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出现过的次数为： ', wc[word])
	else:
		print('这个字没有出现过')


for d in data:
	sum += len(d)

print('留言平均长度为', sum/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '笔留言长度小于100')
print(new[0])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '笔留言提到good')
# print(good[0])

good = [d for d in data if 'good' in d]
print(len(good))

bad = ['bad' in d for d in data]
print(bad)
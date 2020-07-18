
def read_file(filename):
	lines = []
	with open(filename,'r',encoding= 'utf-8-sig') as f:
		for line in f :
			lines.append(line.strip())
	return lines

def convert(lines):
	person = 0
	allen_wordcount = 0
	viki_wordcount = 0
	allen_stickercount = 0
	viki_stickercount = 0
	allen_imagecount = 0
	viki_imagecount = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_stickercount += 1
			elif s[2] == '圖片':
				allen_imagecount += 1
			else:
				for m in s[2:]:
					allen_wordcount += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_stickercount += 1
			elif s[2] == '圖片':
				viki_imagecount += 1
			else:				
				for m in s[2:]:
					viki_wordcount += len(m)
	print('allen說了', allen_wordcount, '個字')
	print('allen傳了', allen_stickercount, '個貼圖')
	print('allen傳了', allen_imagecount, '張圖片')

	print('viki說了', viki_wordcount, '個字')
	print('viki傳了', viki_stickercount, '個貼圖')
	print('viki傳了', viki_imagecount, '張圖片')


def write_file(filename, lines):
	with open(filename,'w')as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
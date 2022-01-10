word_list = []

with open('american-english.txt') as american_english:
    for line in american_english:
        if "'" in  line:
            continue

        l = ''.join(c for c in line.lower() if c in 'abcdefghijklmnopqrstuvwxyz')
        if len(l) == 5:
            word_list.append(l)
        
with open('word_list.txt','wb') as f:
    for word in sorted(word_list):
        f.write( (word+ "\n").encode())
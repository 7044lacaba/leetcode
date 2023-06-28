

s = "pwwkew"

tracker = 0 

for i in range(len(s)):
    buffer = []
    print(s[i])
    buffer.append(s[i])
    length = 1
    
    for j in range(len(s)):
        try:
            if s[i + j + 1] in buffer:
                break
            else:
                buffer.append(s[i + j + 1])
                length = len(buffer)
        except:
            pass
    if length > tracker:
        tracker = length 


#print(buffer)

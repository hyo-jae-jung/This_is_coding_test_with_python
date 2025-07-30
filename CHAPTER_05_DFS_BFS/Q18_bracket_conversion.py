from sys import stdin  

p = stdin.readline().strip()

def recursion(p):
    
    if p == '':
        return ''

    left,right = 0,0
    u = ''
    cc = True
    while True:
        u+=p[left+right]
        if u[-1] == '(':
            left+=1
        else:
            right+=1
        if cc and left < right:
            cc = False
        if left == right:
            break

    v = p[left+right:]
    rv = recursion(v)
    if cc:
        return u + rv
    else:
        tmp = ''
        for i in range(1,len(u)-1):
            
            if u[i] == '(':
                tmp+=')'
            else:
                tmp+='('

        return '(' + rv + ')' + tmp
    
print(recursion(p))

'''
(()())()

)(

()))((()
'''
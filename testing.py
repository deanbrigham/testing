import turtle
import math
import random
import os
import dbm
def add_spaces(word):
    if len(word)!=70:
        word=" "+word
        add_spaces(word)
    else:
        print(word)
#Chapter 3
def do_two(f):
    f()
    f()
def do_four(f):
    do_two(f)
    do_two(f)
def beam():
    print('- - - - +', end=' ')
def post():
    print('        |', end=' ')
def beam_line():
    print('+', end=' ')
    do_two(beam)
    print('')
def post_line():
    print("|", end=' ')
    do_two(post)
    print('')
def print_grid():
    beam_line()
    x=4
    while x>0:
        post_line()
        x-=1
    beam_line()
#chapter 4
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def pies(t, slices, length):
    in_angle=360.0/slices
    turn_angle=180.0-(180.0-in_angle)/2
    out_dist=math.tan(in_angle)*(length/2)
    for i in range(slices):
        t.fd(length)
        t.lt(turn_angle)
        t.fd(out_dist)
        t.lt(turn_angle)
        t.fd(length)
        t.lt(180)
#Chapter 5
def check_fermat(a, b, c, n):
    if a**n+b**n==c**n:
        print("They are equal")
    else:
        print("Unequal, theorem holds")
def fermat_input():
    x = input("Enter a, b, c, n: ")
    a = x.split(", ")
    check_fermat(int(a[0]), int(a[1]), int(a[2]), int(a[3]))
def is_triangle(a, b, c):
    if a+b<c or a+c<b or b+c<a:
        return False
    return True
#Chapter 6
def ackermann(m, n):
    assert m>=0 and n>=0
    if m==0:
        return n+1
    elif n==0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))
def palindrome(word):
    if len(word)<2:
        return True
    if word[0]==word[-1]:
        return palindrome(word[1:-1])
    return False
def is_power(a, b):
    if a%b==0:
        return True if a/b==b else is_power(a/b, b)
    return False
def gcd(a, b):
    return a if b==0 else gcd(b, a%b)
#Chapter 7
def test_root(a):
    pass
def eval_loop():
    x=0
    while True:
        ans = input('Enter problem or done when finished: ')
        if 'done' in ans:
            return x
        else:
            print(eval(ans))
            x = eval(ans)
def factorial(n):
    assert type(n)==int
    return 1 if n<=1 else n*factorial(n-1)
def each_sum(k):
    return (2*2**.5)/9801*((factorial(4*k)*(1103+26390*k))/
        (factorial(k)**4*396**(4*k)))
def est_pi():
    k=total=0
    while each_sum(k)>1e-15:
        total += each_sum(k)
        k+=1
    return 1/total
#Chapter 8
def palindrome2(word):
    return word==word[::-1]
def rotate(word, n):
    new_word = ""
    for c in word:
        ch = ord(c)+n
        if ch<97:
            ch+=26
        if ch>122:
            ch-=26
        new_word+=chr(ch)
    return new_word
def rotate2(word, n): #better
    new_word=""
    for c in word:
        anum=0
        if c.islower():
            anum=ord('a')
        elif c.isupper():
            anum=ord('A')
        cnum=(ord(c)-anum+n)%26
        new_word+=chr(cnum+anum)
    return new_word


#Chapter 9
def twenty(f):
    for line in f:
        if len(line.strip())>19:
            print(line)
def no_e(word):
    for c in word:
        if c == 'e':
            return False
    return True
def percent(f):
    y=0.0
    t=0.0
    for line in f:
        if no_e(line.strip()):
            y+=1
        t+=1
    return y/t
    
def forbidden(word, str):
    for c in str:
        if c in word.strip():
            return False
    return True
def uses_only(word, str):
    for c in word.strip():
        if c not in str:
            return False
    return True
def shortest(f):
    s="qqqqqqqqqqqqqqqqqqqqq"
    for line in f:
        if uses_all(line, "aeiou") and len(line)<len(s):
            s=line
    print(s.strip())
def uses_all(word, str):
    for c in str:
        if c not in word.strip():
            return False
    return True
def is_abc(word, str): #str used to fit file_read
    i=1
    while i<len(word.strip()):
        if word[i-1]>=word[i]:
            return False
        i+=1
    return True
def abc_rec(word):
    if len(word.strip())<2:
        return True
    elif word[0]>=word[1]:
        return False
    else:
        return abc_rec(word[1:])
def file_read(file, fu, str):
    for line in file:
        if fu(line, str):
            print(line)
def nine_sev(f): #bookkeeper
    for word in f:
        if len(word.strip())>5:
            for i in range(len(word.strip())-5):
                if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                    print(word.strip())
def nine_eight(): #198888, 199999
    for n in range(100000, 500000):
        if palindrome2(str(n)[2:]) and palindrome2(str(n+1)[1:]):
            if palindrome2(str(n+2)[1:-1]) and palindrome2(str(n+3)):
                print(n)
def nine_nine():
    pass
#chapter 10
def nested_sum(l):
    while len(l)>1:
        l[0]=l[0]+l[1]
        del l[1]
    while len(l[0])>1:
        l[0][0]=l[0][0]+l[0][1]
        del l[0][1]
    return l[0][0]
def cumsum(l):
    count = 0
    newl = []
    for i in range(len(l)):
        count += l[i]
        newl.append(count)
    return newl
def middle(l):
    return l[1:-1]
def chop(l):
    del l[0]
    del l[-1]
def is_sorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True
def is_anagram(w1, w2):
    l1=[]
    l2=[]
    for c in w1:
        l1.append(c)
    for c in w2:
        l2.append(c)
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        if not (l1[i]==l2[i]):
            return False
    return True
def has_dups(l):
    x = l[::]
    for i in range(len(l)):
        for j in range(1, len(x)):
            if l[i] == x[j]:
                return True
        del x[0]
    return False
def birthdays(i):
    count = 0
    for n in range(1, 100):
        if bday_help(i):
            count+=1
    return count/100.0
def bday_help(i):
    x = []
    for n in range(0, i):
        x.append(random.randint(1, 365))
    if has_dups(x):
        return True
    return False
def in_bisect(l, word):
    if len(l)==0:    
        return False
    mid = len(l)//2
    if word==l[mid]:
        return True
    elif word<l[mid]:
        return in_bisect(l[:mid], word)
    else:
        return in_bisect(l[mid:], word)
def bi_help(f):
    l=[]
    for line in f:
        l.append(line.strip())
    return l
def rev_pair(l):
    for i in range(len(l)):
        l[i]=l[i][::-1]


#chapter 11
def histogram(s):
    d=dict()
    for c in s:
        d[c]=1 if c not in d else d[c]+1
    return d
def histogram2(s):
    d=dict()
    for c in s:
        d[c]=d.get(c, 0)+1
    return d
def rev_lookup(d, v):
    for k in d:
        if d[k]==v:
            return k
    raise LookupError('not a key')
def invert_dict(d):
    nd=dict()
    for k in d:
        nd[d[k]]=[k] if d[k] not in nd else nd[d[k]]+[k]
    return nd
def invert_dict2(d):
    nd=dict()
    for k in d:
        nd.setdefault(d[k], []).append(k)
    return nd
def read_dict(f):
    d=dict()
    for line in f:
        if not line[0]=='#':
            t = line.split()
            word = t[0].lower()
            pron = ' '.join(t[1:])
            d[word] = pron
    return d
def homophone(d):
    for k in d:
        if len(k)==5:
            if k[1:] in d and k[0]+k[2:] in d:
                if d[k]==d[k[1:]]==d[k[0]+k[2:]]:
                    print(k)
            
def store_dict(f):
    d = dict()
    for line in f:
        d[line.strip()] = random.randint(1, 10000)
    return d
def has_dups2(l):
    d=dict()
    for x in l:
        if x not in d:
            d.setdefault(x)
        else:
            return True
    return False
def rotate_pairs(f):
    d=store_dict(f)
    for k in d:
        for i in range(1, 26):
            if rotate2(k, i) in d:
                print(k+' rotates to '+rotate2(k, i))


#chapter 12
def minmax(l):
    return min(l), max(l)
def sumall(*args):
    if len(args)==1:
        return args[0]
    else:
        return args[0] + sumall(*args[1:])
def most_freq(s):
    t={}
    for c in s:
        t[c]=t.setdefault(c, 0)+1
    r=invert_dict2(t)
    s=reversed(sorted(r))
    for n in s:
        for l in r[n]:
            print(l+' '+str(n))
def most_freq2(s):
    t={}
    for c in s:
        t[c]=t.setdefault(c, 0)+1
    l=[]
    for ch, n in t.items():
        l.append((n,ch))
    l.sort()
    l.reverse()
    for n, ch in l:
        print(ch+' '+str(n))
def more_anagrams(f):
    d={}
    for line in f:
        t=tuple(sorted(tuple(line.strip()))) 
        d[t]=d.setdefault(t, [])+[line.strip()]
    d2={}
    for w in d:
        if len(d[w])>3:
            d2[len(d[w])]=d2.setdefault(len(d[w]),[])+[d[w]]
    return d2
def print_anagrams(f):
    d=more_anagrams(f)
    for num in reversed(sorted(d)):
        for anagram_set in d[num]:
            print(anagram_set)
def scrabble(f):
    d={}
    for line in f:
        if len(line.strip())==8:
            t=tuple(sorted(tuple(line.strip())))
            d[t]=d.setdefault(t, [])+[line.strip()]
    x=[]
    for tup, lis in d.items():
        if len(lis)>len(x):
            x=lis
    return x
def tuple_list(f):
    d={}
    for line in f:
       t=tuple(sorted(tuple(line.strip())))
       d[t]=d.setdefault(t, [])+[line.strip()]
    return d
def metathesis(f):
    d={}
    for line in f:
       t=tuple(sorted(tuple(line.strip())))
       d[t]=d.setdefault(t, [])+[line.strip()]
    l=[]
    for lis in d.values():
        for word in lis:
            for wo in lis[1:]:
                if meta_helper(word, wo):
                    l.append((word, wo))
            lis.remove(word)
    for w1, w2 in l:
        print(w1+' ---> '+w2)
def is_meta(w1, w2):
    clist=[]
    ilist=[]
    count=0
    for i in range(len(w1)):
        if not w1[i]==w2[i]:
            count+=1
            ilist.append(i)
            clist.append(w1[i])
    if count==2:
        nw=w1[:ilist[0]]+clist[1]+w1[ilist[0]+1:ilist[1]]+clist[0]+w1[ilist[1]+1:]
        if nw==w2:
            return True
    return False
def meta_helper(w1, w2):
    count=0
    if len(w1)==len(w2):
        for c1, c2 in zip(w1, w2):
            if c1!=c2:
                count+=1
    return count==2
def twelve_four(f):
    longest=''
    for line in f:
        if len(line.strip())>len(longest):
            if tf_helper(line.strip()):
                longest=word
    print(longest)
def tf_helper(word):
    if len(word)==1 and (word[0]=='a' or word[0]=='i'):
        return True
    if len(word)>1:
        return True 
    return False
def child_list(word, f):
    l=[]
    d=tuple_list(f)
    for i in range(len(word)):
        t=tuple(word[:i]+word[i+1:])
        for w in d[tuple(sorted(t))]:
            l.append(w)
    return l
        
#Chapter 13

    
#chapter 14
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name) #joins names into path
        if os.path.isfile(path): #print if file, rec call if directory
            print(path)
        else:
            walk(path)
            
def sed(str, rep, f1, f2):
    old=open(f1, 'r')
    n=open(f2, 'w')
    for line in old:
        line=line.replace(str, rep)
        n.write(line)
    old.close()
    n.close()
def store_anagrams():
    pass
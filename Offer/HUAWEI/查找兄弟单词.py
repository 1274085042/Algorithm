#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.


def define_dict(inp):
    #lis=inp.split()
    inp.sort()
    return  inp
    #dict=[]

def sibling_count(l,str,n):
    count=0
    res=[]

    for j in l:
        if j==str:
            continue
        else:
            if sorted(list(str))==sorted(list(j)):
                count+=1
                res.append(j)
    if n-1>=len(res):
        return count,None
    else:
        return count,res[n-1]

while True:
    try:
        inp="183 bacad ad cda a dcccd aab bb cb cbd bacd dcbb dda b adcb dca ab adbd ab caa bbaba adad dc cbd ccddb cdc ab ad cb ddb bc bcdb cdcc bcbb dd abdd bda bad cdbb d dcb bc badcb cacc bbacb da dbadd cada bcbdc ddbca db ca ca d ad d ddcb bb ba bab adaca aba cbca aaddd cbccc c c bcdbb cdd dcabd d dd db dabad d acddc a ddcb daba daca b bba adb db c a accb aa dcab bdccc adbb a bacb cbdba aa ad cab cada bcba ccadc cba bd dad cc bcda dcaac acaad abada a cb c d ddac acb a ba acaa bdb cdb cada bc cccac d dcaa bd bcada dab ad dacb aaada dc dcccd acac dbdb cd acdac bbdbc caad cbc bdab dd abaa bc ada ba cbda a dbaa dabd cd aacdc bdcb bbcc ccca cac ddba cdcd dc aab b bbad bbdd bc adc cdab bba acad ca cbc a c c addbd caadb cbaa ab d bbbd c dcc ab c ba ccbb adad 1"
        #inp=input().strip().split()
        inp=inp.strip().split()
        inp_str=inp[1:-2]
        str=inp[-2]
        n=int(inp[-1])
        l=define_dict(inp_str)
        count,res=sibling_count(l,str,n)
        print(count)
        if res!=None:
            print(res)
#print(define_dict(inp))
    except:
        break



















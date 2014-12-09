import os, re

linea,a,c,counter="vane",[],[],0

file1=open('UTR_Todas_sp_unicas_linea.txt', 'r')
file2=open('RF00059_vs_UTR_Todas_sp_unicas', 'r')
f=open("nuevo.txt","w")

while linea!="":
    linea=file2.readline()
    p=re.compile('(\s*[(0-9)]+\s*[!]\s*[0-9a-zA-Z.-]+\s*)([0-9.]+)(\s*[0-9.]+\s*) (\w{3}\-.*?\|.*?\|\w*)')
    patron=re.search(p,linea)
    if patron!=None:
        score=float(patron.group(2))
        ide=patron.group(4)
        if score>=35.8:
            a.append(ide)
'''
a=list(set(a))
for line in file1.readlines():
    lineas=file1.readline()
    for x in range(0,5):
        geno=re.search(a[x],lineas)
        if geno!=None:
            lineas=file1.readline()
            print (a[x]+','+lineas)
            #f.write(a[x]+','+lineas)
            break
'''
b= list(set(a))

for item in file1:
    c.append(item)

for item in a:
    condi = False
    for line in c:
        if condi:
            counter += 1
            print(str((counter/len(b))*100)[0:4]+" % Cargado")
            f.write(item + "," + line)
            condi = False
            break
        if item in line:
            condi = True
f.close()
file1.close()
file2.close()


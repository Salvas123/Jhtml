li = input("Escribe el nombre del archivo Json:")
try:
    f = open(li+".jhtml","r")
except:
    exit()

def traducir(lineas,li):
    fo = open(li+".json","w")
    arr = ""
    con0 = 0
    con1 = 0
    holol2 = len(lineas)
    print(lineas)
    insi = False # for attributes or main data
    insi1 = False #for [
    print(range(0,len(lineas)-1))
    for i in range(0,len(lineas)):
        fo.write("{")
        arr = ""
        con1 = 0
        print("numero i",i)
        for j in range(0,len(lineas[i])-1):
            holol = list(lineas[i])
            savbe = -1
            if not holol[j] == holol[len(lineas[i])-1]:
                if holol[j] == ",":
                    print(arr)
                    fo.write("tagName:"+arr)
                    arr = ""
                elif holol[j] == ":":
                    print(arr)
                    if arr == "content":
                        fo.write("content:")
                        insi = False
                    elif arr == "name":
                        fo.write("name:")
                        insi = False
                    else:
                        if not insi1:
                            fo.write("attributes:[{attrName:"+arr+",")
                            print(2)
                            insi = True
                            insi1 = True
                            print(insi)
                        else:
                            fo.write("{attrName:"+arr+",")
                            insi = True
                    arr = ""
                elif holol[j] == "-":
                    print(arr)
                    con1 += 1
                    print(con1,"soy savbe")
                elif holol[j] == " ":
                    print(3)
                    print(insi)
                    if insi:
                        fo.write("attr:"+arr+"},")
                    else:
                        fo.write(arr+",")
                    arr = ""
                elif holol[j] == "_":
                    arr += " "
                elif holol[j] == "&":
                    arr += ":"
                else:
                    print(arr)
                    arr += holol[j]
        else:
            if not insi1:
                fo.write("attributes:[],")
            else:
                fo.write("],")
            insi1 = False
            insi = False
            con3 = con1 - 1
            if lineas[i] == lineas[holol2-1]:
                fo.write("tagChilds:[]")
                while con3 >= 0:
                    if con3 > 0:
                        fo.write("}],")
                    elif con3 == 0:
                        fo.write("}]")
                    con3 -= 1
            else:
                if list(lineas[i+1])[con1] == "-":
                    fo.write("tagChilds:[")
                    print("hola soy yo")
                else:
                    fo.write("tagChilds:[]},")
                    h = 0
                    while not list(lineas[i+1])[con1-h-1] == "-":
                        if h > 1:
                            fo.write("}],")
                        h += 1
    fo.write("}")
    fo.close()

lin = f.readlines()
traducir(lin,li)
f.close();

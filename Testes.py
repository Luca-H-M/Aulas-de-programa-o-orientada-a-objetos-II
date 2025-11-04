list = []
dic = {"1":"string", "2":[1, 2, 3]}
dic2 = {"1":"string3", "2":[4, 5, 6]}
dic3 = {"1":"string2", "2":[7, 8, 9]}
list.append(dic)
list.append(dic2)
list.append(dic3)

for x in list:
    nf = 0
    for n in x["2"]:
        nf += n

    print(nf/len(x["2"]))
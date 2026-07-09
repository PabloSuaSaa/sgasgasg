dict1={}
dict2={}
dict1={"lista1":["dato", "dato2", "dato3"],
       "lista2": ["dato", "dato2", "ldato3"],
       "lista3":["dato", "dato2", "dato3"]}
print(dict1["lista1"][1])
for i in dict1:
    if i=="lista2":
        print(dict1["lista2"][2])    

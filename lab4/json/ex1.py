import json

file = open('01.json', 'r')
js = json.load(file)



print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for i in js['imdata']:
    print(i['l1PhysIf']['attributes']['dn'], end ="                       \t")
    print(i['l1PhysIf']['attributes']['descr'], end= "  \t")
    print( i['l1PhysIf']['attributes']['speed'], end= "   ")
    print( i['l1PhysIf']['attributes']['mtu'], end= '\n')


file.close()




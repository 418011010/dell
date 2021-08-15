filecheckdict = {
    "Aar": {"readme.txt": "condition", "Digest": False, "DtsInfo.txt": True},
    "HM": {"readme.txt": "condition", "Digest": False, "DtsInfo.txt": "condition"},
    "Common": {"readme.txt": False, "Digest": True, "DtsInfo.txt": True}
}

newdict = dict()
newdictchild = dict()
for k1, v1 in filecheckdict.items():
    #print(k1, v1)
    for k2, v2 in v1.items():
        print(k2, v2)
        if v2:
            newdictchild = {}
            newdictchild[k1] = v2
            if newdict.get(k2):
                newdict[k2].update(newdictchild)
            else:
                newdict[k2] = newdictchild

print(newdict)


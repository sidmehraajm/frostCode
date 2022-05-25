def pushVec(end):
    vec=findClosest(end)
    #print(vec)
    return (vec/1.0)
#pos =getVec('pSphere4')
mesh = om2.MSelectionList()
mesh.add('pSphere1')
dagPath = mesh.getDagPath(0)
obj = om2.MFnMesh(dagPath)


def findClosest(pos):
    vec= obj.getClosestNormal(om2.MPoint(pos),space= om2.MSpace.kWorld)[0]
    #print (vec)
    return vec
sl = pm.ls(sl=1)    
for i in sl:
    defPos = getVec(i)
    print(defPos)
    a= pushVec(defPos)
    print (a)
    i.translate.set(defPos+a)
    
'''    
vec = None
    dist = 10000.0
    for loc in pm.ls('locator?'):
        loc_pos = getVec(loc)
        print(loc_pos)
        temp_vec = pos-loc_pos
        print(temp_vec)
        if temp_vec.length() < dist:
            vec = om2.MVector(temp_vec)
            dist = temp_vec.length()
'''
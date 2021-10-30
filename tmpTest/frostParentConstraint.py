import pymel.core as pm
import maya.api.OpenMaya as om




dgn = om.MFnDagNode()
mobj = om.MObject()


sel = om.MGlobal.getActiveSelectionList()  # selection
srcDagpath = sel.getDependNode(0)          # first node
srctransform_node  = om.MFnTransform(srcDagpath) # MFnTransform
srcBaseMtx= srctransform_node.transformation().asMatrix()  # matrix
srcName = (dgn.setObject(sel.getDagPath(0))).name()#dagname 
srcPym = pm.PyNode(srcName)#dagPynode

tgtDagpath = sel.getDependNode(1)          # first node
tgttransform_node  = om.MFnTransform(tgtDagpath) # MFnTransform
tgtBaseMtx= tgttransform_node.transformation().asMatrix()  # matrix
tgtName = (dgn.setObject(sel.getDagPath(1))).name()#dagname    
tgtPym = pm.PyNode(tgtName)#dagPynode


srcAtrName = str(srcPym)+'_srcBaseMtx'
tgtAtrName = str(tgtPym)+'_tgtBaseMtx'

if pm.attributeQuery(srcAtrName,n =srcPym ,ex=1):
    pass
else:
    pm.addAttr(srcPym,dt = 'matrix',ln = srcAtrName)
    
pm.addAttr(srcPym,dt = 'matrix',ln = tgtAtrName)

pm.PyNode(srcPym+'.'+srcAtrName).set(srcBaseMtx)
pm.PyNode(srcPym+'.'+tgtAtrName).set(tgtBaseMtx)



bfGraphConNode =  pm.createNode('bifrostGraphShape',n=(str(srcPym)+'_To_'+ str(tgtPym)+'_parentCons'))

grphTr = pm.listRelatives(bfGraphConNode,p=1)[0]

pm.rename(grphTr,(str(srcPym)+'_To_'+ str(tgtPym)+'_parentCons'))

pm.vnnNode(bfGraphConNode,'/input',cop = ('srcBaseMtx','Math::float4x4'))
pm.vnnNode(bfGraphConNode,'/input',cop = ('tgtBaseMtx','Math::float4x4'))
pm.vnnNode(bfGraphConNode,'/input',cop = ('srcMtx','Math::float4x4'))
pm.vnnNode(bfGraphConNode,'/input',cop = ('tgtMtx','Math::float4x4'))

srcBaseMtxN = pm.vnnCompound(bfGraphConNode,'/',an =  "BifrostGraph,Core::Constants,Math::float4x4",rn = ('value','srcBaseMtxMult'))                             

pm.vnnConnect(bfGraphConNode,'.srcBaseMtx',"/srcBaseMtxMult.value")

tgtBaseMtxN = pm.vnnCompound(bfGraphConNode,'/',an =  "BifrostGraph,Core::Constants,Math::float4x4",rn = ('value','tgtBaseMtxMult'))                             

pm.vnnConnect(bfGraphConNode,'.tgtBaseMtx',"/tgtBaseMtxMult.value")


srcBaseMtxN = pm.vnnCompound(bfGraphConNode,'/',an =  "BifrostGraph,Core::Constants,Math::float4x4",rn = ('value','srcMtxMult'))                             

pm.vnnConnect(bfGraphConNode,'.srcMtx',"/srcMtxMult.value")



pm.vnnConnect(Graph1,'.BasePos',('/'+str(aimPos1[0])+'.BaseTransform1'),cm=1)




















Graph1 = pm.createNode('bifrostGraphShape',n= 'TestGraph')

a = pm.bifrostGraph(lgs =1)

aimPos1 = pm.vnnCompound(Graph1,'/',an = "BifrostGraph,User::Compounds,aimPos")

pm.vnnNode(Graph1,'/input',cop = ('BasePos','Math::float4x4'))
pm.vnnNode(Graph1,'/input',cop = ('BasePos','Math::float4x4'))

pm.vnnConnect(Graph1,'.BasePos',('/'+str(aimPos1[0])+'.BaseTransform1'),cm=1)











import maya.api.OpenMaya as om2
import pymel.core as pm

def getVec(arg):
    v = om2.MVector(pm.xform(arg,q=1,rp=1,ws=1))
    return v
    

#polPos = polePos(ArmPos = 'a',ElbowPos = 'e',WristPos ='w',PoleFactor=4)
#a.translate.set(polPos)

def polePos(ArmPos,ElbowPos,WristPos,PoleFactor = 5) :  
    armPos = getVec(ArmPos)
    elbowPos = getVec(ElbowPos)
    wristPos = getVec(WristPos)
    
    armToWrist = wristPos-armPos
    midPos_vc = armToWrist/2.0
    midPos = armPos+midPos_vc
    
    
    midPToElb_vc = elbowPos-midPos
    midPToElb_vcScale = midPToElb_vc*PoleFactor
    midPToElb_pos = midPos+midPToElb_vcScale
    return midPToElb_pos
        


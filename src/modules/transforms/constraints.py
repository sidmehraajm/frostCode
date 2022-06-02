#ParentConstraint from bfr 
import pymel.core as pm
import maya.cmds as cmds
def bf_parent_con(src = None,tgt=[],dcm=True,opm=False):
    """
    Bifrost Constraint 
    Args:
        src: Source Object : single transform
        tgt:Target objects : list of transforms/ singe transform
        dcm: decompose the Output connection: bool
        opm: uses offest parent matrix of the children for the Output connection: bool
        
    Returns:
        None

    Raises:
        Raises Runtime error if no src or target is provided

    example: 
        bf_parent_con('source Object',['target_object_1','target_object_2'],dcm=False)
    """

    if src == None:
        raise RuntimeError('No Source Provided')
    if len(tgt)<=0:
        raise RuntimeError('No Target Provided')
        
    for child in tgt:
        parent_con_name = ('%s_to_%s_parent_cons'%(str(src[0]),child))

        #creating bfr node 
        bf_node = pm.createNode('bifrostGraphShape',n = parent_con_name)

        #creating inputs and outputs on bfr node
        pm.vnnNode(bf_node,'/output',cip = ('out_constraint','Math::float4x4'))
        pm.vnnNode(bf_node,'/input',cop = ('src','Math::float4x4'))
        pm.vnnNode(bf_node,'/input',cop = ('src_pos','Math::float4x4'))
        pm.vnnNode(bf_node,'/input',cop = ('tgt_pos','Math::float4x4'))

        #creating parent compund
        constraint_compund = pm.vnnCompound(bf_node,'/',an =  'BifrostGraph,User::Compounds,ParentConstraint_2')

        #connecting the parent compund to bfr node
        pm.vnnConnect(bf_node,'.src','/ParentConstraint_2.src')
        pm.vnnConnect(bf_node,'.src_pos','/ParentConstraint_2.src_pos')
        pm.vnnConnect(bf_node,'.tgt_pos','/ParentConstraint_2.tgt_pos')
        pm.vnnConnect(bf_node,'/ParentConstraint_2.out_constraint','.out_constraint')

        #connecting to src and tgt
        srcPyNode = pm.PyNode(src)
        tgtPyNode = pm.PyNode(child)
        
        srcPyNode.worldMatrix[0]>>bf_node.src
        srcPyNode.worldMatrix[0]>>bf_node.src_pos
        tgtPyNode.worldMatrix[0]>>bf_node.tgt_pos

        #disconnecting the pos attrs
        pm.disconnectAttr(srcPyNode.worldMatrix[0],bf_node.src_pos)
        pm.disconnectAttr(tgtPyNode.worldMatrix[0],bf_node.tgt_pos)
        tgtPyNode.inheritsTransform.set(0)

        #connection by decompose matrix by default
        if dcm == True:
            DCM_out = pm.createNode('decomposeMatrix',n =parent_con_name+'_DCM')
            bf_node.out_constraint>>DCM_out.inputMatrix
            DCM_out.outputTranslate>>tgtPyNode.translate
            DCM_out.outputRotate>>tgtPyNode.rotate
            DCM_out.outputScale>>tgtPyNode.scale
            DCM_out.outputShear>>tgtPyNode.shear

        #else by offset parent matrix 
        else:
            bf_node.out_constraint>>tgtPyNode.offsetParentMatrix
            tgtPyNode.translate.set(0,0,0)
            tgtPyNode.rotate.set(0,0,0)
            tgtPyNode.scale.set(1,1,1)
            tgtPyNode.shear.set(0,0,0)

        #converting bfr node to dg
        brf_board = pm.bifrostGraph(bf_node,tbd =True)
        pm.rename(brf_board,parent_con_name)

        

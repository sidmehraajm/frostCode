from ast import Raise
import pymel.core as pm
#constant shape positon variables


def create_bfr_control(bfnode = None,shape_array =circle_shape,Ctlname = 'ctrl_00',pos = None,parent = None):
    if bf_node==None:
        bf_node = pm.createNode('bifrostGraphShape',n = 'ControlBase'+'_bfGraph')
    else:
        if pm.objectType(bfnode)=='bifrostGraphShape':
            bf_node  = bfnode
        else:
            raise RuntimeError(str(bfnode) +'bf graph not found')

        

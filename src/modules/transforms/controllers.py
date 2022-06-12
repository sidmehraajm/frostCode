import random
import pymel.core as pm
#constant shape positon variables


def create_bfr_control(bfnode = None,shape_array ='circle_shape',Ctlname = 'temp',color = 'rand', pos = None,parent = None,ctrl_volume=.03,inheritTransform = 1):
    """
    Bifrost Constraint 
    Args:
        bfnode: a bifrost node can be given, when a control has to be created
                in a seperate graph else it will create in it's own graph: single transform: |||Needs a bifrost graph node|||
        
        shape_array:Shape of the Control by default create circle shape
                    Avialable shapes - Global_shape
                                       COG_Shape
                                       circle_shape
                                       sphere_shape
                                       pyramid_shape
                                       head_ctrl_shape
                                       octahedron_shape
                                       cube_shape
                                       four_arrow_shape

        Ctlname: Only the name and side Name of the control, '_ctrl will be added automatically'
        color: = a random color will be assigned automaticall,
                 Avialable color options are - Red
                                               Black
                                               Green
                                               Blue 
                                               Yellow
                                               Teal
                                               White

        pos: A matrix can be given if the control has to be placed at  specific position it will be set from offsetParentMatrix, A matrix should be a pyMel matrix, else it can cause erros
    

        parent: name of the parent object can be given else default it will be parente to world

        ctrl_volume: Default volume is .03, for importnat controls more volume looks appealing

        inheritTransform: Default is switched on 

    Returns:
        Ctrl Transform

    Raises:
        Raises Runtime error if no parent is found

    example: 
        bf_parent_con('source Object',['target_object_1','target_object_2'],dcm=False)
    """

    Ctlname = Ctlname+'_ctrl_0'
    if bfnode==None:
        
        if pm.objExists('ControlBase_bfGraph'):
            
            bifrost_control_shape = 'ControlBase_bfGraph'
        else:
            
            bifrost_control_shape = pm.createNode('bifrostGraphShape',n = 'ControlBase_bfGraph')
            brf_board = pm.bifrostGraph(bifrost_control_shape,tbd =True)
            pm.rename(brf_board,str(bifrost_control_shape))
    else:
        if pm.objectType(bfnode)=='bifrostGraphShape':
            bifrost_control_shape  = bfnode
            
        else:
            raise RuntimeError(str(bfnode) +'bf graph not found')
    
    print (bifrost_control_shape)
    shape_compund = pm.vnnCompound(str(bifrost_control_shape),'/',an =  'BifrostGraph,User::Compounds,%s'%shape_array)[0]
    Out_ctrls = pm.vnnNode(str(bifrost_control_shape), "/", listPorts=True)
    ctrl_Names = []
    
    if Out_ctrls:
        if len(Out_ctrls)>0:
            for i in Out_ctrls:
                ctrl_Names.append(i.split('.')[-1])
                
        while Ctlname in ctrl_Names:
            integer = int(Ctlname.split('_')[-1])
            Ctlname = Ctlname.replace(str(integer),'')
            integer= integer+1
            Ctlname= Ctlname+str(integer)
            
    
                
    ip = pm.vnnNode(str(bifrost_control_shape),'/output',cip = ('%s'%Ctlname,'Amino::Object'))
    pm.vnnConnect(str(bifrost_control_shape),'/%s.%s'%(shape_compund,shape_array),'.%s'%Ctlname)
    ctrlNode = pm.listConnections('%s.%s'%(str(bifrost_control_shape),Ctlname))[0]
    pm.rename(ctrlNode,Ctlname)

    rand_color = [random.randint(0,10),random.randint(0,10),random.randint(0,10)]
    color_dict = {'Red':[10,0,0],
                   'Black':[0,0,0],
                   'Green':[0,10,0],
                   'Blue':[0,0,10],
                   'Yellow':[10,10,0],
                   'Teal':[0,12,12],
                   'White':[1,1,1]
                   }
    if color in color_dict:
        shape_color = color_dict[color]
        print(color_dict[color])
    else:
        shape_color = rand_color
        print(shape_color)
    pm.vnnNode(str(bifrost_control_shape),'/%s'%shape_compund,setPortDefaultValues = ('colormin','{%s,%s,%s}'%(shape_color[0],shape_color[1],shape_color[2])))
    pm.vnnNode(str(bifrost_control_shape),'/%s'%shape_compund,setPortDefaultValues = ('colormax','{%s,%s,%s}'%(shape_color[0],shape_color[1],shape_color[2])))
    pm.vnnNode(str(bifrost_control_shape),'/%s'%shape_compund,setPortDefaultValues = ('default_size','%s'%ctrl_volume))
    ctlPyNode = pm.PyNode(Ctlname)
    if pos:
        
        try:
            try:
                ctlPyNode.offsetParentMatrix.set(pos)
            except:
                pm.setAttr('%s.offsetParentMatrix'%Ctlname,pos, type="matrix")
        except:
            raise RuntimeError('Failed to set the pos for%s'%Ctlname)
    
    if parent:
        try:
            pm.parent(Ctlname,parent)
        except:
            raise RuntimeError('Failed to parent %s under %s'%(Ctlname,parent))
    
    ctlPyNode.inheritsTransform.set(inheritTransform)
    

create_bfr_control(color='Green',ctrl_volume=.09,inheritTransform=0)

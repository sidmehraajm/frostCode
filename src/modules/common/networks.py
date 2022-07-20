import pymel.core as pm
from ..transforms import transform
tn = transform.tf_class()

class networker(object):
    
    def create_network(self,modName=''):
        if modName !='':
            pass
        else:
            raise RuntimeError('mod name %s not found unable to create network'%modName)
        
        global_input_network = pm.createNode('network',name = '%s_input_network'%modName)
        global_output_network = pm.createNode('network',name = '%s_output_network'%modName)

        guide_input_network = pm.createNode('network',name = '%s_guide_input_network'%modName)
        guide_output_network = pm.createNode('network',name = '%s_guide_output_network'%modName)\

        control_input_network = pm.createNode('network',name = '%s_control_input_network'%modName)
        control_output_network = pm.createNode('network',name = '%s_control_output_network'%modName)

        skeleton_input_network = pm.createNode('network',name = '%s_skeleton_input_network'%modName)
        skeleton_output_network = pm.createNode('network',name = '%s_skeleton_output_network'%modName)                    

        misc_input_network = pm.createNode('network',name = '%s_misc_input_network'%modName)
        misc_output_network = pm.createNode('network',name = '%s_misc_output_network'%modName)                    

        tn.add_network_attr(global_input_network,'%s_input_network'%modName)
        tn.add_network_attr(global_output_network,'%s_output_network'%modName)
        
        tn.add_network_attr(guide_input_network,'%s_guide_input_network'%modName)
        tn.add_network_attr(guide_output_network,'%s_guide_output_network'%modName)

        tn.add_network_attr(control_input_network,'%s_control_input_network'%modName)        
        tn.add_network_attr(control_output_network,'%s_control_output_network'%modName)

        tn.add_network_attr(skeleton_input_network,'%s_skeleton_input_network'%modName)    
        tn.add_network_attr(skeleton_output_network,'%s_skeleton_output_network'%modName)
        
        tn.add_network_attr(misc_input_network,'%s_misc_input_network'%modName)    
        tn.add_network_attr(misc_output_network,'%s_misc_output_network'%modName)
        
        rig_global_grp = pm.PyNode('%s'%modName)
        rig_guide_grp = pm.PyNode('%s_guides'%modName)
        rig_controls_grp = pm.PyNode('%s_controls'%modName)
        rig_skeleton_grp = pm.PyNode('%s_skeleton'%modName)
        rig_misc_grp = pm.PyNode('%s_misc'%modName)


        pm.connectAttr(global_input_network+'.%s_input_network'%modName,rig_global_grp+'.%s_input_network'%modName)
        pm.connectAttr(rig_global_grp+'.%s_output_network'%modName,global_output_network+'.%s_output_network'%modName)

        pm.connectAttr(guide_input_network+'.%s_guide_input_network'%modName,rig_guide_grp+'.%s_guide_input_network'%modName)
        pm.connectAttr(rig_guide_grp+'.%s_guide_output_network'%modName,guide_output_network+'.%s_guide_output_network'%modName)

        pm.connectAttr(control_input_network+'.%s_control_input_network'%modName,rig_controls_grp+'.%s_control_input_network'%modName)
        pm.connectAttr(rig_controls_grp+'.%s_control_output_network'%modName,control_output_network+'.%s_control_output_network'%modName)

        pm.connectAttr(skeleton_input_network+'.%s_skeleton_input_network'%modName,rig_skeleton_grp+'.%s_skeleton_input_network'%modName)
        pm.connectAttr(rig_skeleton_grp+'.%s_skeleton_output_network'%modName,skeleton_output_network+'.%s_skeleton_output_network'%modName)
        
        pm.connectAttr(misc_input_network+'.%s_misc_input_network'%modName,rig_misc_grp+'.%s_misc_input_network'%modName)
        pm.connectAttr(rig_misc_grp+'.%s_misc_output_network'%modName,misc_output_network+'.%s_misc_output_network'%modName)

    def find_input_network(self,modName='',sub_module=None):
        
        if modName !='':
            pass
        else:
            raise RuntimeError('mod name %s not found'%modName)

        if sub_module == None:
            all_networks = pm.ls(pm.listConnections('%s'%modName),typ = 'network')
            for i in all_networks:
                if '_input' in str(i):
                    input_network = i
                    return input_network
                else:
                    pass
        else:
            if pm.objExists('%s_%s'%(modName,sub_module)):
                all_networks = pm.ls(pm.listConnections('%s_%s'%(modName,sub_module)),typ = 'network')
                for i in all_networks:
                    if '_input' in str(i):
                        input_network = i
                        return input_network
                    else:
                        pass
                
            else:
                raise RuntimeError('%s_%s not found'%(modName,sub_module))
            
    def find_output_network(self,modName='',sub_module=None):
        
        if modName !='':
            pass
        else:
            raise RuntimeError('mod name %s not found'%modName)
        
        if sub_module == None:
            all_networks = pm.ls(pm.listConnections('%s'%modName),typ = 'network')
            for i in all_networks:
                if '_output' in str(i):
                    output_network = i
                    return output_network
                else:
                    pass
        else:
            if pm.objExists('%s_%s'%(modName,sub_module)):
                all_networks = pm.ls(pm.listConnections('%s_%s'%(modName,sub_module)),typ = 'network')
                for i in all_networks:
                    if '_output' in str(i):
                        output_network = i
                        return output_network
                    else:
                        pass
                
            else:
                raise RuntimeError('%s_%s not found'%(modName,sub_module))
            
    def add_world_mtxs_to_output(self,output_ntw='',object=''):
        if output_ntw !='':
            pass
        else:
            raise RuntimeError('%s output network node not found'%output_ntw)
        if object !='':
            pass
        else:
            raise RuntimeError('%s object network node not found'%object)

        tn.add_matrix_attr(output_ntw,atrName='%s_worldMatrix'%object)
        pm.connectAttr(object+'.worldMatrix[0]',output_ntw+'.%s_worldMatrix'%object)
        tn.add_matrix_attr(output_ntw,atrName='%s_worldInverseMatrix'%object)
        pm.connectAttr(object+'.worldInverseMatrix[0]',output_ntw+'.%s_worldInverseMatrix'%object)

    def match_network_attrs(self,ntw_from='',ntw_to=''):
        if ntw_from !='':
            pass
        else:
            raise RuntimeError('%s network node not found'%ntw_from)
        if ntw_to !='':
            pass
        else:
            raise RuntimeError('%s network node not found'%ntw_to)

        Attributes = pm.listAttr('%s'%ntw_from,ud=1)
        Out_Attributes = pm.listAttr('%s'%ntw_to,ud=1)
        for i in Attributes:
            at_type = pm.getAttr('%s.%s'%(ntw_from,i),type=1)
            if at_type == 'message':
                Attributes.remove(i)

        for i in Attributes:
            at_type = pm.getAttr('%s.%s'%(ntw_from,i),type=1)

            if at_type == 'matrix':
                if i in Out_Attributes:
                    try:pm.connectAttr(ntw_from+'.%s'%i,ntw_to+'.%s'%i)
                    except:pass
                    
                else:
                    tn.add_matrix_attr(ntw_to,atrName=i)
                    pm.connectAttr(ntw_from+'.%s'%i,ntw_to+'.%s'%i)
            elif at_type == 'enum' or 'float' or 'double' or 'bool':
                print ('%s_%s'%(i,at_type))











            
        
        










        



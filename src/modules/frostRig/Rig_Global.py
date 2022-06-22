#Global_ctrl_setup
import pymel.core as pm 
from ..transforms import transform
from ..transforms import controllers
from ..common import networks

tn = transform.tf_class()
ctl = controllers.control()
class globals(object):
    
    def base_Hi(self,assetName,modName=''):
        
        """
        Global Hi setup
        Args:
            assetName: Name of the asset :String Data 
            modName: name of the base parent group/module name

        Returns:
            Global group 

        Example:
            import sys
            sys.path.append('E:\frostCode\src')
            from src.modules.frostRig import Rig_Global
            var = Rig_Global.globals()
            var.global_Hi('Test Asset') 
        """
        #creating main network Nodes
        if modName !='':
            pass
        else:
            raise RuntimeError('Mod name not given')




        #creating main global groups
        rig_global_grp = tn.create_transform(Trname='%s'%modName,Data = assetName)
        rig_guide_grp = tn.create_transform(Trname='%s_guides'%modName,Data = assetName+'_guides')
        rig_controls_grp = tn.create_transform(Trname='%s_controls'%modName,Data = assetName+'_controls')
        rig_skeleton_grp = tn.create_transform(Trname='%s_skeleton'%modName,Data = assetName+'_skeleton')
        rig_misc_grp = tn.create_transform(Trname='%s_misc'%modName,Data = assetName+'_misc')

        #add message attrs for network
        tn.add_network_attr(rig_global_grp,'%s_input_network'%modName)
        tn.add_network_attr(rig_global_grp,'%s_output_network'%modName)

        tn.add_network_attr(rig_guide_grp,'%s_guide_output_network'%modName)
        tn.add_network_attr(rig_guide_grp,'%s_guide_input_network'%modName)

        tn.add_network_attr(rig_controls_grp,'%s_control_output_network'%modName)
        tn.add_network_attr(rig_controls_grp,'%s_control_input_network'%modName)        


        tn.add_network_attr(rig_skeleton_grp,'%s_skeleton_output_network'%modName)
        tn.add_network_attr(rig_skeleton_grp,'%s_skeleton_input_network'%modName)     
           

        pm.parent([rig_guide_grp,rig_controls_grp,rig_skeleton_grp,rig_misc_grp],rig_global_grp)
        return [rig_global_grp,rig_guide_grp,rig_controls_grp,rig_skeleton_grp,rig_misc_grp]
        
    def global_hi(self,globalGrps = []):
        if len(globalGrps)!= 5:
            raise RuntimeError('Not enough args provided')
        
        rig_global_grp=globalGrps[0]
        rig_guide_grp=globalGrps[1]
        rig_controls_grp=globalGrps[2]
        rig_skeleton_grp=globalGrps[3]
        rig_misc_grp=globalGrps[4]

        #creating global guides
        world_base_gd = pm.PyNode(ctl.create_bfr_guide(guideName='world_base',parent=rig_guide_grp))
        world_01_gd = pm.PyNode(ctl.create_bfr_guide(guideName='world_01',parent=rig_guide_grp))
        world_02_gd = pm.PyNode(ctl.create_bfr_guide(guideName='world_02',parent=rig_guide_grp))
        cog_01_gd = pm.PyNode(ctl.create_bfr_guide(guideName='cog_01',parent=rig_guide_grp))
        setting_01_gd = pm.PyNode(ctl.create_bfr_guide(guideName='setting_01',parent=rig_guide_grp))

        #creating global controls
        World_01_ctrl = pm.PyNode(ctl.create_bfr_control(shape_array = 'Global_shape',Ctlname = 'World_01',color='Yellow',parent = rig_controls_grp,ctrl_volume=.05))
        World_02_ctrl = pm.PyNode(ctl.create_bfr_control(shape_array = 'fat_cross_shape',Ctlname = 'World_02',color='Teal',parent = rig_controls_grp,ctrl_volume=.03,shape_scale=.7))
        COG_ctrl = pm.PyNode(ctl.create_bfr_control(shape_array = 'COG_Shape',Ctlname = 'COG',color='Yellow',parent = rig_controls_grp,ctrl_volume=.03))
        setting_ctrl = pm.PyNode(ctl.create_bfr_control(shape_array = 'setting_shape',Ctlname = 'Setting',color='Teal',parent = rig_controls_grp,ctrl_volume=.03,shape_scale=.5))
            

        #matrix_setup_guides
        world_base_gd.worldMatrix[0]>>world_01_gd.offsetParentMatrix
        world_01_gd.worldMatrix[0]>>world_02_gd.offsetParentMatrix
        world_02_gd.worldMatrix[0]>>cog_01_gd.offsetParentMatrix
        cog_01_gd.worldMatrix[0]>>setting_01_gd.offsetParentMatrix

        
        #matrix_setup_ctrls
        w1_to_w2_mltMtx = pm.createNode('multMatrix',n = 'world_01_to_world_02')
        w2_to_cog_mltMtx = pm.createNode('multMatrix',n = 'world_02_to_COG')
        cog_to_setting_mltMtx = pm.createNode('multMatrix',n = 'COG_to_setting')

        world_01_gd.worldMatrix[0]>>World_01_ctrl.offsetParentMatrix

        world_02_gd.worldMatrix[0]>>w1_to_w2_mltMtx.matrixIn[0]
        world_01_gd.worldInverseMatrix[0]>>w1_to_w2_mltMtx.matrixIn[1]
        World_01_ctrl.worldMatrix[0]>>w1_to_w2_mltMtx.matrixIn[2]
        w1_to_w2_mltMtx.matrixSum>>World_02_ctrl.offsetParentMatrix

        cog_01_gd.worldMatrix[0]>>w2_to_cog_mltMtx.matrixIn[0]
        world_02_gd.worldInverseMatrix[0]>>w2_to_cog_mltMtx.matrixIn[1]
        World_02_ctrl.worldMatrix[0]>>w2_to_cog_mltMtx.matrixIn[2]
        w2_to_cog_mltMtx.matrixSum>>COG_ctrl.offsetParentMatrix

        setting_01_gd.worldMatrix[0]>>cog_to_setting_mltMtx.matrixIn[0]
        cog_01_gd.worldInverseMatrix[0]>>cog_to_setting_mltMtx.matrixIn[1]
        COG_ctrl.worldMatrix[0]>>cog_to_setting_mltMtx.matrixIn[2]
        cog_to_setting_mltMtx.matrixSum>>setting_ctrl.offsetParentMatrix







        

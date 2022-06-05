#Global_ctrl_setup
from ..transforms import transform as trf
transform = trf.tf_class()
class globals(object):
    
    def global_Hi(self,assetName):
        """
        Global Hi setup
        Args:
            assetName: Name of the asset :String Data 

        Returns:
            Global group 

        Example:
            import sys
            sys.path.append('E:\frostCode\src')
            from src.modules.frostRig import Rig_Global
            var = Rig_Global.globals()
            var.global_Hi('Test Asset') 
        """
        #crerating main global groups
        rig_global_grp = transform.create_transform(Trname='rig_global',Data = assetName)
        rig_guide_grp = transform.create_transform(Trname='guides',parent=rig_global_grp,Data = assetName)
        rig_controls_grp = transform.create_transform(Trname='controls',parent=rig_global_grp,Data = assetName)
        rig_skeleton_grp = transform.create_transform(Trname='skeleton',parent=rig_global_grp,Data = assetName)
        rig_misc_grp = transform.create_transform(Trname='misc',parent=rig_global_grp,Data = assetName)

        #creating global guides
        



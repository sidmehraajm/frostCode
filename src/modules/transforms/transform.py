import pymel.core as pm
class tf_class(object):
    def create_transform(self,Trname = '_empty_grp',parent= '',Data = ''):
        """
        create_transform
        Args:
            Trname: Name of the transform : String
            parent: Parent of the given transform : Optional arg 
            Data: Data to put in transfroms data attribute : String

        Returns:
            Returns Transform Name

        Raises:
            Raises Runtime error if parent string is given and that is not found in the scene

        example: 
            var = tf_class()
            var.create_transform(Trname = 'Test',parent= 'rig_global',Data = 'Test Data')
        """

        trf = pm.createNode('transform', n = Trname)
        dataAtr = pm.addAttr(trf,dt = 'string',ln = 'data')
        trf.data.set(Data)
        if parent !='':
            try:
                pm.parent(trf,parent)
            except:
                raise RuntimeError('Parent not found')
        else:
            pass
        return trf

    def add_data_attr(self,Trname = None,Data = ''):
        if Trname!=None:
            pass
        else:
            raise RuntimeError('Transform not given or not an applicable obj')

        trf = pm.PyNode('Trname')
        try:
            dataAtr = pm.addAttr(trf,dt = 'string',ln = 'data')
            trf.data.set(Data)
        except:
            try:
                trf.data.set(Data)
            except:
                raise RuntimeError('Failed to add/set Data Attribute')

            


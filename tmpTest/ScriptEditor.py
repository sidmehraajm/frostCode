import pymel.core as pm


if pm.window('ScriptEditorX',ex=True):
	pm.deleteUI('ScriptEditorX')
	
if cmds.windowPref('ScriptEditorX', exists=True ):
   cmds.windowPref( 'ScriptEditorX', r=1 )

wind = pm.window( 'ScriptEditorX',t = 'Script Editor Mini',w=650,h=800,s=1,bgc = [(.17),(.18),(.19)],le = 10,te = 10,mb=1,nde=1)
Tab = pm.tabLayout('Tabs',p='ScriptEditorX',tc =1,stb=1,snt=1,ntc = 'NewScriptTab()')


FileMenu = pm.menu(l = 'Files',to =0)
FileMenuItem1 = pm.menuItem('OpenSc',l = 'Open Script',p = FileMenu)
FileMenuItem2 = pm.menuItem('SaveSc',l = 'Save Script',p = FileMenu)
FileMenuItem3 = pm.menuItem('SvScToShelf',l = 'Save Script to Shelf',p = FileMenu)

EditMenu = pm.menu(l = 'Edit',to =0)
EditMenuItem1 = pm.menuItem('ClearOutput',l = 'Clear Output',p = EditMenu)
EditMenuItem2 = pm.menuItem('ClearInput',l = 'Clear Input',p = EditMenu)
EditMenuItem3 = pm.menuItem('ClearBoth',l = 'Clear Both',p = EditMenu)

CmdMenu = pm.menu(l = 'Command',to =0)
CmdMenuItem1 = pm.menuItem('ShowLines',l = 'Show Line Numbers',p = CmdMenu,icb =1)
CmdMenuItem2 = pm.menuItem('CmdComp',l = 'Command Completion',p = CmdMenu,icb =1)
CmdMenuItem3 = pm.menuItem('ToolHelp',l = 'Show Toolkit help',p = CmdMenu,icb =1)

HelpMenu = pm.menu(l = 'Help',to =0)
HelpMenuItem1 = pm.menuItem('ShowMayaTechnicalDocs',l = 'Show Maya Technical Docs',p = HelpMenu,icb =1)
HelpMenuItem2 = pm.menuItem('About',l = 'About Author',p = HelpMenu,icb =1)

ExtraEdtr = pm.menu(l = 'Extras',to =0)
ExtraEdtrItem = pm.menuItem('WorkspaceEditor',l = 'Show Extra Script Editor',p = ExtraEdtr,icb =1,c ='ScriptTmpWorkspace()')



pm.showWindow('ScriptEditorX')


#formMain = pm.formLayout('ScEdtMainForm',w=650,h=1000)


def ScriptTmpWorkspace():

    def UItry():
        Tab = tabLayout('TabsWps',tc =1,stb=1,snt=1,ntc = 'NewScriptTab()')
    
    if pm.workspaceControl('Asdd',ex=1):
        pm.deleteUI('Asdd')
        pm.workspaceControl('Asdd',e=1,cl=1)
    pm.workspaceControl('Asdd',rt =0,fl =1,uiScript= 'UItry()',l= 'Attachable ScriptEditor')
    

    #pm.workspaceControl('Asdd',e=1,uiScript= 'UItry()')

    
    
    
class ScriptTabForm(object):
    def __init__(self,object):
        self.Form = pm.columnLayout(w=650,h=800,p = object)
        self.OutputScrpt = pm.cmdScrollFieldReporter(w = 645,h = 200,p=self.Form,bgc = [(.17),(.18),(.19)])
        self.InputScrpt = pm.cmdScrollFieldExecuter(w = 645,h = 600,p=self.Form,sth=0,sln=1,cco=1, sourceType="python",opc=0,bgc = [(.17),(.19),(.17)])

        
        
    
def NewScriptTab(ob = 'Tabs'):
    NewTab = ScriptTabForm(ob)
        
        
         
    
    
    
 
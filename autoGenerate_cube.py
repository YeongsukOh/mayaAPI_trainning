import maya.cmds as cmds

selList = cmds.ls(sl = True)

for item in selList:
    cube = cmds.polyCube()[0]
    cmds.delete(cmds.parentConstraint(item, cube, mo = False))
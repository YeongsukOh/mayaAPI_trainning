import maya.OpenMaya as openMaya
import maya.cmds as cmds

# making empty selction list
mSelectionList = openMaya.MSelectionList()

# add some item that I want to modify
mSelectionList.add("pPlane1")

# DagPath of selected item
# ex) group | group_off | pPlane1

mDagPath = openMaya.MDagPath()

# in mSelectionList, index[0] item put in mDagPath
mSelectionList.getDagPath(0, mDagPath)
print(mDagPath.fullPathName())

# need to check what MObject do ?
mObj = openMaya.MObject()

# also, what does getDepenNode do ?
mSelectionList.getDependNode(0, mObj)
print(mObj.apiTypeStr())

# contacting with the shape node of the item in mSelectionlist
mFnMesh = openMaya.MFnMesh(mDagPath)
print(mFnMesh.name())
import maya.OpenMaya as openMaya
import maya.cmds as cmds

mSelectionList = openMaya.MSelectionList()
mSelectionList.add("pPlane1")

mDagPath = openMaya.MDagPath()
mSelectionList.getDagPath(0, mDagPath)

print(mDagPath.fullPathName())

mObj = openMaya.MObject()
mSelectionList.getDependNode(0,mObj)

print(mObj.apiTypeStr())

mFnMesh = openMaya.MFnMesh(mDagPath)
print(mFnMesh.name())

mPlugArray = openMaya.MPlugArray()
mFnMesh.getConnections(mPlugArray)

print(mPlugArray.length())
# pPlaneShape1.instObjGroups[0]
print(mPlugArray[0].name())
# pPlaneShape1.inMesh
print(mPlugArray[1].name())

mPlugArray_connection = openMaya.MPlugArray()
mPlugArray[1].connectedTo(mPlugArray_connection, True, False)

print(mPlugArray_connection.length())
# polyPlane1.output
print(mPlugArray_connection[0].name())

mObj2 = mPlugArray_connection[0].node()

# polyPlane1
mFnDependNode_2 = openMaya.MFnDependencyNode(mObj2)

print(mFnDependNode_2.name())

mPlugWidth = mFnDependNode_2.findPlug("width")
mPlugHeight = mFnDependNode_2.findPlug("height")

mPlugWidth.setInt(30)
mPlugHeight.setInt(30)

mPlug_subWidth = mFnDependNode_2.findPlug("subdivisionsWidth")
mPlug_subHeight = mFnDependNode_2.findPlug("subdivisionsHeight")

mPlug_subWidth.setInt(30)
mPlug_subHeight.setInt(30)
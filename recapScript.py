import maya.OpenMaya as openMaya

mselectionList = openMaya.MSelectionList()
mselectionList.add("pPlane1")

mDagPath = openMaya.MDagPath()

mselectionList.getDagPath(0, mDagPath)

print(mDagPath.fullPathName())

mObj = openMaya.MObject()

mselectionList.getDependNode(0,mObj)

mFnMesh = openMaya.MFnMesh(mDagPath)
print(mFnMesh.fullPathName())

print(mObj.apiTypeStr())

mFnDependNode = openMaya.MFnDependencyNode(mObj)
print(mFnDependNode.name())

mPlugArray = openMaya.MPlugArray()
mFnMesh.getConnections(mPlugArray)

print(mPlugArray.length())
print(mPlugArray[0].name())
print(mPlugArray[1].name())

mPlugArray_connection = openMaya.MPlugArray()
mPlugArray[1].connectedTo(mPlugArray_connection,True, False)

print(mPlugArray_connection.length())
print(mPlugArray_connection[0].name())

mObj_2 = mPlugArray_connection[0].node()
mFnDependNode2 = openMaya.MFnDependencyNode(mObj_2)

print(mFnDependNode2.name())

mPlug_width = mFnDependNode2.findPlug("width")
mPlug_height = mFnDependNode2.findPlug("height")

print(mPlug_width.asInt())
print(mPlug_height.asInt())

mPlug_width.setInt(10)
mPlug_height.setInt(10)
import maya.OpenMaya as OpenMaya
# MSelectionList
# MObject
# MDagPath

#1. create a selection list
mSel = OpenMaya.MSelectionList()
mSel.add("pPlane1")

#2. create MObject and MDagPath
mObj = OpenMaya.MObject()
mDagPath = OpenMaya.MDagPath()

#3. request Dependency Node and Dag Path of the object
mSel.getDependNode(0, mObj)
mSel.getDagPath(0, mDagPath)

print(mDagPath.fullPathName())

#4. create Mesh function set
mFnMesh = OpenMaya.MFnMesh(mDagPath)
print(mFnMesh.fullPathName())

#5. create Dependency node function set
mFnDependNode = OpenMaya.MFnDependencyNode(mObj)

print (mFnDependNode.name())

#6. get all the connection of a shape node
mPlugArray = OpenMaya.MPlugArray()
mFnMesh.getConnections(mPlugArray)

mPlugArray.length()
print(mPlugArray[0].name())
print(mPlugArray[1].name())

mPlugArray_connections = OpenMaya.MPlugArray()
mPlugArray[1].connectedTo(mPlugArray_connections,True, False)

print(mPlugArray_connections.length())

# cannot be used : len(mPlugArray_connections)

print(mPlugArray_connections[0].name())

mObj2 = mPlugArray_connections[0].node() 

mFnDependNode2 = OpenMaya.MFnDependencyNode(mObj2)

print (mFnDependNode2.name())

mPlug_width = mFnDependNode2.findPlug("width")
mPlug_height = mFnDependNode2.findPlug("height")

print (mPlug_width.asInt())
print (mPlug_height.asInt())

mPlug_subWidth = mFnDependNode2.findPlug("subdivisionsWidth")
mPlug_subHeight = mFnDependNode2.findPlug("subdivisionsHeight")

print (mPlug_subWidth.asInt())
print (mPlug_subHeight.asInt())

mPlug_subWidth.setInt(10)
mPlug_subHeight.setInt(10)
import maya.OpenMaya as OpenMaya

# making empty list with OpenMaya
# we can add and remove any object in maya scene
# methods of creating, add/remove, walking, etc
mSelectionList = OpenMaya.MSelectionList()

# add some item into the list with DAG path
mSelectionList.add("campus01|room01|computer_01")

# the object is capable of containing DAG path of the object
mDagPath = OpenMaya.MDagPath()

# put the index[0] item of the mSelectionList into mDagPath
mSelectionList.getDagPath(0,mDagPath)

# the function to print fullPath of the mSelection Item
print(mDagPath.fullPathName())

# specilized handle that can access modeling, animation, lighting, etc
mObj = OpenMaya.MObject()

# mSelectionList's index[0] item send to mObj
mSelectionList.getDependNode(0, mObj)
print(mObj.apiTypeStr())
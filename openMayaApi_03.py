import maya.OpenMaya as openMaya
import maya.OpenMayaMPx as openMayaMPx
import sys

commandName = "pluginCommand"

# derived class should have doit function
class PluginCommand(openMayaMPx.MPxCommand):

    def __init__(self):
        openMayaMPx.MPxCommand.__init__(self)
    
    def doIt(self, argList):
        print("do it")
    
# create command 
def cmdCreator():
    return openMayaMPx.asMPxPtr(PluginCommand()) # this will be pointer

def initializePlugin(mobject):
    mplugin = openMayaMPx.MFnPlugin(mobject)

    try:
        mplugin.registerCommand(commandName, cmdCreator)
    except:
        sys.stderr.write("Failed to register command : " + commandName)

def uninitializePlugin(mobject):
    mplugin = openMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(commandName)
    except:
        sys.stderr.write("Failed to de-register command : " + commandName)


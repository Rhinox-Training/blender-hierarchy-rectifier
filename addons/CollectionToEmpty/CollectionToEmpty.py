bl_info = {
    "name": "Convert Collection to Empty Structure",
    "author": "Glenn Quintyn | Rhinox",
    "version": (1, 2),
    "blender": (3, 3, 1),
    "location": "View3D",
    "description": "Converts all the collections under the scene collection to the equivalent strucut but made out of empty objects",
    "warning": "",
    "doc_url": "",
    #"category": "Add Mesh",
}

import bpy
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
    PropertyGroup,
)
from bpy_extras.object_utils import AddObjectHelper

class ConvertCollectionToEmpty(Operator):
    """Converts all the Collections in the scene collection view to an Empty object"""   # Use this as a tooltip for menu items and buttons.
    bl_idname = "tool.converttoempty"           # Unique identifier for buttons and menu items to reference.
    bl_label = "Convert collection to empty"    # Display name in the interface.
    bl_description = "Converts all the collections under the scene collection to the equivalent but made out of empty objects"
    bl_options = {'REGISTER', 'UNDO'}           # Enable undo for the operator.

    def execute(self, context):
        #gets all the collections that are directly connect to the "scene collection"
        sCollection = bpy.context.scene.collection.children
        print("\nStart\n")
        #looping over the root collections and then making an equivelant empty object
        for rootCol in sCollection:
            rootEmptyObj = bpy.data.objects.new("empty", None)#check if exists and if so don't re-create
            bpy.context.scene.collection.objects.link(rootEmptyObj)
            rootEmptyObj.name = rootCol.name
            parentCol(rootCol, rootEmptyObj)

        return {'FINISHED'}

#this funtions looks inside the given collection and re-parents the objects (if there are any)
#then it loops over all the collections inside of it and re-parents al of its objects
#if there are more collections under here then it recursively adds their objects aswell
def parentCol(_colParent, _objParent):
    #print("funbc")
    #if len(_colParent.objects) > 0:
        #print("inside")
    
    
    
    parentObjs = _colParent.objects
    for obj in parentObjs:
        #parentObjs.unlink(obj)
        #bpy.context.scene.collection.objects.link(obj)
        obj.parent = _objParent
        #reChilding(obj)
            
#            if obj.parent == None:
#                parentObjsunlink(obj)
#                bpy.context.scene.collection.objects.link(obj)
#                obj.parent = _objParent
    
    for col in _colParent.children:
        newObj = bpy.data.objects.new("empty", None)
        bpy.context.scene.collection.objects.link(newObj)
        newObj.name = col.name
        newObj.parent = _objParent
    
        if len(col.objects) > 0:
            objs = col.objects
            
            #props need to do a recursive search inside the object's objects
            for obj in objs:
                #for childObj in obj.children
                #col.objects.unlink(obj)
                bpy.context.scene.collection.objects.link(obj)
                obj.parent = newObj
                
        parentCol(col, newObj)

def reChilding(parent):
    #go over childs and reparent them if they have children go over it recursively
    #print("parent: ")
    #print(parent.name)
    children = parent.children
    for child in children:
        #parent.unlink(child)
        #bpy.context.scene.collection.objects.link(child)
        child.parent = parent
        #print("child:")
        #print(child.name)
        if len(child.children) > 0:
            reChilding(child)
            
        
#def recursiveChildObjects():

#functions needed for the UI buttons
def menu_item_draw_func(self, context):
    self.layout.separator()
    self.layout.operator(ConvertCollectionToEmpty.bl_idname, text="Convert To Empties", icon='PLUGIN')

#this function gets called by blender when running the addon
def register():
    bpy.utils.register_class(ConvertCollectionToEmpty)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_item_draw_func)
 
#this function gets called by blender when running the addon
def unregister():
    bpy.utils.unregister_class(ConvertCollectionToEmpty)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_item_draw_func)
    
# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
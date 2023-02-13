bl_info = {
    "name": "Convert Collection to Empty Structure",
    "author": "Your Name Here",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Converts all the collections in the scene collection to empty objects",
    "warning": "",
    "doc_url": "",
    #"category": "Add Mesh",
}

import bpy
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper

class ConvertCollectionToEmpty(Operator):
    """Converts all the Collections in the scene collection view to an Empty object"""   # Use this as a tooltip for menu items and buttons.
    bl_idname = "tool.converttoempty"           # Unique identifier for buttons and menu items to reference.
    bl_label = "Convert collection to empty"    # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}           # Enable undo for the operator.


    def execute(self, context):
              
        rez_list = []
        
        #using index 0 as there is only one scene collection, meaning there is no use in copying this one aswell.
        collections(bpy.context.scene.collection.children[0], rez_list, None)
        print(rez_list)
        #    if collection.all_objects.count > 0:
        #print(len(bpy.context.collection.values()))
        
        return {'FINISHED'}

def collections(collection, col_list, parentObj):
    col_list.append(collection.name)    
    print(len(collection.objects))
    
    emptyObj
    
    if len(collection.objects) > 0:    
        objName = collection.name
        emptyObj = bpy.data.objects.new(objName, None)
        emptyObj.empty_display_size = 0.0001
        emptyObj.empty_display_type = 'PLAIN_AXES'   
        bpy.context.scene.collection.objects.link(emptyObj)
        
        if parentObj is not None:
            emptyObj.parent = parentObj
        
        for obj in collection.objects:
            obj.parent = emptyObj
            
    for sub_collection in collection.children:
        collections(sub_collection, col_list, emptyObj)






def menu_item_draw_func(self, context):
    self.layout.separator()
    self.layout.operator(ConvertCollectionToEmpty.bl_idname, text="conversion", icon='PLUGIN')

#this function gets called by blender when running the addon
def register():
    bpy.utils.register_class(ConvertCollectionToEmpty)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_item_draw_func)
 
#this function gets called by blender when running the addon
def unregister():
    bpy.utils.unregister_class(ConvertCollectionToEmpty)
    #bpy.types.VIEW3D_MT_object_context_menu.remove(menu_item_draw_func)
    
# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
import bpy

bl_info = {
    "name" : "Project active camera background image.",
    "author" : "Martijn Versteegh",
    "version" : (1, 0),
    "blender" : (2, 80, 0),
    "description" : "Project the active camera background image onto the mesh from the camera.",
    "warning" : "",
    "doc_url" : "",
    "tracker_url" : "",
    "category" : "Paint",
}



class ProjectActiveCameraBackgroundImage(bpy.types.Operator):
    """Project the active Camera's Background Image onto the current mesh."""
    bl_idname = "camera.projectbackgroundimage"
    bl_label = "Project Camera Background Image"
    bl_description = "This operator projects the background image of the currently active camera onto the mesh."
    bl_options = { "UNDO" }
    
    
    
    def execute(self, context):
        camera = context.scene.camera
        bgimage = camera.data.background_images[0]
        bgimage.image.gl_load(frame=bgimage.image_user.frame_current)
        bpy.ops.paint.project_image(image=bgimage.image.name)
        bgimage.image.gl_free()
        return { "FINISHED" }
    #end execute
    
    def invoke(self, context, events):
        return self.execute(context)
    #end invoke()
    
    @classmethod
    def poll(cls, context):
        if context.mode != 'PAINT_TEXTURE':
            return False
        if not context.scene.camera:
            return False
        
        if context.scene.camera.data.background_images.items():
            return True
        
        return False
    #end poll
#end class


class ProjectAnimatedCameraBackrounds(bpy.types.Operator):
    
    @classmethod
    def poll(cls, context):
        if context.mode != 'PAINT_TEXTURE':
            return False
        if not context.scene.camera:
            return False
        
        if context.scene.camera.data.background_images.items():
            return True
        
        return False
    #end poll


    def execute(self, context):

        camera = context.scene.camera
        bgimage = camera.data.background_images[0]
        bpy.ops.paint.project_image(image=bgimage.image.name)
        return { "FINISHED" }
    #end execute



    def invoke(self, context, events):
        return self.execute(context)
    #end invoke()


#end class    

def draw_button(self, context):
    layout = self.layout
    layout.operator("camera.projectbackgroundimage", text = "Apply Camera BG Image")

def register():
    bpy.utils.register_class(ProjectActiveCameraBackgroundImage)
    bpy.types.VIEW3D_PT_tools_imagepaint_options_external.append(draw_button)
#end register()    

def unregister():
    bpy.types.VIEW3D_PT_tools_imagepaint_options_external.remove(draw_button)
    bpy.utils.unregister_class(ProjectActiveCameraBackgroundImage)
#end unregister

#if we are run as a script, register out class    
if __name__ == "__main__":
    #unregister()
    register()





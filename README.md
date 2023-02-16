# Blender Hierarchy Rectifier

This is the python script of the add-on that will convert the collection hierarchy into the same hierarchy but using empty objects instead.
This is because collections is a blender exclusive thing and it does not get saved inside the .fbx file.
Empty objects do get saved inside the .fbx file, making it possible to retain the hierarchy when using it inside Unity.

## Installing the addon

Open blender

At the top: “**Edit**” > “**Preferences**”

In the “Add-ons” tab. Click on “Install…”

![image installing Add-on](https://user-images.githubusercontent.com/76707656/219386702-14533f7a-e274-43b6-9736-fcec1d8352fb.png)


Navigate to the location of where you download the “CollectionToEmpty.py” add-on.

Select it and press “**Install Add-on**”

The following should show up.

Finally, click on the check box next to the add-on name to enable it.

![image activating Add-on](https://user-images.githubusercontent.com/76707656/219388248-feed7cb1-c9e9-4231-adfd-31418ac0ddea.png)

## How to use the addon

Right click anywhere in the 3D view and get the “Object Context Menu”.

Select the option “Convert to Empties”.

<!---![image Object Context Menu](https://user-images.githubusercontent.com/76707656/219388591-a2e1d782-4859-4dd2-b400-de2c5deaa6a3.png)-->
<img src="https://user-images.githubusercontent.com/76707656/219388591-a2e1d782-4859-4dd2-b400-de2c5deaa6a3.png" height="500">

## Additional
#### TIP:
In the blender Viewport Shading UI. Select the option “Solid”. This will ease the processing load of blender make the addon run faster on more complex/larger scenes.

![image Viewport Shading](https://user-images.githubusercontent.com/76707656/219388742-191309ec-6793-47bf-9594-6efe413f0eee.png)

# License

Apache-2.0 © Rhinox NV

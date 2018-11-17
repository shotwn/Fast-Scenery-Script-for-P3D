import os
import time
from colorama import init, Fore, Back
init()


# Get current dir
rootdir = os.path.dirname(os.path.realpath(__file__))

# Addon name to use
addon_name = os.path.split(rootdir)[1]
addon_xml_file = os.path.join(rootdir, "add-on.xml")
# Warn user for replacement
if os.path.isfile(addon_xml_file):
    print(Fore.RED,"   [WARNING] ", Fore.RESET)
    print("""   This script will replace {0}""".format(addon_xml_file))
    input("Press Enter to continue or CTRL+C to exit.")

# Check for directory
upper_dir = os.path.split(os.path.split(rootdir)[0])[1]
if upper_dir != "Prepar3D v4 Add-ons":
    print(Fore.RED,"   [WARNING] ", Fore.RESET)
    print("""
    Current directory : {0}
    You should use this script within a folder, inside of default Prepar3D v4 Add-ons directory. 
    For example:
        C:\\username\\Documents\\Prepar3D v4 Add-ons\\Addon Scenery
    
    If you are using this script outside of default directories you should add created add-on.xml to add-ons.cfg manually.

    """.format(rootdir))
    input("Press Enter to continue or CTRL+C to exit.")

# List directories within current dir
for dirs in os.walk(rootdir):
    directories = dirs[1]
    break

# List to keep each scenery directory
addon_components = []
for scenery in directories:
    # Exception, if folder name is etc pass.
    if scenery == "etc":
        continue

    # Path to scenery
    scenery_path = os.path.join(rootdir, scenery)
    print("--- Checking {0}".format(scenery_path))
    
    print
    if not os.path.isdir(os.path.join(scenery_path, "texture")):
        print(Fore.RED, """   [ERROR]
    Directory doesn't have texture folder, passing this directory.
        """, Fore.RESET)
        continue
    
    if not os.path.isdir(os.path.join(scenery_path, "scenery")):
        print(Fore.RED, """   [ERROR]
    Directory doesn't have scenery folder, passing this directory.
        """, Fore.RESET)
        continue

    component ="""
    <AddOn.Component>
        <Category>Scenery</Category>
        <Path>{1}</Path>
        <Name>{0}</Name>
    </AddOn.Component>""".format(scenery, scenery_path)
    addon_components.append(component)

    print(Fore.GREEN, """    Added {0}""".format(scenery), Fore.RESET)
    print()

# Check if do we have any addon components
if len(addon_components) < 1:
    print("Non of the folders within this directory have scenery files inside.")
    input("Press Enter to exit.")
    exit()

with open (addon_xml_file, 'w') as xml_file:
    format_out = """<?xml version="1.0" encoding="UTF-8"?>
    <SimBase.Document Type="AddOnXml" version="4,0" id="add-on">
    <AddOn.Name>{0}</AddOn.Name>
    <AddOn.Description>Content for scenery</AddOn.Description>{1}
</SimBase.Document>
        """.format(addon_name, "".join(addon_components))

    xml_file.write(format_out)

print("--- Successful.")
print(Fore.GREEN, """                            
    'add-on.xml' write complete.       
    {0} sceneries listed in the xml.    """.format(len(addon_components)), Fore.RESET)

print(Fore.GREEN)
input("""
    ***   Press Enter to exit   ***
""")

"""
Additional components for future development
<AddOn.Component>
<Category>Effects</Category>
<Path>E:\P3D Addons\Aerosoft Dillingham\Effects</Path>
</AddOn.Component>
<AddOn.Component>
<Category>Sound</Category>
<Path>E:\P3D Addons\Aerosoft Dillingham\Sound</Path>
</AddOn.Component>
"""


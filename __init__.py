from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, log_to_console, Path
import os
import filecmp
import shutil
import __main__




WEB_DIRECTORY = './js'
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']



extentions_folder = os.path.join(os.path.dirname(os.path.realpath(__main__.__file__)),
                                 "web" + os.sep + "extensions" + os.sep + "IamMEsNodes")
javascript_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "js")
outdate_file_list = ['nodes_js.js']

if not os.path.exists(extentions_folder):
    log_to_console("Making the 'web\extensions\IamMEsNodes' folder")
    os.mkdir(extentions_folder)
else:
    for i in outdate_file_list:
        outdate_file = os.path.join(extentions_folder, i)
        if os.path.exists(outdate_file):
            os.remove(outdate_file)

result = filecmp.dircmp(javascript_folder, extentions_folder, ignore=[file.name for file in Path(javascript_folder).iterdir() if file.name.startswith(".")])
if result.left_only or result.diff_files:
    log_to_console("Update to javascripts files detected")
    file_list = list(result.left_only)
    file_list.extend(x for x in result.diff_files if x not in file_list)

    for file in file_list:
        log_to_console(f"Copying {file} to extensions folder")
        src_file = os.path.join(javascript_folder, file)
        dst_file = os.path.join(extentions_folder, file)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_file)
else:
    log_to_console("No update to javascript files found")
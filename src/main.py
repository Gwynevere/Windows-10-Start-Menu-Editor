import json
from src.core.Image import *
from src.io.Crawler import get_filtered_list, get_dirs_r
from src.core.XMLEditor import *
from src.io.File import *
from src.config.Constant import *
from src.utils.Rand import *

f = open(get_current_wd() + '\\config.json')
config = json.load(f)

tiles_locations = config['tiles_locations']
lnk_paths = get_filtered_list(config['path_images'], tiles_locations)
bg_images_paths = get_dirs_r(config['path_background_images'])
text_color = config['text_color']
text_color_fill = config['text_color_fill']
color = config['background_color']

for path in lnk_paths:

    icon_path = path.get('icon_path')
    icon_name = get_file_name(icon_path).replace('.fill', '')
    icon_fill_mode = True if get_file_name(icon_path).split('.').__contains__('fill') else False

    file_exe_path = get_lnk_file_target(path.get('lnk_path'))
    file_exe_path_root = get_file_path(file_exe_path)
    file_exe_name = get_file_name(file_exe_path).replace('.exe', '')

    print(path.get('lnk_path'))
    print(file_exe_path)
    print(icon_path)

    ve_xml_file = file_exe_path_root + '\\' + file_exe_name + "." + XML_VEM_FILE_NAME + '.' + XML_FILE_EXT
    md_folder = file_exe_path_root + '\\' + XML_MD_FOLDER_NAME
    md_xml_file_m = md_folder + '\\' + XML_MD_M_FILE_NAME.replace('{}', file_exe_name) + '.' + XML_FILE_EXT
    md_img_file_m = md_folder + '\\' + PNG_MD_M_FILE_NAME.replace('{}', file_exe_name) + '.' + PNG_FILE_EXT
    md_xml_file_s = md_folder + '\\' + XML_MD_S_FILE_NAME.replace('{}', file_exe_name) + '.' + XML_FILE_EXT
    md_png_file_s = md_folder + '\\' + PNG_MD_S_FILE_NAME.replace('{}', file_exe_name) + '.' + PNG_FILE_EXT

    # check if xml visualElements file already exists under a different name
    # for file_name in list_dir(file_path_root):
    #    if XML_VEM_FILE_NAME + '.' + XML_FILE_EXT in file_name:
    #        ve_xml_file = file_path_root + '\\' + file_name
    #        break

    if path_exists(ve_xml_file):
        del_file(ve_xml_file)

    if path_exists(md_folder):
        del_dir(md_folder)

    create_folder(md_folder)

    image_b_64 = encode_64(icon_path)

    if not icon_fill_mode:
        image_r_med = fill_with_bg(icon_path, bg_images_paths[rand(len(bg_images_paths))], IMG_RES_MED)
        # image_r_med = adjust(icon_path, IMG_RES_MED, int(IMG_RES_MED / 2.4))
    else:
        image_r_med = fill(icon_path, IMG_RES_MED)
    save(md_img_file_m, image_r_med)
    close(image_r_med)

    if not icon_fill_mode:
        image_r_min = fill_with_bg(icon_path, bg_images_paths[rand(len(bg_images_paths))], IMG_RES_MIN)
    else:
        image_r_min = fill(icon_path, IMG_RES_MIN * 2)
    save(md_png_file_s, image_r_min)
    close(image_r_min)

    ve_manifest_attrs = dict(
        display_name='on',
        logo_150=XML_MD_FOLDER_NAME + '\\' + PNG_MD_M_FILE_NAME.replace('{}', file_exe_name) + '.' + PNG_FILE_EXT,
        logo_70=XML_MD_FOLDER_NAME + '\\' + PNG_MD_S_FILE_NAME.replace('{}', file_exe_name) + '.' + PNG_FILE_EXT,
        foreground_text=text_color if not icon_fill_mode else text_color_fill,
        background_color=color
    )
    metadata_m_attrs = dict(
        ob=image_b_64,
        op=file_exe_path,
        h=str(TILE_IMG_MED_RES),
        w=str(TILE_IMG_MED_RES),
        x=str(TILE_IMG_MED_X),
        y=str(TILE_IMG_MED_Y)
    )
    metadata_s_attrs = dict(
        ob=image_b_64,
        op=file_exe_path,
        h=str(TILE_IMG_MIN_RES),
        w=str(TILE_IMG_MIN_RES),
        x=str(TILE_IMG_MIN_X),
        y=str(TILE_IMG_MIN_Y)
    )

    run_ve_manifest(ve_xml_file, ve_manifest_attrs)
    run_metadata(md_xml_file_m, metadata_m_attrs)
    run_metadata(md_xml_file_s, metadata_s_attrs)

    edit_file_time(path.get('lnk_path'))
    print()

print("Press key to exit ...")
input()

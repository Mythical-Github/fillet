import os

import shutil

from fillet import file_io, data_structures, logging


def get_game_enum_value_automatically(install_directory: str) -> str:
    if os.path.isfile(os.path.normpath(f'{install_directory}/CoDWaW.exe')):
        return data_structures.Games.CALL_OF_DUTY_WORLD_AT_WAR.value
    elif os.path.isfile(os.path.normpath(f'{install_directory}/BlackOps.exe')):
        return data_structures.Games.CALL_OF_DUTY_BLACK_OPS_I.value
    elif os.path.isfile(os.path.normpath(f'{install_directory}/t6zm.exe')):
        return data_structures.Games.CALL_OF_DUTY_BLACK_OPS_II.value
    else:
        automatic_game_detection_error = f'Automatic game detection failed for directory at: "{install_directory}"'
        raise RuntimeError(automatic_game_detection_error)


def trim_call_of_duty_world_at_war_install(install_directory: str, skip_verification: bool):
    
    valid_files = [
        "iw_00.iwd"
        "iw_14.iwd",
        "iw_21.iwd",
        "iw_22.iwd",
        "iw_24.iwd",
        "iw_26.iwd",
        "localized_english_iw00.iwd",
        "localized_english_iw04.iwd",
    ]

    main_dir = os.path.normpath(f'{install_directory}/main')

    for file in file_io.get_all_files_in_tree(main_dir):
        if os.path.basename(file) not in valid_files:
            os.remove(file)

    file_io.remove_empty_directories_in_directory_tree(main_dir)
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/iw_00.iwd'), 'images')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/iw_22.iwd'), 'images')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/iw_22.iwd'), 'sound')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/iw_24.iwd'), 'images')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/iw_26.iwd'), 'sound')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/localized_english_iw00.iwd'), 'images')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/localized_english_iw00.iwd'), 'sound')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/localized_english_iw04.iwd'), 'images')
    file_io.remove_directory_from_zip_file(os.path.normpath(f'{main_dir}/localized_english_iw04.iwd'), 'sound')


def trim_call_of_duty_black_ops_i(install_directory: str, skip_verification: bool):
    
    valid_files = [
        "iw_00.iwd",
        "server.cfg"
    ]

    main_dir = os.path.normpath(f'{install_directory}/main')

    for file in file_io.get_all_files_in_tree(main_dir):
        if os.path.basename(file) not in valid_files:
            os.remove(file)

    file_io.remove_empty_directories_in_directory_tree(main_dir)


def trim_call_of_duty_black_ops_ii(install_directory: str, skip_verification: bool):

    valid_files = [
        "en_common_mp.ff",
        "en_common_zm.ff",
        "en_dlc1_load_zm.ff",
        "en_dlc2_load_zm.ff",
        "en_dlc3_load_zm.ff",
        "en_dlc4_load_zm.ff",
        "en_faction_cd_mp.ff",
        "en_faction_cd_sand_mp.ff",
        "en_faction_fbi_mp.ff",
        "en_faction_isa_mp.ff",
        "en_faction_isa_sand_mp.ff",
        "en_faction_multiteam_mp.ff",
        "en_faction_multiteam_snow_mp.ff",
        "en_faction_multiteam_wet_mp.ff",
        "en_faction_pla_mp.ff",
        "en_faction_pla_wet_mp.ff",
        "en_faction_pmc_mp.ff",
        "en_faction_pmc_snow_mp.ff",
        "en_faction_seals_mp.ff",
        "en_faction_seals_snow_mp.ff",
        "en_faction_seals_wet_mp.ff",
        "en_mp_bridge.ff",
        "en_mp_carrier.ff",
        "en_mp_castaway.ff",
        "en_mp_concert.ff",
        "en_mp_dig.ff",
        "en_mp_dockside.ff",
        "en_mp_downhill.ff",
        "en_mp_drone.ff",
        "en_mp_express.ff",
        "en_mp_frostbite.ff",
        "en_mp_hijacked.ff",
        "en_mp_hydro.ff",
        "en_mp_la.ff",
        "en_mp_magma.ff",
        "en_mp_meltdown.ff",
        "en_mp_mirage.ff",
        "en_mp_nightclub.ff",
        "en_mp_nuketown_2020.ff",
        "en_mp_overflow.ff",
        "en_mp_paintball.ff",
        "en_mp_pod.ff",
        "en_mp_raid.ff",
        "en_mp_skate.ff",
        "en_mp_slums.ff",
        "en_mp_socotra.ff",
        "en_mp_studio.ff",
        "en_mp_takeoff.ff",
        "en_mp_turbine.ff",
        "en_mp_uplink.ff",
        "en_mp_vertigo.ff",
        "en_mp_village.ff",
        "en_mp.ff",
        "en_patch_mp.ff",
        "en_patch_ui_mp.ff",
        "en_patch_ui_zm.ff",
        "en_patch_zm.ff",
        "en_so_zdclassic_zm_transit.ff",
        "en_so_zencounter_zm_transit.ff",
        "en_so_zsurvival_zm_transit.ff",
        "en_ui_mp.ff",
        "en_ui_zm.ff",
        "en_zm_buried.ff",
        "en_zm_highrise.ff",
        "en_zm_nuked.ff",
        "en_zm_prison.ff",
        "en_zm_tomb.ff",
        "en_zm_transit.ff"
    ]
    zone_directory = os.path.normpath(f'{install_directory}/zone')

    zone_dirs = file_io.get_directories_in_directory(zone_directory)

    for zone_dir in zone_dirs:
        if not zone_dir.endswith('all') or not zone_dir.endswith('english'):
            if os.path.isdir(zone_dir):
                shutil.rmtree(zone_dir)
    
    all_zone_folder = os.path.normpath(f'{zone_directory}/all')

    for file in file_io.get_all_files_in_tree(all_zone_folder):
        base_name = os.path.basename(file)
        
        mp_valid = "mp" in base_name if "gump" not in base_name else "mp" in base_name.replace("gump", "")

        if file.endswith('ipak') or not ("zm" in base_name or mp_valid):
            os.remove(file)

    english_zone_folder = os.path.normpath(f'{zone_directory}/english')

    all_english_zone_files = file_io.get_all_files_in_tree(english_zone_folder)

    for file in all_english_zone_files:
        if not os.path.basename(file) in valid_files:
            os.remove(file)

    players_dir = os.path.normpath(f'{install_directory}/players')
    sound_dir = os.path.normpath(f'{install_directory}/sound')
    video_dir = os.path.normpath(f'{install_directory}/video')

    dirs_to_delete = [
        players_dir,
        sound_dir,
        video_dir
    ]
    for dir in dirs_to_delete:
        if os.path.isdir(dir):
            shutil.rmtree(dir)


def trim_game(install_directory: str, game_enum_value: str, skip_verification: bool):
    if game_enum_value == data_structures.Games.CALL_OF_DUTY_WORLD_AT_WAR.value:
        trim_call_of_duty_world_at_war_install(install_directory, skip_verification)
    elif game_enum_value == data_structures.Games.CALL_OF_DUTY_BLACK_OPS_I.value:
        trim_call_of_duty_black_ops_i(install_directory, skip_verification)
    else:
        trim_call_of_duty_black_ops_ii(install_directory, skip_verification)


def trim_install(
    install_directory: str,
    game_enum_value: str,
    skip_verification: bool
):
    if not os.path.isdir(install_directory):
        error_message = f'The provided install directory does not exist: "{install_directory}"'
        logging.logger.log_message(error_message)
        raise NotADirectoryError(error_message)
    
    if game_enum_value and game_enum_value in data_structures.get_enum_strings_from_enum(data_structures.Games):
        trim_game(install_directory, game_enum_value, skip_verification)
    else:
        trim_game(install_directory, get_game_enum_value_automatically(install_directory), skip_verification)


def automatic_detection_run():
    trim_game(file_io.SCRIPT_DIR, get_game_enum_value_automatically(file_io.SCRIPT_DIR), False)

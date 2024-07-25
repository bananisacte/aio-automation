from functions.mor_levi_files_functions import create_updated_file, create_deleted_file, create_new_to_upload_file, create_update_file_to_upload, create_website_mor_levi_only_file, \
    create_new_items_for_picture_parse
from functions.prices_growth_qa import generate_qa_results


def mor_levi():
    create_updated_file("autosync-suppliers/files/Mor_Levi_Compare_FINAL.csv")
    create_website_mor_levi_only_file("autosync-suppliers/files/aio_website_full.csv")
    create_deleted_file("autosync-suppliers/files/Mor_Levi_Compare_FINAL.csv", "autosync-suppliers/files/aio_website_mor_levi_only.csv")
    create_new_to_upload_file("Files/mor_levi_final/mor_levi_updated_prices.csv", "autosync-suppliers/files/aio_website_mor_levi_only.csv")
    create_new_items_for_picture_parse("Files/mor_levi_final/mor_levi_new.csv")
    create_update_file_to_upload("Files/mor_levi_final/mor_levi_updated_prices.csv", "autosync-suppliers/files/aio_website_mor_levi_only.csv")


def suppliers():
    mor_levi()


suppliers()

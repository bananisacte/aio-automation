from functions.mor_levi_files_functions import create_updated_file, create_deleted_file, create_new_to_upload_file, create_update_file_to_upload

create_updated_file("autosync-suppliers/files/Mor_Levi_Compare_FINAL.csv")
create_deleted_file("autosync-suppliers/files/Mor_Levi_Compare_FINAL.csv", "autosync-suppliers/files/aio_site_mor_levi_only.csv")
create_new_to_upload_file("mor_levi_updated_prices.csv", "autosync-suppliers/files/aio_site_mor_levi_only.csv")
create_update_file_to_upload("mor_levi_updated_prices.csv", "autosync-suppliers/files/aio_site_mor_levi_only.csv")
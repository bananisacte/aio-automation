import pandas as pd
from functions.mor_levi import rename_headers_mor_levi, change_item_status_mor_levi, change_prices_mor_levi, \
    finalize_sale_price, delete_irrelevant_items, finalize_upload_sheet, export_faulty_rows_to_file

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

df = pd.read_csv("files/mor-levi-pricelist.csv")
mor_levi = df.copy()

mor_levi = rename_headers_mor_levi(mor_levi)
mor_levi = export_faulty_rows_to_file(mor_levi)
mor_levi = change_item_status_mor_levi(mor_levi)
mor_levi = delete_irrelevant_items(mor_levi)
mor_levi = change_prices_mor_levi(mor_levi)
mor_levi = finalize_sale_price(mor_levi)
mor_levi = finalize_upload_sheet(mor_levi)

mor_levi.to_csv("mor_levi_updated.csv", index=False)

df2 = pd.read_csv("files/aio_website_products.csv", low_memory=False)
aio = df2.copy()
filtered_aio = aio[aio['SupplierName'] == 'מור לוי']

ids_only_in_file1 = set(mor_levi['ItemId']) - set(filtered_aio['ItemId'])
new_df = mor_levi[mor_levi['ItemId'].isin(ids_only_in_file1)]
new_df.to_csv("mor-levi-new.csv", encoding='utf-8-sig', index=False)

ids_only_in_file2 = set(filtered_aio['ItemId']) - set(mor_levi['ItemId'])
new_df2 = filtered_aio[filtered_aio['ItemId'].isin(ids_only_in_file2)]
keep_cols = ['ItemId', 'ItemStatus']
new_df2 = new_df2[keep_cols]
new_df2.to_csv("mor-levi-false.csv", index=False)

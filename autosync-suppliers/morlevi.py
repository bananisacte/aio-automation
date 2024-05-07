import pandas as pd
from functions.mor_levi import rename_headers_mor_levi, change_item_status_mor_levi, change_prices_mor_levi, finalize_sale_price, delete_irrelevant_items, finalize_upload_sheet

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

df = pd.read_csv("files/mor-levi-pricelist.csv")
mor_levi = df.copy()

mor_levi = rename_headers_mor_levi(mor_levi)
mor_levi = change_item_status_mor_levi(mor_levi)
mor_levi = delete_irrelevant_items(mor_levi)
mor_levi = change_prices_mor_levi(mor_levi)
mor_levi = finalize_sale_price(mor_levi)
mor_levi = finalize_upload_sheet(mor_levi)

mor_levi.to_csv("mor_levi_upload.csv", encoding='utf-8-sig', index=False)

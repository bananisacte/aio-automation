import pandas as pd
from functions.ml_price_compare import change_inventory, change_prices_mor_levi, change_item_status, \
    finalize_sale_price,delete_irrelevant_categorys

df = pd.read_csv("files/Mor_Levi_Compare_FINAL.csv")
mor_levi = df.copy()

mor_levi = change_prices_mor_levi(mor_levi)
mor_levi = delete_irrelevant_categorys(mor_levi)
mor_levi = finalize_sale_price(mor_levi)
mor_levi = change_inventory(mor_levi)
mor_levi = change_item_status(mor_levi)
mor_levi.to_csv("mor_levi_updated.csv", encoding='utf-8-sig', index=False)

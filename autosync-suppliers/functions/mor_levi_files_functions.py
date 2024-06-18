import pandas as pd

from functions.mor_levi_compare_functions import change_prices_mor_levi, delete_irrelevant_categorys, finalize_sale_price, \
    change_inventory, change_item_status


def create_updated_file(filepath):
    df = pd.read_csv(filepath)
    mor_levi = df.copy()

    mor_levi = change_prices_mor_levi(mor_levi)
    mor_levi = delete_irrelevant_categorys(mor_levi)
    mor_levi = finalize_sale_price(mor_levi)
    mor_levi = change_inventory(mor_levi)
    mor_levi = change_item_status(mor_levi)
    mor_levi.to_csv("mor_levi_compare_updated.csv", encoding='utf-8-sig', index=False)


def create_deleted_file(filepath):
    pass

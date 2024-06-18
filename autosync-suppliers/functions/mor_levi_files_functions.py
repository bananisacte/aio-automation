import pandas as pd

from functions.mor_levi_compare_functions import change_prices_mor_levi, delete_irrelevant_categorys, finalize_sale_price, change_inventory, change_item_status


def create_updated_file(supplier_file_path):
    df = pd.read_csv(supplier_file_path)
    mor_levi = df.copy()

    mor_levi = change_prices_mor_levi(mor_levi)
    mor_levi = delete_irrelevant_categorys(mor_levi)
    mor_levi = finalize_sale_price(mor_levi)
    mor_levi = change_inventory(mor_levi)
    mor_levi = change_item_status(mor_levi)
    mor_levi.to_csv("mor_levi_updated_prices.csv", encoding='utf-8-sig', index=False)


def create_deleted_file(supplier_file_path):
    df = pd.read_csv(supplier_file_path)
    mor_levi = df.copy()
    return mor_levi


def compare_mor_levi_files(supplier_file_path, aio_website_file_path):
    df = pd.read_csv(supplier_file_path)
    df2 = pd.read_csv(aio_website_file_path)
    mor_levi = df.copy()
    all_in_one = df2.copy()
    return mor_levi, all_in_one


def create_mor_levi_only_file(aio_website_file_path):
    df = pd.read_csv(aio_website_file_path)
    all_in_one = df.copy()
    return all_in_one

import pandas as pd
from constants import Category, SubCategory, GrowthEnum


def clean_up_website_file(website_df):
    columns_to_keep = [
        "ItemId",
        "category",
        "SubCategory",
        "CostPrice",
        "ItemStatus",
        "RegularPrice",
        "SupplierName",
        "zap_url",
        "ZapLocation",
        "ZapMinimumPrice",
    ]
    filtered_df = website_df[columns_to_keep]
    filtered_df = filtered_df[filtered_df['SupplierName'] == 'מור לוי']
    return filtered_df



def extract_products_to_delete(supplier_df, website_df):
    unique_item_ids_website = website_df[~website_df['ItemId'].isin(supplier_df['ItemId'])]['ItemId'].unique()
    rows_to_keep = []
    for item_id in unique_item_ids_website:
        rows = website_df.loc[website_df['ItemId'] == item_id, ['ItemId', 'ItemStatus', 'category', 'SubCategory']].copy()
        rows['ItemStatus'] = False
        rows['category'] = "לא פעילים - למחיקה או טיפול"
        rows['SubCategory'] = "מור לוי למחיקה"
        rows_to_keep.append(rows)
    new_df = pd.concat(rows_to_keep, ignore_index=True)
    return new_df


# def extract_products_to_new(supplier_df, website_df):
#     unique_item_ids_supplier = supplier_df[~supplier_df['ItemId'].isin(website_df['ItemId'])]['ItemId'].unique()
#     rows_to_keep = []
#     for item_id in unique_item_ids_supplier:
#         rows = supplier_df.loc[supplier_df['ItemId'] == item_id, ['ItemId', 'CostPrice', 'RegularPrice', 'ItemStatus']].copy()
#         rows_to_keep.append(rows)
#     new_df = pd.concat(rows_to_keep, ignore_index=True)
#     return new_df


def extract_products_to_new(supplier_df, website_df):
    # Find unique ItemIds in supplier_df that are not in website_df
    unique_item_ids_supplier = supplier_df[~supplier_df['ItemId'].isin(website_df['ItemId'])]['ItemId'].unique()

    # Keep rows from supplier_df for the unique item ids
    new_df = supplier_df[supplier_df['ItemId'].isin(unique_item_ids_supplier)].copy()

    return new_df

def create_upload_to_update_file(supplier_df, website_df):
    new_rows = []
    for index, row in supplier_df.iterrows():
        item_id = row['ItemId']
        if item_id in website_df['ItemId'].values:
            website_row = website_df[website_df['ItemId'] == item_id].iloc[0]
            supplier_row = supplier_df[supplier_df['ItemId'] == item_id].iloc[0]
            new_row = {
                'erpid': item_id,
                'ItemId': item_id,
                'CostPrice': row['CostPrice'],
                'RegularPrice': supplier_row['RegularPrice'],
                'ZapMinimumPrice': supplier_row['RegularPrice'],
                'ZapLocation': 1,
                'Inventory': row['Inventory'],
                'ItemStatus': row['ItemStatus'],
                'PriceList': 'פרטי',
                'zap_url': website_row['zap_url']
            }
            new_rows.append(new_row)
    new_df = pd.DataFrame(new_rows)
    return new_df


def change_prices_mor_levi(df):
    df['CostPrice'] = df['CostPrice'].str.replace('₪', '')
    df['CostPrice'] = df['CostPrice'].str.replace(',', '')
    df['CostPrice'] = pd.to_numeric(df['CostPrice'], errors='coerce')
    df.insert(df.columns.get_loc('CostPrice') + 1, 'RegularPrice', None)
    return df


def change_inventory(df):
    df['Inventory'] = df['Inventory'].apply(lambda x: 100 if x == 'זמין במלאי' else -100)
    return df


def change_item_status(df):
    df['ItemStatus'] = df['ItemStatus'].apply(lambda x: True)
    return df


def delete_irrelevant_categorys(df):
    return df[df['Category'] != Category.MorLevi.CCTV]


def finalize_sale_price(df):
    df['RegularPrice'] = df.apply(calculate_sale_price, axis=1)
    return df


def calculate_sale_price(row):
    match row['Category']:
        case Category.MorLevi.MOBOS:
            if row['SubCategory'] in SubCategory.MorLevi.MOBOS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)

        case Category.MorLevi.GPUS:
            if row['SubCategory'] in SubCategory.MorLevi.GPUS:
                if row['CostPrice'] < 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
                elif 1000 < row['CostPrice'] < 3000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
                elif row['CostPrice'] > 3000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)

        case Category.MorLevi.PERIPHERALS:
            if row['SubCategory'] in SubCategory.MorLevi.PERIPHERALS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.CABLE_PERIPHERALS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 2.25), 0)

        case Category.MorLevi.CPU_AND_COOLING:
            if row['SubCategory'] in SubCategory.MorLevi.CPUS:
                if row['CostPrice'] < 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
                elif row['CostPrice'] > 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
            if row['SubCategory'] in SubCategory.MorLevi.AIR_COOLING:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            if row['SubCategory'] in SubCategory.MorLevi.LIQUID_COOLING:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
            if row['SubCategory'] in SubCategory.MorLevi.THERMO_PASTE:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.55), 0)

        case Category.MorLevi.MEMORY:
            if row['SubCategory'] in SubCategory.MorLevi.MEMORY:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.2), 0)

        case Category.MorLevi.STORAGE:
            if row['SubCategory'] in SubCategory.MorLevi.INTERNAL_STORAGE:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.EXTERNAL_STORAGE:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.MorLevi.FANS_CASES_MISC:
            if row['SubCategory'] in SubCategory.MorLevi.PC_CASES:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.PC_FANS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.PC_INTERNAL_CABLES:
                return round((row['CostPrice'] * 1.17 * 1.02 * 2.25), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.PC_PANELS_AND_DOORS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.75), 0)

        case Category.MorLevi.PSU:
            if row['SubCategory'] in SubCategory.MorLevi.PSUS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)

        case Category.MorLevi.LAPTOPS_TABLETS:
            if row['SubCategory'] in SubCategory.MorLevi.LAPTOPS_TABLETS:
                if row['CostPrice'] < 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
                elif row['CostPrice'] > 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.WARRANTY_EXT:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.CHARGERS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.DOCKING_STATIONS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.BAGS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 2.25), 0)

        case Category.MorLevi.DESKTOPS:
            if row['SubCategory'] in SubCategory.MorLevi.DESKTOPS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.WARRANTY_EXT:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)

        case Category.MorLevi.KBM:
            if row['SubCategory'] in SubCategory.MorLevi.KBM:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.MorLevi.MONITORS_TVS_AND_HANGERS:
            if row['SubCategory'] in SubCategory.MorLevi.MONITORS_TVS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.14), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.SCREEN_HANGERS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.75), 0)

        case Category.MorLevi.SOUND:
            if row['SubCategory'] in SubCategory.MorLevi.SOUND:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.MorLevi.NETWORK:
            if row['SubCategory'] in SubCategory.MorLevi.HOME_NETWORK:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.25), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.COMM_CLOSET:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.75), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.NETWORK_CABLES:
                return round((row['CostPrice'] * 1.17 * 1.02 * 3.25), 0)

        case Category.MorLevi.UPS:
            if row['SubCategory'] in SubCategory.MorLevi.UPS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)


def set_price_growths(row):
    pass
#     if row['SubCategory'] in SubCategory.MorLevi.MOBOS:
#         row['MinGrowth'] = GrowthEnum.FACTOR_1_15.value

        # case Category.MorLevi.GPUS:
        #     if row['SubCategory'] in SubCategory.MorLevi.GPUS:
        #         if row['CostPrice'] < 1000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
        #         elif 1000 < row['CostPrice'] < 3000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
        #         elif row['CostPrice'] > 3000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)
        #
        # case Category.MorLevi.PERIPHERALS:
        #     if row['SubCategory'] in SubCategory.MorLevi.PERIPHERALS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.CABLE_PERIPHERALS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 2.25), 0)
        #
        # case Category.MorLevi.CPU_AND_COOLING:
        #     if row['SubCategory'] in SubCategory.MorLevi.CPUS:
        #         if row['CostPrice'] < 1000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
        #         elif row['CostPrice'] > 1000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
        #     if row['SubCategory'] in SubCategory.MorLevi.AIR_COOLING:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #     if row['SubCategory'] in SubCategory.MorLevi.LIQUID_COOLING:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
        #     if row['SubCategory'] in SubCategory.MorLevi.THERMO_PASTE:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.55), 0)
        #
        # case Category.MorLevi.MEMORY:
        #     if row['SubCategory'] in SubCategory.MorLevi.MEMORY:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.2), 0)
        #
        # case Category.MorLevi.STORAGE:
        #     if row['SubCategory'] in SubCategory.MorLevi.INTERNAL_STORAGE:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.EXTERNAL_STORAGE:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #
        # case Category.MorLevi.FANS_CASES_MISC:
        #     if row['SubCategory'] in SubCategory.MorLevi.PC_CASES:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.PC_FANS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.PC_INTERNAL_CABLES:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 2.25), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.PC_PANELS_AND_DOORS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.75), 0)
        #
        # case Category.MorLevi.PSU:
        #     if row['SubCategory'] in SubCategory.MorLevi.PSUS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
        #
        # case Category.MorLevi.LAPTOPS_TABLETS:
        #     if row['SubCategory'] in SubCategory.MorLevi.LAPTOPS_TABLETS:
        #         if row['CostPrice'] < 1000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
        #         elif row['CostPrice'] > 1000:
        #             return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.WARRANTY_EXT:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.CHARGERS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.DOCKING_STATIONS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.BAGS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 2.25), 0)
        #
        # case Category.MorLevi.DESKTOPS:
        #     if row['SubCategory'] in SubCategory.MorLevi.DESKTOPS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.WARRANTY_EXT:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
        #
        # case Category.MorLevi.KBM:
        #     if row['SubCategory'] in SubCategory.MorLevi.KBM:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #
        # case Category.MorLevi.MONITORS_TVS_AND_HANGERS:
        #     if row['SubCategory'] in SubCategory.MorLevi.MONITORS_TVS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.14), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.SCREEN_HANGERS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.75), 0)
        #
        # case Category.MorLevi.SOUND:
        #     if row['SubCategory'] in SubCategory.MorLevi.SOUND:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
        #
        # case Category.MorLevi.NETWORK:
        #     if row['SubCategory'] in SubCategory.MorLevi.HOME_NETWORK:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.25), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.COMM_CLOSET:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.75), 0)
        #     elif row['SubCategory'] in SubCategory.MorLevi.NETWORK_CABLES:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 3.25), 0)
        #
        # case Category.MorLevi.UPS:
        #     if row['SubCategory'] in SubCategory.MorLevi.UPS:
        #         return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

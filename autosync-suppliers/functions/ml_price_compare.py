import pandas as pd

from constants import Category, SubCategory


def change_prices_mor_levi(df):
    df['CostPrice'] = df['CostPrice'].str.replace('₪', '')
    df['CostPrice'] = df['CostPrice'].str.replace(',', '')
    df['CostPrice'] = pd.to_numeric(df['CostPrice'], errors='coerce')
    df.insert(df.columns.get_loc('CostPrice') + 1, 'SalePrice', None)
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
    df['SalePrice'] = df.apply(calculate_sale_price, axis=1)
    return df


def calculate_sale_price(row):
    match row['Category']:
        case Category.MorLevi.MOBOS:
            if row['SubCategory'] in SubCategory.MorLevi.MOBOS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)

        case Category.MorLevi.GPUS:
            if row['SubCategory'] in SubCategory.MorLevi.GPUS:
                if row['CostPrice'] < 5000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
                elif row['CostPrice'] > 5000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)

        case Category.MorLevi.PERIPHERALS:
            if row['SubCategory'] in SubCategory.MorLevi.PERIPHERALS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.CABLE_PERIPHERALS:
                return round((row['CostPrice'] * 2.5), 0)

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
                return round((row['CostPrice'] * 2), 0)

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
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.PC_FANS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.PC_INTERNAL_CABLES:
                return round((row['CostPrice'] * 2.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.PC_PANELS_AND_DOORS:
                return round((row['CostPrice'] * 2), 0)

        case Category.MorLevi.PSU:
            if row['SubCategory'] in SubCategory.MorLevi.PSUS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)

        case Category.MorLevi.LAPTOPS_TABLETS:
            if row['SubCategory'] in SubCategory.MorLevi.LAPTOPS_TABLETS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.WARRANTY_EXT:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.CHARGERS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.DOCKING_STATIONS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.BAGS:
                return round((row['CostPrice'] * 2.5), 0)

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
                return round((row['CostPrice'] * 2), 0)

        case Category.MorLevi.SOUND:
            if row['SubCategory'] in SubCategory.MorLevi.SOUND:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.MorLevi.NETWORK:
            if row['SubCategory'] in SubCategory.MorLevi.HOME_NETWORK:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.25), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.COMM_CLOSET:
                return round((row['CostPrice'] * 2), 0)
            elif row['SubCategory'] in SubCategory.MorLevi.NETWORK_CABLES:
                return round((row['CostPrice'] * 3.5), 0)

        case Category.MorLevi.UPS:
            if row['SubCategory'] in SubCategory.MorLevi.UPS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
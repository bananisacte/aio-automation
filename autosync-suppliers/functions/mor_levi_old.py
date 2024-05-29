import pandas as pd

DELETE_ITEMS_PREFIXES = ('ציוד נלווה לMINING', 'מטענים')

MOTHERBOARD_PREFIXES = ('לוח אם', 'לוח לדור', 'לוח', 'לוח למעבדי')
GRAPHICS_CARD_PREFIXES = ('כרטיס מסך', 'כ. מסך', 'כ.מסך')
CPU_PREFIXES = ('מעבד', 'מעבד דור', 'מעבד גיימינג')
AIR_COOLING_PREFIXES = ('מתאם', 'מאוורר', 'קירור אוויר', 'מאורר למעבד', 'מאוורר למעבד', 'Antec A30')
LIQUID_COOLING_PREFIXES = ('קירור למעבד', 'קירור נוזלי', 'קירור', 'קרור', 'נוזלי')
THERMO_PASTE_PREFIXES = ('משחה טרמית', 'משחה תרמית')
MEMORY_PREFIXES = (
'זכרון לנייח', 'זכרון לנייד', 'זיכרון לנייח', 'זיכרון לנייד', 'ז. לנייח', 'ז. לנייד', 'ז.לנייח', 'ז.לנייד', 'זכרון',
'זיכרון')
INTERNAL_DRIVES_PREFIXES = ('דיסק פנימי', 'דיסק קשיח', 'דיסק', 'דיסק לנייח')
EXTERNAL_DRIVES_PREFIXES = (
'דיסק חיצוני', 'דיסק קשיח חיצוני', 'דיסק קשיח מכאני חיצוני', 'זכרון נייד', 'ז.נייד', 'ז. נייד', 'כרטיס זכרון',
'כ. זכרון')
EXTERNAL_MISC_PREFIXES = (
    'צורב פנימי', 'צורב חיצוני', 'מארז  חיצוני ', 'קופסא לדיסק חיצוני', 'תחנת עגינה', 'קופסא חיצונית לדיסק', 'Maivo',
    'מתאם', 'מארז ל4 דיסקים', 'קופסא לדיסק', 'קורא כרטיסים',
    'מארז חיצוני  ל-2 דיסקים', 'מארז חיצוני לדיסק', 'קופסא חיצונית', 'ת. עגינה'
)
PC_CASE_PREFIXES = (
    'מארז ללא ספק', 'מארז Antec', 'מארז ANTEC', 'מארז Cooler Master', 'מארז COOLER MASTER', 'מארז Corsair',
    'מארז CORSAIR', 'מארז וספק', 'מארז שחור', 'מארז לבן', 'מארז שקט', 'מארז גיימינג'
)
PC_CASE_PARTS_PREFIXES = (
'דלת צד למארז', 'זכוכית צד למארז ', 'זכוכית קידמית למארז', 'דלת ימין ', 'פנל קדמי', 'זכוכית קדמית', 'זכוכית למארז',
'דלת צד זכוכית למארזים')
PC_FANS_PREFIXES = (
'מאורר למארז', 'מאוורר אנטק', 'מאוררים למארז', 'מאוררים ובקר למארז', 'מאוורר קורסייר', 'מאוורר למארז')
BASIC_PERIPHERALS_PREFIXES = (
    'PCIe 5.0 12VHPWR GPU', 'כבל Molex', 'כבל SATA', 'מתאם MOLEX', 'מפצל חשמל Sata', 'מפצל לשתי Molex', 'מפצל Molex',
    'ברגים למאוררים', 'רמקול ללוח אם', 'מפצל מאוררים מחיבור'
)
ADV_PERIPHERALS_PREFIXES = (
    'סט כבלים מאריכים', 'כבלים מאריכים', 'מתאם לספק', 'כבל ותושבת לכ. מסך', 'כבל ומתאם לכ.מסך', 'כבל לכרטיס מסך',
    'תומך לכרטיס מסך', 'תומך לכרטיסי מסך', 'תופסן אנכי', 'בקר Cooler'
)
PSU_PREFIXES = ('ספק כח', 'ספק כוח', 'ספק', 'Corsair HX1500i')
LAPTOPS_PREFIXES = (
'נייד', 'Gigabyte AERO 16', 'נינייד', 'מחשב נייד', 'נ. ASUS', 'ASUS VivoBook', 'ASUS TUF Gaming', 'VIVOBOOK PRO',
'Asus VivoBook')
LAPTOP_WARRANTY_PREFIXES = ('הרחבת אחריות', 'ASUS Laptop series warranty', 'ASUS Vivibook / Vivobook S warranty',
                            'ASUS Zenbook / Vivobook Pro series warranty')
BACKPACK_PREFIXES = ('תיק מהודר לנייד', 'תיק למחשב נייד', 'תיק צד שחור לנייד', 'תיק צד', 'תיק גב', 'תיק נשיאה לנייד',
                     'Dell Essential Briefcase')
SCREENS_PREFIXES = (
'SOLID', 'מסך', 'מסך גיימינג', 'Solid', 'מסך שטוח', 'מסך מחשב קעור', 'מסך קעור', 'מסך מחשב', 'מסך חכם', 'טלווזייה',
'טלוויזיה')
SCREEN_STANDS_PREFIXES = (
'מתקן תליה', 'מתקן צמוד קיר', 'זרוע דו מפרקית', 'זרוע שולחנית', 'מתאם למחשב נייד', 'מתקן תלייה')
PC_PERIPHERALS_PREFIXES = (
    'מקלדות סטנדרטיות', 'מקלדות גיימינג', 'עכברי גיימינג', 'עכבר חוטי', 'עכבר אלחוטי', 'סט חוטי', 'סט אל-חוטי',
    'משטח לעכבר/משענת יד למקלדת', 'LOGITECH', 'CREATIVE', 'GENIUS', 'מיקרופונים', 'אוזניות'
)
USB_CABLES_ADATPTERS_PREFIXES = ('מפצלי USB', 'USB כבלים ומתאמים')
DISPLAY_CABLES_PREFIXES = ('HDMI', 'VGA', 'Display Port', 'DVI')
PERIPHERALS_PREFIXES = (
'מוצרי אבטחה', 'מוצרי עזר לדיסק קשיח', 'מצלמות אינטרנט', 'כרטיסי PCI וPCIE', 'משטח קירור למחשב נייד', 'מצלמות דרך',
"ג'ויסטיקים")
POWER_EXTENSTION_CORDS_PREFIXES = ('כבל מאריך חשמל', 'מפצל שני שקעים', 'מפצל חשמל')
OTHER_PREFIXES = ('ספרי מנקה', 'ספריי לחץ אוויר', 'קופסאת מיתוג')

HOME_NETWORK_PREFIXES = (
'מודם סלולרי', 'נתבים', '2.5 Gbps', '10/100', '10/100/1000', 'POE', 'מנוהל', "סוויצ'ים", 'אקסס פוינט', 'כרטיסי רשת')
NETWORK_CABLES_PREFIXES = ('CAT 5', 'CAT 5E', 'CAT 6', 'CAT 6A/7')
OFFICE_NETWORK_PREFIXES = ('ארונות תקשורת', 'ארונות תקשורת', 'כלי עבודה לציוד רשת')

UPS_PREFIXES = ('אל פסק', 'אל-פסק', 'סוללה לאל פסק')


def rename_headers_mor_levi(df):
    for item in df.columns:
        match item:
            case 'מק"ט מור לוי':
                df.rename(columns={item: 'mor_levi_id'}, inplace=True)
            case 'מק"ט יצרן':
                df.rename(columns={item: 'manufacturer_id'}, inplace=True)
            case 'תיאור פריט':
                df.rename(columns={item: 'description'}, inplace=True)
            case 'מחיר':
                df.rename(columns={item: 'price'}, inplace=True)
            case 'קטגוריה':
                df.rename(columns={item: 'category'}, inplace=True)
            case 'זמינות':
                df.rename(columns={item: 'item_status'}, inplace=True)
            case 'יצרן':
                df.rename(columns={item: 'manufacturer'}, inplace=True)
            case 'תמונת המוצר':
                df.rename(columns={item: 'image'}, inplace=True)
    return df


def export_faulty_rows_to_file(df):
    condition = df[['mor_levi_id', 'price', 'item_status']].isnull().any(axis=1)
    faulty_df = df[condition]
    clean_df = df[~condition]
    faulty_df.to_csv("mor_levi_faulty.csv",encoding='utf-8-sig', index=False)
    return clean_df


def change_item_status_mor_levi(df):
    status_str = 'זמין במלאי'
    df["item_status"] = df["item_status"].str.strip().apply(lambda x: x == status_str)
    return df


def change_prices_mor_levi(df):
    df['price'] = df['price'].str.replace('₪', '')
    df['price'] = df['price'].str.replace(',', '')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df.insert(df.columns.get_loc('price') + 1, 'sale_price', None)

    return df


def calculate_sale_price(row):
    if row['description'].startswith(MOTHERBOARD_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.15), 0)

    if row['description'].startswith(GRAPHICS_CARD_PREFIXES):
        if row['price'] < 5000:
            return round((row['price'] * 1.17 * 1.02 * 1.1), 0)
        elif row['price'] > 5000:
            return round((row['price'] * 1.17 * 1.02 * 1.05), 0)

    if row['description'].startswith(AIR_COOLING_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['description'].startswith(LIQUID_COOLING_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.15), 0)

    if row['description'].startswith(CPU_PREFIXES):
        if row['price'] < 1000:
            return round((row['price'] * 1.17 * 1.02 * 1.15), 0)
        elif row['price'] > 1000:
            return round((row['price'] * 1.17 * 1.02 * 1.1), 0)

    if row['description'].startswith(THERMO_PASTE_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.15), 0)

    if row['description'].startswith(MEMORY_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.1), 0)

    if row['description'].startswith(INTERNAL_DRIVES_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.15), 0)

    if row['description'].startswith(EXTERNAL_DRIVES_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['description'].startswith(EXTERNAL_MISC_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['description'].startswith(PC_CASE_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.2), 0)

    if row['description'].startswith(PC_CASE_PARTS_PREFIXES):
        return round((row['price'] * 2), 0)

    if row['description'].startswith(PC_FANS_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.5), 0)

    if row['description'].startswith(BASIC_PERIPHERALS_PREFIXES):
        return round((row['price'] * 2.5), 0)

    if row['description'].startswith(ADV_PERIPHERALS_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['description'].startswith(PSU_PREFIXES):
        if row['mor_levi_id'] == 'CCPS-SAMA512' or row['mor_levi_id'] == 'CCPS512':
            row['price'] = 149
        else:
            row['price'] = round(row['price'] * 1.17 * 1.02 * 1.15, 0)
        return row['price']

    if row['description'].startswith(LAPTOPS_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.05), 0)

    if row['description'].startswith(LAPTOP_WARRANTY_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.20), 0)

    if row['description'].startswith(BACKPACK_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.30), 0)

    if row['description'].startswith(SCREENS_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.14), 0)

    if row['description'].startswith(SCREEN_STANDS_PREFIXES):
        return round((row['price'] * 2.1), 0)

    if row['category'] in PC_PERIPHERALS_PREFIXES:
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['category'] in USB_CABLES_ADATPTERS_PREFIXES:
        return round((row['price'] * 2.5), 0)

    if row['category'] in DISPLAY_CABLES_PREFIXES:
        if row['category'] == 'Display Port' or row['category'] == 'HDMI':
            return round((row['price'] * 3.5), 0)
        else:
            return round((row['price'] * 2.5), 0)

    if row['category'] in PERIPHERALS_PREFIXES or row['description'].startswith('ממיר IDE Converter'):
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['description'].startswith('כבל מתח'):
        return round((row['price'] * 2), 0)

    if row['description'].startswith(POWER_EXTENSTION_CORDS_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.75), 0)

    if row['description'].startswith(OTHER_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.3), 0)

    if row['category'] in HOME_NETWORK_PREFIXES:
        return round((row['price'] * 1.17 * 1.02 * 1.25), 0)

    if row['category'] in NETWORK_CABLES_PREFIXES:
        return round((row['price'] * 3.5), 0)

    if row['category'] in OFFICE_NETWORK_PREFIXES:
        return round((row['price'] * 1.17 * 1.02 * 2), 0)

    if row['description'].startswith(UPS_PREFIXES):
        return round((row['price'] * 1.17 * 1.02 * 1.30), 0)


def delete_irrelevant_items(df):
    df.drop('image', axis=1, inplace=True)
    df.drop(df.index[df['mor_levi_id'] == 'ST-HD50025Z'][0], inplace=True)
    for prefix in DELETE_ITEMS_PREFIXES:
        mask = df['category'].str.startswith(prefix)
        df.drop(df.index[mask.fillna(False)], inplace=True)
    return df


def finalize_sale_price(df):
    df['sale_price'] = df.apply(calculate_sale_price, axis=1)
    return df


def finalize_upload_sheet(df):
    df = df.rename(columns={'mor_levi_id': 'ItemId',
                            'price': 'CostPrice',
                            'sale_price': 'RegularPrice',
                            'item_status': 'ItemStatus'})
    df = df.drop(columns=['manufacturer_id', 'description', 'category', 'manufacturer'])
    return df

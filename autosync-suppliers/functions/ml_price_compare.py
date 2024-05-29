import pandas as pd


class Category:
    MOBOS = 'לוחות אם'
    GPUS = 'כרטיסי מסך'
    PERIPHERALS = 'ציוד הקפי'
    CPU_AND_COOLING = 'מעבדים ופתרונות קירור'
    MEMORY = 'זכרון'
    STORAGE = 'אחסון'
    FANS_CASES_MISC = 'מארזים / מאוררים למארז/ ציוד עזר לבנית מחשב'
    PSU = 'ספקי כוח'
    LAPTOPS_TABLETS = 'מחשבים ניידים/ טאבלטים'
    DESKTOPS = 'מחשבים נייחים'
    KBM = 'מקלדות ועכברים'
    MONITORS_TVS_AND_HANGERS = 'מסכי מחשב / טלוויזיות/מתקני תלייה'
    SOUND = 'SOUND - ציוד קול'
    NETWORK = 'ציוד רשת'
    UPS = 'אל פסק UPS'
    CCTV = 'טלוויזיה במעגל סגור'


class SubCategory:
    MOBOS = ('לוחות למעבדי AMD', 'לוחות למעבדי Intel', 'מעבד מובנה על הלוח')
    GPUS = ('AMD Radeon', 'NVIDIA')
    PERIPHERALS = (
        'כרטיסי PCI וPCIE', 'משטח קירור למחשב נייד', 'מוצרי אבטחה', 'מפצלי USB', 'מצלמות אינטרנט', 'ציוד נלווה לMINING',
    )
    CABLE_PERIPHERALS = ('כבלים ומתאמים')
    CPUS = ('מעבדים INTEL', 'מעבדים AMD')
    LIQUID_COOLING = ('קירור נוזלי')
    AIR_COOLING = ('פתרונות קירור אוויר')
    THERMO_PASTE = ('משחה טרמית')
    MEMORY = ('זכרון לנייח DIMM', 'זכרון לנייד SODIMM')
    INTERNAL_STORAGE = ('SSD sata 3', 'NVME GEN3', 'NVME GEN4', 'HDD פנימי','NVME GEN5')
    EXTERNAL_STORAGE = ('קופסא חיצונית לHDD', 'SSD חיצוני', 'HDD חיצוני', 'Disk On Key', 'MICRO SD', 'כונן אופטי')
    PC_CASES = ('Antec', 'Corsair', 'Cooler Master', 'Solid & Others')
    PC_FANS = ('מאוררים למארז')
    PC_INTERNAL_CABLES = ('כבלים ומתאמים לבניית מחשב')
    PC_PANELS_AND_DOORS = ('פנלים קדמיים ודלתות צד')
    PSUS = ('ספקי כוח')
    LAPTOPS_TABLETS = ('מחשבים ניידים')
    WARRANTY_EXT = ('הרחבות אחריות ניידים', 'הרחבת אחריות למחשבי מותג')
    CHARGERS = ('מטענים')
    DOCKING_STATIONS = ('תחנות עגינה')
    BAGS = ('תיקים')
    DESKTOPS = ('Mini PC', 'AIO', 'מחשב מותג')
    KBM = ('מקלדות סטנדרטיות', 'מקלדות גיימינג', 'עכברים', 'סט מקלדת + עכבר', 'משטח לעכבר/משענת יד למקלדת')
    MONITORS_TVS = ('מסכי מחשב', 'טלוויזיות')
    SCREEN_HANGERS = ('מתקני תלייה')
    SOUND = ('רמקולים', 'מיקרופונים', 'אוזניות')
    UPS = ('אל פסק UPS')
    HOME_NETWORK = ("סוויצ'ים", "כרטיסי רשת", "מודם סלולרי", "אקסס פוינט", "נתבים")
    COMM_CLOSET = ('ארונות תקשורת', 'כלי עבודה לציוד רשת')
    NETWORK_CABLES = ('כבלי רשת', 'ראשים וקופסאות')


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
    return df[df['Category'] != Category.CCTV]


def finalize_sale_price(df):
    df['SalePrice'] = df.apply(calculate_sale_price, axis=1)
    return df


def calculate_sale_price(row):
    match row['Category']:
        case Category.MOBOS:
            if row['SubCategory'] in SubCategory.MOBOS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)

        case Category.GPUS:
            if row['SubCategory'] in SubCategory.GPUS:
                if row['CostPrice'] < 5000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
                elif row['CostPrice'] > 5000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)

        case Category.PERIPHERALS:
            if row['SubCategory'] in SubCategory.PERIPHERALS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.CABLE_PERIPHERALS:
                return round((row['CostPrice'] * 2.5), 0)

        case Category.CPU_AND_COOLING:
            if row['SubCategory'] in SubCategory.CPUS:
                if row['CostPrice'] < 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
                elif row['CostPrice'] > 1000:
                    return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
            if row['SubCategory'] in SubCategory.AIR_COOLING:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            if row['SubCategory'] in SubCategory.LIQUID_COOLING:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
            if row['SubCategory'] in SubCategory.THERMO_PASTE:
                return round((row['CostPrice'] * 2), 0)

        case Category.MEMORY:
            if row['SubCategory'] in SubCategory.MEMORY:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.2), 0)

        case Category.STORAGE:
            if row['SubCategory'] in SubCategory.INTERNAL_STORAGE:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)
            elif row['SubCategory'] in SubCategory.EXTERNAL_STORAGE:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.FANS_CASES_MISC:
            if row['SubCategory'] in SubCategory.PC_CASES:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.PC_FANS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.PC_INTERNAL_CABLES:
                return round((row['CostPrice'] * 2.5), 0)
            elif row['SubCategory'] in SubCategory.PC_PANELS_AND_DOORS:
                return round((row['CostPrice'] * 2), 0)

        case Category.PSU:
            if row['SubCategory'] in SubCategory.PSUS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.15), 0)

        case Category.LAPTOPS_TABLETS:
            if row['SubCategory'] in SubCategory.LAPTOPS_TABLETS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.05), 0)
            elif row['SubCategory'] in SubCategory.WARRANTY_EXT:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.CHARGERS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)
            elif row['SubCategory'] in SubCategory.DOCKING_STATIONS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)
            elif row['SubCategory'] in SubCategory.BAGS:
                return round((row['CostPrice'] * 2.5), 0)

        case Category.DESKTOPS:
            if row['SubCategory'] in SubCategory.DESKTOPS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.1), 0)
            elif row['SubCategory'] in SubCategory.WARRANTY_EXT:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.5), 0)

        case Category.KBM:
            if row['SubCategory'] in SubCategory.KBM:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.MONITORS_TVS_AND_HANGERS:
            if row['SubCategory'] in SubCategory.MONITORS_TVS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.14), 0)
            elif row['SubCategory'] in SubCategory.SCREEN_HANGERS:
                return round((row['CostPrice'] * 2), 0)

        case Category.SOUND:
            if row['SubCategory'] in SubCategory.SOUND:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

        case Category.NETWORK:
            if row['SubCategory'] in SubCategory.HOME_NETWORK:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.25), 0)
            elif row['SubCategory'] in SubCategory.COMM_CLOSET:
                return round((row['CostPrice'] * 2), 0)
            elif row['SubCategory'] in SubCategory.NETWORK_CABLES:
                return round((row['CostPrice'] * 3.5), 0)

        case Category.UPS:
            if row['SubCategory'] in SubCategory.UPS:
                return round((row['CostPrice'] * 1.17 * 1.02 * 1.3), 0)

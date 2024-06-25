from enum import Enum


class Category:
    class MorLevi:
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
    class MorLevi:
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
        INTERNAL_STORAGE = ('SSD sata 3', 'NVME GEN3', 'NVME GEN4', 'HDD פנימי', 'NVME GEN5')
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


class GrowthEnum(Enum):
    FACTOR_1_05 = 25.31
    FACTOR_1_1 = 31.27
    FACTOR_1_15 = 37.24
    FACTOR_1_2 = 43.21
    FACTOR_1_25 = 49.18
    FACTOR_1_3 = 55.14
    FACTOR_1_35 = 61.11
    FACTOR_1_5 = 79.01
    FACTOR_1_55 = 84.98
    FACTOR_1_75 = 108.85
    FACTOR_2_25 = 168.52
    FACTOR_2_75 = 228.19
    FACTOR_3_25 = 287.86

# class CategoryFactor:
#     class MorLevi:
#         MOBOS =
#         GPUS =
#         PERIPHERALS =
#         CABLE_PERIPHERALS =
#         CPUS =
#         LIQUID_COOLING =
#         AIR_COOLING =
#         THERMO_PASTE =
#         MEMORY =
#         INTERNAL_STORAGE =
#         EXTERNAL_STORAGE =
#         PC_CASES =
#         PC_FANS =
#         PC_INTERNAL_CABLES =
#         PC_PANELS_AND_DOORS =
#         PSUS =
#         LAPTOPS_TABLETS =
#         WARRANTY_EXT =
#         CHARGERS =
#         DOCKING_STATIONS =
#         BAGS =
#         DESKTOPS =
#         KBM =
#         MONITORS_TVS =
#         SCREEN_HANGERS =
#         SOUND =
#         UPS =
#         HOME_NETWORK =
#         COMM_CLOSET =
#         NETWORK_CABLES =
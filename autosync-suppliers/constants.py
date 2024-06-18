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

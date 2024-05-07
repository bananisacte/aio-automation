# Automation of Products Synchronization

## Mor-Levi Supplier:
### Step 1:
- Download the relevant price list from the Mor-Levi website (all categories).

### Step 2:
- Go through the file and arrange cells with empty values in the price and availability columns!

### Step 3:
- Save the price list with the name in CSV UTF-8 file format.

### Step 4:
- Move the saved file into the folder named "files" located in autosync-suppliers, with the name 'mor-levi-pricelist.csv'.

### Step 5:
- After running the script, take the file from Step 4, rename it to 'mor-levi-pricelist-YYYYMMDD.csv' (YYYYMMDD - current date), and move it to the OLD directory.
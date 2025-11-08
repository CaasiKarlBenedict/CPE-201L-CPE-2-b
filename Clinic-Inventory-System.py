# clinic_inventory_list.py - Using Basic List Data Structures
from datetime import datetime
import customtkinter as ctk
from tkinter import ttk, messagebox
import collections

# ---------------- APP CONFIG ----------------
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Using Multidimensional Array Data Structures for storing inventory data
# Each row represents a record, each column represents a field
# medicines[row][column] where columns are: [id, name, packs, items_per_pack, total_qty, expiry]
medicines = []  # 2D array: medicines[row][0]=id, medicines[row][1]=name, etc.

# equipment[row][column] where columns are: [id, name, stock, status]  
equipment = []  # 2D array: equipment[row][0]=id, equipment[row][1]=name, etc.

# Column indices for medicines array
MED_ID = 0
MED_NAME = 1
MED_PACKS = 2
MED_ITEMS_PER_PACK = 3
MED_TOTAL_QTY = 4
MED_EXPIRY = 5

# Column indices for equipment array
EQ_ID = 0
EQ_NAME = 1
EQ_STOCK = 2
EQ_STATUS = 3

# Add default data to demonstrate list operations
def initialize_default_data():
    """Initialize the multidimensional arrays with default medicine and equipment data"""
    global medicines, equipment
    
    # Clear existing data
    medicines.clear()
    equipment.clear()
    
    # Arrays start empty - no default data

# Basic Array Operations for Medicines
def add_medicine(name, packs, items_per_pack, total_qty, expiry):
    """Add medicine to multidimensional array using append()"""
    global medicines
    
    row_id = len(medicines) + 1  # simple auto-increment using array length
    # Create a new row with all fields
    new_row = [row_id, name, packs, items_per_pack, total_qty, expiry]
    medicines.append(new_row)  # Add entire row to 2D array
    
    # Return a dictionary for compatibility with existing code
    return {
        "id": row_id,
        "name": name,
        "packs": packs,
        "items_per_pack": items_per_pack,
        "total_qty": total_qty,
        "expiry": expiry
    }

def insert_medicine_at_position(index, name, packs, items_per_pack, total_qty, expiry):
    """Insert medicine into multidimensional array at a specific index using insert()"""
    global medicines
    
    if not (0 <= index <= len(medicines)):
        print(f"Error: Index {index} is out of bounds for medicines array (size {len(medicines)})")
        return None
    
    # Generate a unique ID for the new medicine
    new_id = (medicines[-1][MED_ID] + 1) if medicines else 1
    
    # Create new row with all fields
    new_row = [new_id, name, packs, items_per_pack, total_qty, expiry]
    medicines.insert(index, new_row)  # Insert entire row at specific index
    
    # Re-assign IDs to maintain sequential order after insertion
    for i in range(len(medicines)):
        medicines[i][MED_ID] = i + 1
        
    return {
        "id": new_id,
        "name": name,
        "packs": packs,
        "items_per_pack": items_per_pack,
        "total_qty": total_qty,
        "expiry": expiry
    }

def remove_medicine_by_id(medicine_id):
    """Remove medicine by ID using multidimensional array operations"""
    global medicines
    
    for i in range(len(medicines)):
        if medicines[i][MED_ID] == medicine_id:
            # Store the removed data before deletion
            removed_data = {
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            }
            # Remove entire row from 2D array
            medicines.pop(i)
            return removed_data
    return None

def remove_medicine_by_name(name):
    """Remove medicine by name using multidimensional array operations"""
    global medicines
    
    for i in range(len(medicines)):
        if medicines[i][MED_NAME].lower() == name.lower():
            # Store the removed data before deletion
            removed_data = {
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            }
            # Remove entire row from 2D array
            medicines.pop(i)
            return removed_data
    return None

def get_medicine_by_index(index):
    """Get medicine by multidimensional array index"""
    if 0 <= index < len(medicines):
        return {
            "id": medicines[index][MED_ID],
            "name": medicines[index][MED_NAME],
            "packs": medicines[index][MED_PACKS],
            "items_per_pack": medicines[index][MED_ITEMS_PER_PACK],
            "total_qty": medicines[index][MED_TOTAL_QTY],
            "expiry": medicines[index][MED_EXPIRY]
        }
    return None

def insert_medicine(name, packs, items_per_pack, total_qty, expiry):
    """Add medicine using basic multidimensional array append operation"""
    return add_medicine(name, packs, items_per_pack, total_qty, expiry)

def fetch_medicines():
    """Fetch all medicines from multidimensional array"""
    return [(medicines[i][MED_ID], medicines[i][MED_NAME], medicines[i][MED_PACKS], 
             medicines[i][MED_ITEMS_PER_PACK], medicines[i][MED_TOTAL_QTY], medicines[i][MED_EXPIRY]) 
            for i in range(len(medicines))]

def get_medicine_count():
    """Get total number of medicines in multidimensional array"""
    return len(medicines)

def is_medicines_empty():
    """Check if medicines multidimensional array is empty"""
    return len(medicines) == 0

def clear_all_medicines():
    """Clear all medicines from multidimensional array"""
    global medicines
    medicines.clear()

def update_medicine(row_id, name, packs, items_per_pack, total_qty, expiry):
    """Update medicine using multidimensional array operations"""
    global medicines
    
    for i in range(len(medicines)):
        if medicines[i][MED_ID] == row_id:
            medicines[i][MED_NAME] = name
            medicines[i][MED_PACKS] = packs
            medicines[i][MED_ITEMS_PER_PACK] = items_per_pack
            medicines[i][MED_TOTAL_QTY] = total_qty
            medicines[i][MED_EXPIRY] = expiry
            return True
    return False

def find_medicine_by_id(row_id):
    """Find medicine by ID using multidimensional array operations"""
    for i in range(len(medicines)):
        if medicines[i][MED_ID] == row_id:
            return {
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            }
    return None

def find_medicine_by_name(name):
    """Find medicine by name using multidimensional array operations"""
    for i in range(len(medicines)):
        if medicines[i][MED_NAME].lower() == name.lower():
            return {
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            }
    return None

def delete_medicine(row_id):
    """Delete medicine using multidimensional array operations"""
    return remove_medicine_by_id(row_id)

# -------------------------
# Equipment functions with Basic Multidimensional Array Operations
# -------------------------
def add_equipment(name, stock, status):
    """Add equipment to multidimensional array using append()"""
    global equipment
    
    row_id = len(equipment) + 1
    # Create a new row with all fields
    new_row = [row_id, name, stock, status]
    equipment.append(new_row)  # Add entire row to 2D array
    
    # Return a dictionary for compatibility with existing code
    return {
        "id": row_id,
        "name": name,
        "stock": stock,
        "status": status
    }

def insert_equipment_at_position(index, name, stock, status):
    """Insert equipment into multidimensional array at a specific index using insert()"""
    global equipment
    
    if not (0 <= index <= len(equipment)):
        print(f"Error: Index {index} is out of bounds for equipment array (size {len(equipment)})")
        return None
    
    # Generate a unique ID for the new equipment
    new_id = (equipment[-1][EQ_ID] + 1) if equipment else 1
    
    # Create new row with all fields
    new_row = [new_id, name, stock, status]
    equipment.insert(index, new_row)  # Insert entire row at specific index
    
    # Re-assign IDs to maintain sequential order after insertion
    for i in range(len(equipment)):
        equipment[i][EQ_ID] = i + 1
        
    return {
        "id": new_id,
        "name": name,
        "stock": stock,
        "status": status
    }

def remove_equipment_by_id(eq_id):
    """Remove equipment by ID using multidimensional array operations"""
    global equipment
    
    for i in range(len(equipment)):
        if equipment[i][EQ_ID] == eq_id:
            # Store the removed data before deletion
            removed_data = {
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            }
            # Remove entire row from 2D array
            equipment.pop(i)
            return removed_data
    return None

def remove_equipment_by_name(name):
    """Remove equipment by name using multidimensional array operations"""
    global equipment
    
    for i in range(len(equipment)):
        if equipment[i][EQ_NAME].lower() == name.lower():
            # Store the removed data before deletion
            removed_data = {
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            }
            # Remove entire row from 2D array
            equipment.pop(i)
            return removed_data
    return None

def get_equipment_by_index(index):
    """Get equipment by multidimensional array index"""
    if 0 <= index < len(equipment):
        return {
            "id": equipment[index][EQ_ID],
            "name": equipment[index][EQ_NAME],
            "stock": equipment[index][EQ_STOCK],
            "status": equipment[index][EQ_STATUS]
        }
    return None

def insert_equipment(name, stock, status):
    """Add equipment using basic multidimensional array append operation"""
    return add_equipment(name, stock, status)

def fetch_equipment():
    """Fetch all equipment from multidimensional array"""
    return [(equipment[i][EQ_ID], equipment[i][EQ_NAME], equipment[i][EQ_STOCK], equipment[i][EQ_STATUS]) 
            for i in range(len(equipment))]

def get_equipment_count():
    """Get total number of equipment in multidimensional array"""
    return len(equipment)

def is_equipment_empty():
    """Check if equipment multidimensional array is empty"""
    return len(equipment) == 0

def clear_all_equipment():
    """Clear all equipment from multidimensional array"""
    global equipment
    equipment.clear()

def update_equipment(row_id, name, stock, status):
    """Update equipment using multidimensional array operations"""
    global equipment
    
    for i in range(len(equipment)):
        if equipment[i][EQ_ID] == row_id:
            equipment[i][EQ_NAME] = name
            equipment[i][EQ_STOCK] = stock
            equipment[i][EQ_STATUS] = status
            return True
    return False

def find_equipment_by_id(row_id):
    """Find equipment by ID using multidimensional array operations"""
    for i in range(len(equipment)):
        if equipment[i][EQ_ID] == row_id:
            return {
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            }
    return None

def find_equipment_by_name(name):
    """Find equipment by name using multidimensional array operations"""
    for i in range(len(equipment)):
        if equipment[i][EQ_NAME].lower() == name.lower():
            return {
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            }
    return None

def delete_equipment(row_id):
    """Delete equipment using multidimensional array operations"""
    return remove_equipment_by_id(row_id)

# -------------------------
# Array Sorting Functions
# -------------------------
def sort_medicines_by_name(ascending=True):
    """Sort medicines multidimensional array by name"""
    global medicines
    
    # Sort the 2D array by name column
    medicines.sort(key=lambda row: row[MED_NAME].lower(), reverse=not ascending)
    
    return [{"id": medicines[i][MED_ID], "name": medicines[i][MED_NAME], "packs": medicines[i][MED_PACKS], 
             "items_per_pack": medicines[i][MED_ITEMS_PER_PACK], "total_qty": medicines[i][MED_TOTAL_QTY], 
             "expiry": medicines[i][MED_EXPIRY]} for i in range(len(medicines))]

def sort_medicines_by_expiry(ascending=True):
    """Sort medicines multidimensional array by expiry date"""
    global medicines
    
    # Sort the 2D array by expiry column
    medicines.sort(key=lambda row: row[MED_EXPIRY], reverse=not ascending)
    
    return [{"id": medicines[i][MED_ID], "name": medicines[i][MED_NAME], "packs": medicines[i][MED_PACKS], 
             "items_per_pack": medicines[i][MED_ITEMS_PER_PACK], "total_qty": medicines[i][MED_TOTAL_QTY], 
             "expiry": medicines[i][MED_EXPIRY]} for i in range(len(medicines))]

def sort_medicines_by_total_qty(ascending=True):
    """Sort medicines multidimensional array by total quantity"""
    global medicines
    
    # Sort the 2D array by total_qty column
    medicines.sort(key=lambda row: row[MED_TOTAL_QTY], reverse=not ascending)
    
    return [{"id": medicines[i][MED_ID], "name": medicines[i][MED_NAME], "packs": medicines[i][MED_PACKS], 
             "items_per_pack": medicines[i][MED_ITEMS_PER_PACK], "total_qty": medicines[i][MED_TOTAL_QTY], 
             "expiry": medicines[i][MED_EXPIRY]} for i in range(len(medicines))]

def sort_medicines_by_packs(ascending=True):
    """Sort medicines multidimensional array by packs"""
    global medicines
    
    # Sort the 2D array by packs column
    medicines.sort(key=lambda row: row[MED_PACKS], reverse=not ascending)
    
    return [{"id": medicines[i][MED_ID], "name": medicines[i][MED_NAME], "packs": medicines[i][MED_PACKS], 
             "items_per_pack": medicines[i][MED_ITEMS_PER_PACK], "total_qty": medicines[i][MED_TOTAL_QTY], 
             "expiry": medicines[i][MED_EXPIRY]} for i in range(len(medicines))]

def sort_equipment_by_name(ascending=True):
    """Sort equipment multidimensional array by name"""
    global equipment
    
    # Sort the 2D array by name column
    equipment.sort(key=lambda row: row[EQ_NAME].lower(), reverse=not ascending)
    
    return [{"id": equipment[i][EQ_ID], "name": equipment[i][EQ_NAME], "stock": equipment[i][EQ_STOCK], 
             "status": equipment[i][EQ_STATUS]} for i in range(len(equipment))]

def sort_equipment_by_stock(ascending=True):
    """Sort equipment multidimensional array by stock quantity"""
    global equipment
    
    # Sort the 2D array by stock column
    equipment.sort(key=lambda row: row[EQ_STOCK], reverse=not ascending)
    
    return [{"id": equipment[i][EQ_ID], "name": equipment[i][EQ_NAME], "stock": equipment[i][EQ_STOCK], 
             "status": equipment[i][EQ_STATUS]} for i in range(len(equipment))]

def sort_equipment_by_status(ascending=True):
    """Sort equipment multidimensional array by status"""
    global equipment
    
    # Sort the 2D array by status column
    equipment.sort(key=lambda row: row[EQ_STATUS].lower(), reverse=not ascending)
    
    return [{"id": equipment[i][EQ_ID], "name": equipment[i][EQ_NAME], "stock": equipment[i][EQ_STOCK], 
             "status": equipment[i][EQ_STATUS]} for i in range(len(equipment))]

# -------------------------
# Array Filtering Functions
# -------------------------
def filter_medicines_by_expiry_range(start_date, end_date):
    """Filter medicines by expiry date range using multidimensional array"""
    from datetime import datetime
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        result = []
        for i in range(len(medicines)):
            if start <= datetime.strptime(medicines[i][MED_EXPIRY], "%Y-%m-%d") <= end:
                result.append({
                    "id": medicines[i][MED_ID],
                    "name": medicines[i][MED_NAME],
                    "packs": medicines[i][MED_PACKS],
                    "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                    "total_qty": medicines[i][MED_TOTAL_QTY],
                    "expiry": medicines[i][MED_EXPIRY]
                })
        return result
    except ValueError:
        return []

def filter_medicines_by_low_stock(threshold=5):
    """Filter medicines with low stock (total_qty <= threshold) using multidimensional array"""
    result = []
    for i in range(len(medicines)):
        if medicines[i][MED_TOTAL_QTY] <= threshold:
            result.append({
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            })
    return result

def filter_medicines_by_name_pattern(pattern):
    """Filter medicines by name pattern (case-insensitive) using multidimensional array"""
    result = []
    for i in range(len(medicines)):
        if pattern.lower() in medicines[i][MED_NAME].lower():
            result.append({
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            })
    return result

def get_medicines_slice(start, end):
    """Get a slice of medicines multidimensional array using slicing operation"""
    result = []
    for i in range(start, min(end, len(medicines))):
        result.append({
            "id": medicines[i][MED_ID],
            "name": medicines[i][MED_NAME],
            "packs": medicines[i][MED_PACKS],
            "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
            "total_qty": medicines[i][MED_TOTAL_QTY],
            "expiry": medicines[i][MED_EXPIRY]
        })
    return result

def filter_medicines_by_packs_range(min_packs, max_packs):
    """Filter medicines by packs range using multidimensional array"""
    result = []
    for i in range(len(medicines)):
        if min_packs <= medicines[i][MED_PACKS] <= max_packs:
            result.append({
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            })
    return result

def filter_equipment_by_stock_level(threshold, above=True):
    """Filter equipment by stock level using multidimensional array"""
    result = []
    for i in range(len(equipment)):
        if above and equipment[i][EQ_STOCK] >= threshold:
            result.append({
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            })
        elif not above and equipment[i][EQ_STOCK] <= threshold:
            result.append({
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            })
    return result

def filter_equipment_by_status_pattern(pattern):
    """Filter equipment by status pattern (case-insensitive) using multidimensional array"""
    result = []
    for i in range(len(equipment)):
        if pattern.lower() in equipment[i][EQ_STATUS].lower():
            result.append({
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            })
    return result

def filter_equipment_by_name_pattern(pattern):
    """Filter equipment by name pattern (case-insensitive) using multidimensional array"""
    result = []
    for i in range(len(equipment)):
        if pattern.lower() in equipment[i][EQ_NAME].lower():
            result.append({
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            })
    return result

def get_equipment_slice(start, end):
    """Get a slice of equipment multidimensional array using slicing operation"""
    result = []
    for i in range(start, min(end, len(equipment))):
        result.append({
            "id": equipment[i][EQ_ID],
            "name": equipment[i][EQ_NAME],
            "stock": equipment[i][EQ_STOCK],
            "status": equipment[i][EQ_STATUS]
        })
    return result

def filter_equipment_by_stock_range(min_stock, max_stock):
    """Filter equipment by stock range using multidimensional array"""
    result = []
    for i in range(len(equipment)):
        if min_stock <= equipment[i][EQ_STOCK] <= max_stock:
            result.append({
                "id": equipment[i][EQ_ID],
                "name": equipment[i][EQ_NAME],
                "stock": equipment[i][EQ_STOCK],
                "status": equipment[i][EQ_STATUS]
            })
    return result

# -------------------------
# Advanced Array Operations
# -------------------------
def get_medicines_sorted_by_expiry():
    """Get medicines sorted by expiry date (earliest first)"""
    return sort_medicines_by_expiry(ascending=True)

def get_equipment_sorted_by_stock():
    """Get equipment sorted by stock quantity (highest first)"""
    return sort_equipment_by_stock(ascending=False)

def get_low_stock_medicines(threshold=5):
    """Get all medicines with low stock"""
    return filter_medicines_by_low_stock(threshold)

def get_low_stock_equipment(threshold=3):
    """Get all equipment with low stock"""
    return filter_equipment_by_stock_level(threshold, above=False)

def get_expiring_medicines(days_ahead=30):
    """Get medicines expiring within specified days using multidimensional array"""
    from datetime import datetime, timedelta
    cutoff_date = datetime.now() + timedelta(days=days_ahead)
    result = []
    for i in range(len(medicines)):
        if datetime.strptime(medicines[i][MED_EXPIRY], "%Y-%m-%d") <= cutoff_date:
            result.append({
                "id": medicines[i][MED_ID],
                "name": medicines[i][MED_NAME],
                "packs": medicines[i][MED_PACKS],
                "items_per_pack": medicines[i][MED_ITEMS_PER_PACK],
                "total_qty": medicines[i][MED_TOTAL_QTY],
                "expiry": medicines[i][MED_EXPIRY]
            })
    return result

def get_medicines_by_name_search(search_term):
    """Search medicines by name (case-insensitive partial match)"""
    return filter_medicines_by_name_pattern(search_term)

def get_equipment_by_name_search(search_term):
    """Search equipment by name (case-insensitive partial match)"""
    return filter_equipment_by_name_pattern(search_term)

def find_medicine_index_by_id(medicine_id):
    """Find the index of a medicine by its ID using multidimensional array operations (internal utility)"""
    for i in range(len(medicines)):
        if medicines[i][MED_ID] == medicine_id:
            return i
    return -1 # Not found

def count_medicines_by_name(name):
    """Count occurrences of a medicine name using multidimensional array operations (internal utility)"""
    count = 0
    for i in range(len(medicines)):
        if medicines[i][MED_NAME].lower() == name.lower():
            count += 1
    return count

def find_equipment_index_by_id(eq_id):
    """Find the index of an equipment by its ID using multidimensional array operations (internal utility)"""
    for i in range(len(equipment)):
        if equipment[i][EQ_ID] == eq_id:
            return i
    return -1 # Not found

def count_equipment_by_name(name):
    """Count occurrences of an equipment name using multidimensional array operations (internal utility)"""
    count = 0
    for i in range(len(equipment)):
        if equipment[i][EQ_NAME].lower() == name.lower():
            count += 1
    return count

def get_array_statistics():
    """Get statistics about the multidimensional arrays"""
    med_count = len(medicines)
    eq_count = len(equipment)
    low_stock_med = len(get_low_stock_medicines())
    low_stock_eq = len(get_low_stock_equipment())
    expiring_med = len(get_expiring_medicines())
    
    return {
        "medicines_count": med_count,
        "equipment_count": eq_count,
        "low_stock_medicines": low_stock_med,
        "low_stock_equipment": low_stock_eq,
        "expiring_medicines": expiring_med
    }


# ---------------- APP CLASS ----------------
class ClinicInventoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🏥 Clinic Inventory System")
        self.geometry("1000x600")
        self.minsize(900, 550)

        # Data Structure initialization - using Python lists with basic operations

        # Selected item ids
        self.selected_medicine_id = None
        self.selected_equipment_id = None

        # Initialize a deque for a fixed-size transaction log (Queue Data Structure)
        # collections.deque is chosen over a list for queues because it provides O(1) complexity
        # for append and popleft operations, which are essential for efficient queue management.
        # A regular list would have O(n) for pop(0) due to element shifting.
        self.transaction_log = collections.deque(maxlen=7) # Keep last 7 transactions
        # self.log_transaction("Application started.") # Moved to after UI creation

        # Initialize with default data
        initialize_default_data()
        
        self.create_ui()
        self.load_all_tables()
        self.log_transaction("Application started.")

    def log_transaction(self, message):
        """Logs a transaction message to the deque-based transaction log (Queue)"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.transaction_log.append(f"[{timestamp}] {message}")
        self.update_transaction_log_display()

    # ---------- UI ----------
    def create_ui(self):
        # Top area: tabs
        tabview = ctk.CTkTabview(self, width=980, height=580)
        tabview.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        tabview.add("Medicines")
        tabview.add("Equipment")

        self.create_medicines_tab(tabview.tab("Medicines"))
        self.create_equipment_tab(tabview.tab("Equipment"))

        # Transaction Log Display
        log_frame = ctk.CTkFrame(self)
        log_frame.pack(fill="x", padx=10, pady=(5, 10))
        ctk.CTkLabel(log_frame, text="Recent Activity Log:").pack(side="left", padx=5, pady=5)
        self.log_display = ctk.CTkTextbox(log_frame, height=50, state="disabled", wrap="word")
        self.log_display.pack(fill="x", expand=True, padx=5, pady=5)
        self.update_transaction_log_display()

        # Time display at top right
        time_frame = ctk.CTkFrame(self)
        time_frame.place(relx=1.0, rely=0, x=-10, y=10, anchor="ne")
        self.time_label = ctk.CTkLabel(time_frame, text="", font=("Arial", 12))
        self.time_label.pack(padx=5, pady=5)
        self.update_time()

    # ---------- MEDICINES TAB ----------
    def create_medicines_tab(self, parent):
        # Input frame
        frm = ctk.CTkFrame(parent)
        frm.pack(fill="x", padx=10, pady=(10, 5))

        # Name
        ctk.CTkLabel(frm, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.med_name = ctk.CTkEntry(frm, width=240, placeholder_text="Medicine name")
        self.med_name.grid(row=1, column=0, padx=5, pady=5)

        # Packs
        ctk.CTkLabel(frm, text="Packs").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.med_packs = ctk.CTkEntry(frm, width=100, placeholder_text="e.g. 5")
        self.med_packs.grid(row=1, column=1, padx=5, pady=5)

        # Items per pack
        ctk.CTkLabel(frm, text="Items / Pack").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.med_items_per_pack = ctk.CTkEntry(frm, width=120, placeholder_text="e.g. 10")
        self.med_items_per_pack.grid(row=1, column=2, padx=5, pady=5)

        # Total qty (readonly)
        ctk.CTkLabel(frm, text="Total Quantity").grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.med_total_qty = ctk.CTkEntry(frm, width=120)
        self.med_total_qty.grid(row=1, column=3, padx=5, pady=5)
        self.med_total_qty.configure(state="disabled")

        # Expiry date
        ctk.CTkLabel(frm, text="Expiry (YYYY-MM-DD)").grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.med_expiry = ctk.CTkEntry(frm, width=150, placeholder_text="YYYY-MM-DD")
        self.med_expiry.grid(row=1, column=4, padx=5, pady=5)

        # New Actions Frame
        actions_frm = ctk.CTkFrame(parent)
        actions_frm.pack(fill="x", padx=10, pady=(5, 5))

        # Add/Insert Buttons
        add_btn = ctk.CTkButton(actions_frm, text="➕ Add Medicine", command=self.add_medicine)
        add_btn.pack(side="left", padx=8, pady=5)

        insert_first_btn = ctk.CTkButton(actions_frm, text="➕ Insert First", fg_color="darkgreen", command=self.insert_medicine_first)
        insert_first_btn.pack(side="left", padx=8, pady=5)

        update_btn = ctk.CTkButton(actions_frm, text="📝 Update Medicine", fg_color="orange", command=self.update_medicine_ui)
        update_btn.pack(side="left", padx=8, pady=5)

        # View Buttons
        view_btn = ctk.CTkButton(actions_frm, text="👁 View Last", fg_color="green", command=self.view_last_medicine)
        view_btn.pack(side="left", padx=(20, 8), pady=5)

        view_slice_btn = ctk.CTkButton(actions_frm, text="✂ View First 3", fg_color="purple", command=self.view_medicine_slice)
        view_slice_btn.pack(side="left", padx=8, pady=5)

        # Remove by ID Controls
        remove_id_frm = ctk.CTkFrame(parent)
        remove_id_frm.pack(fill="x", padx=10, pady=(5, 5))

        ctk.CTkLabel(remove_id_frm, text="Remove by ID:").pack(side="left", padx=5, pady=5)
        self.med_remove_id_entry = ctk.CTkEntry(remove_id_frm, width=60, placeholder_text="ID")
        self.med_remove_id_entry.pack(side="left", padx=5, pady=5)
        ctk.CTkButton(remove_id_frm, text="🗑 Remove by ID", fg_color="darkred", command=self.remove_medicine_by_id_ui).pack(side="left", padx=5, pady=5)
        remove_last_btn = ctk.CTkButton(remove_id_frm, text="🗑 Remove Last", fg_color="darkred", command=self.remove_last_medicine)
        remove_last_btn.pack(side="left", padx=(20, 5), pady=5)

        # Sort and Filter Controls
        sort_filter_frm = ctk.CTkFrame(parent)
        sort_filter_frm.pack(fill="x", padx=10, pady=(0, 5))
        
        # Sort Controls
        ctk.CTkLabel(sort_filter_frm, text="Sort by:").pack(side="left", padx=5, pady=5)
        self.med_sort_var = ctk.StringVar(value="name")
        med_sort_combo = ctk.CTkComboBox(sort_filter_frm, values=["name", "expiry", "total_qty", "packs"], 
                                        variable=self.med_sort_var, width=100)
        med_sort_combo.pack(side="left", padx=5, pady=5)
        
        self.med_sort_order = ctk.StringVar(value="asc")
        med_order_combo = ctk.CTkComboBox(sort_filter_frm, values=["asc", "desc"], 
                                        variable=self.med_sort_order, width=80)
        med_order_combo.pack(side="left", padx=5, pady=5)
        
        ctk.CTkButton(sort_filter_frm, text="🔄 Sort", width=80, command=self.sort_medicines).pack(side="left", padx=5, pady=5)
        
        # Filter Controls
        ctk.CTkLabel(sort_filter_frm, text="Filter:").pack(side="left", padx=(20, 5), pady=5)
        self.med_filter_type = ctk.StringVar(value="name")
        med_filter_combo = ctk.CTkComboBox(sort_filter_frm, values=["name", "low_stock", "expiry_range", "packs_range"], 
                                          variable=self.med_filter_type, width=120)
        med_filter_combo.pack(side="left", padx=5, pady=5)
        
        self.med_filter_value = ctk.CTkEntry(sort_filter_frm, placeholder_text="Filter value", width=150)
        self.med_filter_value.pack(side="left", padx=5, pady=5)
        
        ctk.CTkButton(sort_filter_frm, text="🔍 Filter", width=80, command=self.filter_medicines).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(sort_filter_frm, text="⟳ Reset", width=80, command=self.load_medicines_table).pack(side="left", padx=5, pady=5)

        # Search
        searchfrm = ctk.CTkFrame(parent)
        searchfrm.pack(fill="x", padx=10, pady=(0, 5))
        self.med_search = ctk.CTkEntry(searchfrm, placeholder_text="Search medicines by name")
        self.med_search.pack(side="left", padx=6, pady=6, fill="x", expand=True)
        ctk.CTkButton(searchfrm, text="🔍 Search", width=100, command=self.search_medicines).pack(side="left", padx=6)
        ctk.CTkButton(searchfrm, text="⟳ Reset", width=80, command=self.load_medicines_table).pack(side="left", padx=6)

        # Table
        tablefrm = ctk.CTkFrame(parent)
        tablefrm.pack(fill="both", expand=True, padx=10, pady=8)

        cols = ("id", "name", "packs", "items_per_pack", "total_qty", "expiry")
        self.med_tree = ttk.Treeview(tablefrm, columns=cols, show="headings", selectmode="browse")
        for col in cols:
            self.med_tree.heading(col, text=col.capitalize())
            # nicer widths
            if col == "name":
                self.med_tree.column(col, width=300, anchor="w")
            elif col == "expiry":
                self.med_tree.column(col, width=110, anchor="center")
            else:
                self.med_tree.column(col, width=90, anchor="center")
        self.med_tree.pack(fill="both", expand=True, side="left")
        self.med_tree.bind("<<TreeviewSelect>>", self.on_med_select)

        # Scrollbar
        scrollbar = ttk.Scrollbar(tablefrm, orient="vertical", command=self.med_tree.yview)
        self.med_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Style & tag for low stock
        style = ttk.Style()
        style.configure("Treeview", rowheight=26, font=("Arial", 11))
        self.med_tree.tag_configure("low", background="#ffdddd")

    # ---------- EQUIPMENT TAB ----------
    def create_equipment_tab(self, parent):
        frm = ctk.CTkFrame(parent)
        frm.pack(fill="x", padx=10, pady=(10, 5))

        # Name
        ctk.CTkLabel(frm, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.eq_name = ctk.CTkEntry(frm, width=320, placeholder_text="Equipment name")
        self.eq_name.grid(row=1, column=0, padx=5, pady=5)

        # Quantity
        ctk.CTkLabel(frm, text="Quantity").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.eq_quantity = ctk.CTkEntry(frm, width=120, placeholder_text="e.g. 3")
        self.eq_quantity.grid(row=1, column=1, padx=5, pady=5)

        # Description
        ctk.CTkLabel(frm, text="Description / Location (optional)").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.eq_description = ctk.CTkEntry(frm, width=360, placeholder_text="e.g. First-aid cabinet")
        self.eq_description.grid(row=1, column=2, padx=5, pady=5)

        # New Actions Frame
        actions_frm = ctk.CTkFrame(parent)
        actions_frm.pack(fill="x", padx=10, pady=(5, 5))

        # Add/Insert Buttons
        add_btn = ctk.CTkButton(actions_frm, text="➕ Add Equipment", command=self.add_equipment)
        add_btn.pack(side="left", padx=8, pady=5)

        insert_first_btn = ctk.CTkButton(actions_frm, text="➕ Insert First", fg_color="darkgreen", command=self.insert_equipment_first)
        insert_first_btn.pack(side="left", padx=8, pady=5)

        update_btn = ctk.CTkButton(actions_frm, text="📝 Update Equipment", fg_color="orange", command=self.update_equipment_ui)
        update_btn.pack(side="left", padx=8, pady=5)

        # View Buttons
        view_btn = ctk.CTkButton(actions_frm, text="👁 View Last", fg_color="green", command=self.view_last_equipment)
        view_btn.pack(side="left", padx=(20, 8), pady=5)

        view_slice_btn = ctk.CTkButton(actions_frm, text="✂ View First 3", fg_color="purple", command=self.view_equipment_slice)
        view_slice_btn.pack(side="left", padx=8, pady=5)

        # Remove Buttons
        remove_last_btn = ctk.CTkButton(actions_frm, text="🗑 Remove Last", fg_color="darkred", command=self.remove_last_equipment)
        remove_last_btn.pack(side="left", padx=(20, 8), pady=5)

        # Remove by ID Controls
        remove_id_frm = ctk.CTkFrame(parent)
        remove_id_frm.pack(fill="x", padx=10, pady=(5, 5))

        ctk.CTkLabel(remove_id_frm, text="Remove by ID:").pack(side="left", padx=5, pady=5)
        self.eq_remove_id_entry = ctk.CTkEntry(remove_id_frm, width=60, placeholder_text="ID")
        self.eq_remove_id_entry.pack(side="left", padx=5, pady=5)
        ctk.CTkButton(remove_id_frm, text="🗑 Remove by ID", fg_color="darkred", command=self.remove_equipment_by_id_ui).pack(side="left", padx=5, pady=5)
        remove_last_btn = ctk.CTkButton(remove_id_frm, text="🗑 Remove Last", fg_color="darkred", command=self.remove_last_equipment)
        remove_last_btn.pack(side="left", padx=(20, 5), pady=5)

        # Sort and Filter Controls
        sort_filter_frm = ctk.CTkFrame(parent)
        sort_filter_frm.pack(fill="x", padx=10, pady=(0, 5))
        
        # Sort Controls
        ctk.CTkLabel(sort_filter_frm, text="Sort by:").pack(side="left", padx=5, pady=5)
        self.eq_sort_var = ctk.StringVar(value="name")
        eq_sort_combo = ctk.CTkComboBox(sort_filter_frm, values=["name", "stock", "status"], 
                                       variable=self.eq_sort_var, width=100)
        eq_sort_combo.pack(side="left", padx=5, pady=5)
        
        self.eq_sort_order = ctk.StringVar(value="asc")
        eq_order_combo = ctk.CTkComboBox(sort_filter_frm, values=["asc", "desc"], 
                                       variable=self.eq_sort_order, width=80)
        eq_order_combo.pack(side="left", padx=5, pady=5)
        
        ctk.CTkButton(sort_filter_frm, text="🔄 Sort", width=80, command=self.sort_equipment).pack(side="left", padx=5, pady=5)
        
        # Filter Controls
        ctk.CTkLabel(sort_filter_frm, text="Filter:").pack(side="left", padx=(20, 5), pady=5)
        self.eq_filter_type = ctk.StringVar(value="name")
        eq_filter_combo = ctk.CTkComboBox(sort_filter_frm, values=["name", "status", "stock_level", "stock_range"], 
                                         variable=self.eq_filter_type, width=120)
        eq_filter_combo.pack(side="left", padx=5, pady=5)
        
        self.eq_filter_value = ctk.CTkEntry(sort_filter_frm, placeholder_text="Filter value", width=150)
        self.eq_filter_value.pack(side="left", padx=5, pady=5)
        
        ctk.CTkButton(sort_filter_frm, text="🔍 Filter", width=80, command=self.filter_equipment).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(sort_filter_frm, text="⟳ Reset", width=80, command=self.load_equipment_table).pack(side="left", padx=5, pady=5)

        # Search
        searchfrm = ctk.CTkFrame(parent)
        searchfrm.pack(fill="x", padx=10, pady=(0, 5))
        self.eq_search = ctk.CTkEntry(searchfrm, placeholder_text="Search equipment by name or description")
        self.eq_search.pack(side="left", padx=6, pady=6, fill="x", expand=True)
        ctk.CTkButton(searchfrm, text="🔍 Search", width=100, command=self.search_equipment).pack(side="left", padx=6)
        ctk.CTkButton(searchfrm, text="⟳ Reset", width=80, command=self.load_equipment_table).pack(side="left", padx=6)

        # Table
        tablefrm = ctk.CTkFrame(parent)
        tablefrm.pack(fill="both", expand=True, padx=10, pady=8)

        cols = ("id", "name", "quantity", "description")
        self.eq_tree = ttk.Treeview(tablefrm, columns=cols, show="headings", selectmode="browse")
        for col in cols:
            self.eq_tree.heading(col, text=col.capitalize())
            if col == "name":
                self.eq_tree.column(col, width=350, anchor="w")
            else:
                self.eq_tree.column(col, width=120, anchor="center")
        self.eq_tree.pack(fill="both", expand=True, side="left")
        self.eq_tree.bind("<<TreeviewSelect>>", self.on_eq_select)

        scrollbar = ttk.Scrollbar(tablefrm, orient="vertical", command=self.eq_tree.yview)
        self.eq_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Style & tag for low stock
        style = ttk.Style()
        style.configure("Treeview", rowheight=26, font=("Arial", 11))
        self.eq_tree.tag_configure("low", background="#fff0cc")



    # ---------- LOAD & DISPLAY ----------
    def load_all_tables(self):
        self.load_medicines_table()
        self.load_equipment_table()

    def load_medicines_table(self):
        for row in self.med_tree.get_children():
            self.med_tree.delete(row)
        rows = fetch_medicines()
        for r in rows:
            rid, name, packs, items_per_pack, total_qty, expiry = r
            self.med_tree.insert("", "end", values=(rid, name, packs, items_per_pack, total_qty, expiry))
        self.highlight_med_low_stock()

    def load_equipment_table(self):
        for row in self.eq_tree.get_children():
            self.eq_tree.delete(row)
        rows = fetch_equipment()
        for r in rows:
            rid, name, quantity, description = r
            self.eq_tree.insert("", "end", values=(rid, name, quantity, description))
        self.highlight_eq_low_stock()

    # ---------- HIGHLIGHT RULES ----------
    def highlight_med_low_stock(self):
        for item in self.med_tree.get_children():
            vals = self.med_tree.item(item, "values")
            packs = int(vals[2])
            total_qty = int(vals[4])
            # low if packs <= 2 or total qty <=5 OR expiry is near/past (you can extend)
            if packs <= 2 or total_qty <= 5:
                self.med_tree.item(item, tags=("low",))
            else:
                self.med_tree.item(item, tags=())

    def highlight_eq_low_stock(self):
        for item in self.eq_tree.get_children():
            vals = self.eq_tree.item(item, "values")
            quantity = int(vals[2])
            if quantity <= 2:
                self.eq_tree.item(item, tags=("low",))
            else:
                self.eq_tree.item(item, tags=())

    # ---------- MEDICINE ACTIONS ----------
    def calc_med_total(self):
        # safe calculation of packs * items_per_pack
        try:
            p = int(self.med_packs.get().strip()) if self.med_packs.get().strip() else 0
            ipp = int(self.med_items_per_pack.get().strip()) if self.med_items_per_pack.get().strip() else 0
            total = p * ipp
        except ValueError:
            total = 0
        # update readonly entry
        self.med_total_qty.configure(state="normal")
        self.med_total_qty.delete(0, "end")
        self.med_total_qty.insert(0, str(total))
        self.med_total_qty.configure(state="disabled")
        return total

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except Exception:
            return False

    def add_medicine(self):
        name = self.med_name.get().strip()
        packs = self.med_packs.get().strip()
        ipp = self.med_items_per_pack.get().strip()
        expiry = self.med_expiry.get().strip()

        if not name or not packs or not ipp or not expiry:
            messagebox.showerror("Error", "Please fill all medicine fields.")
            return
        if not packs.isdigit() or not ipp.isdigit():
            messagebox.showerror("Error", "Packs and Items/Pack must be integers.")
            return
        if not self.validate_date(expiry):
            messagebox.showerror("Error", "Expiry date must be in YYYY-MM-DD format.")
            return

        packs_i = int(packs)
        ipp_i = int(ipp)
        total = packs_i * ipp_i

        add_medicine(name, packs_i, ipp_i, total, expiry)  # Using list append operation
        self.load_medicines_table()
        self.clear_med_entries()
        self.log_transaction(f"Added medicine: {name}")

    # Removed on_med_select - items can only be accessed by index operations
    def on_med_select(self, event):
        """Load selected medicine data into input fields"""
        selected_item = self.med_tree.focus()
        if selected_item:
            values = self.med_tree.item(selected_item, 'values')
            self.selected_medicine_id = values[0]
            self.med_name.delete(0, "end")
            self.med_name.insert(0, values[1])
            self.med_packs.delete(0, "end")
            self.med_packs.insert(0, values[2])
            self.med_items_per_pack.delete(0, "end")
            self.med_items_per_pack.insert(0, values[3])
            # Total qty is read-only, so update its text
            self.med_total_qty.configure(state="normal")
            self.med_total_qty.delete(0, "end")
            self.med_total_qty.insert(0, values[4])
            self.med_total_qty.configure(state="disabled")
            self.med_expiry.delete(0, "end")
            self.med_expiry.insert(0, values[5])
        else:
            self.clear_med_entries()

    def search_medicines(self):
        q = self.med_search.get().strip().lower()
        if not q:
            messagebox.showinfo("Info", "Enter search keywords.")
            return
        rows = fetch_medicines()
        filtered = [r for r in rows if q in r[1].lower()]
        for row in self.med_tree.get_children():
            self.med_tree.delete(row)
        for r in filtered:
            self.med_tree.insert("", "end", values=r)
        self.highlight_med_low_stock()

    def clear_med_entries(self):
        self.med_name.delete(0, "end")
        self.med_packs.delete(0, "end")
        self.med_items_per_pack.delete(0, "end")
        self.med_expiry.delete(0, "end")
        self.med_total_qty.configure(state="normal")
        self.med_total_qty.delete(0, "end")
        self.med_total_qty.configure(state="disabled")
        self.selected_medicine_id = None

    # ---------- EQUIPMENT ACTIONS ----------
    def add_equipment(self):
        name = self.eq_name.get().strip()
        quantity = self.eq_quantity.get().strip()
        desc = self.eq_description.get().strip()

        if not name or not quantity:
            messagebox.showerror("Error", "Please fill name and quantity for equipment.")
            return
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be an integer.")
            return
        add_equipment(name, int(quantity), desc)  # Using list append operation
        self.load_equipment_table()
        self.clear_eq_entries()
        self.log_transaction(f"Added equipment: {name}")

    # Removed on_eq_select - items can only be accessed by index operations
    def on_eq_select(self, event):
        """Load selected equipment data into input fields"""
        selected_item = self.eq_tree.focus()
        if selected_item:
            values = self.eq_tree.item(selected_item, 'values')
            self.selected_equipment_id = values[0]
            self.eq_name.delete(0, "end")
            self.eq_name.insert(0, values[1])
            self.eq_quantity.delete(0, "end")
            self.eq_quantity.insert(0, values[2])
            self.eq_description.delete(0, "end")
            self.eq_description.insert(0, values[3])
        else:
            self.clear_eq_entries()

    def search_equipment(self):
        q = self.eq_search.get().strip().lower()
        if not q:
            messagebox.showinfo("Info", "Enter search keywords.")
            return
        rows = fetch_equipment()
        filtered = [r for r in rows if q in r[1].lower() or (r[3] and q in r[3].lower())]
        for row in self.eq_tree.get_children():
            self.eq_tree.delete(row)
        for r in filtered:
            self.eq_tree.insert("", "end", values=r)
        self.highlight_eq_low_stock()

    def clear_eq_entries(self):
        self.eq_name.delete(0, "end")
        self.eq_quantity.delete(0, "end")
        self.eq_description.delete(0, "end")
        self.selected_equipment_id = None

    # ---------- SORTING METHODS ----------
    def sort_medicines(self):
        """Sort medicines based on selected criteria"""
        sort_by = self.med_sort_var.get()
        ascending = self.med_sort_order.get() == "asc"
        
        if sort_by == "name":
            sort_medicines_by_name(ascending)
        elif sort_by == "expiry":
            sort_medicines_by_expiry(ascending)
        elif sort_by == "total_qty":
            sort_medicines_by_total_qty(ascending)
        elif sort_by == "packs":
            sort_medicines_by_packs(ascending)
        
        self.load_medicines_table()
        messagebox.showinfo("Sort Complete", f"Medicines sorted by {sort_by} ({'ascending' if ascending else 'descending'})")

    def sort_equipment(self):
        """Sort equipment based on selected criteria"""
        sort_by = self.eq_sort_var.get()
        ascending = self.eq_sort_order.get() == "asc"
        
        if sort_by == "name":
            sort_equipment_by_name(ascending)
        elif sort_by == "stock":
            sort_equipment_by_stock(ascending)
        elif sort_by == "status":
            sort_equipment_by_status(ascending)
        
        self.load_equipment_table()
        messagebox.showinfo("Sort Complete", f"Equipment sorted by {sort_by} ({'ascending' if ascending else 'descending'})")

    # ---------- FILTERING METHODS ----------
    def filter_medicines(self):
        """Filter medicines based on selected criteria"""
        filter_type = self.med_filter_type.get()
        filter_value = self.med_filter_value.get().strip()
        
        if not filter_value:
            messagebox.showwarning("Warning", "Please enter a filter value!")
            return
        
        filtered_medicines = []
        
        if filter_type == "name":
            filtered_medicines = filter_medicines_by_name_pattern(filter_value)
        elif filter_type == "low_stock":
            try:
                threshold = int(filter_value)
                filtered_medicines = filter_medicines_by_low_stock(threshold)
            except ValueError:
                messagebox.showerror("Error", "Low stock threshold must be a number!")
                return
        elif filter_type == "expiry_range":
            # Expected format: "2026-01-01,2027-12-31"
            try:
                start_date, end_date = filter_value.split(",")
                filtered_medicines = filter_medicines_by_expiry_range(start_date.strip(), end_date.strip())
            except ValueError:
                messagebox.showerror("Error", "Expiry range format: start_date,end_date (YYYY-MM-DD,YYYY-MM-DD)")
                return
        elif filter_type == "packs_range":
            # Expected format: "1,10"
            try:
                min_packs, max_packs = filter_value.split(",")
                filtered_medicines = filter_medicines_by_packs_range(int(min_packs.strip()), int(max_packs.strip()))
            except ValueError:
                messagebox.showerror("Error", "Packs range format: min,max (e.g., 1,10)")
                return
        
        # Display filtered results
        self.display_filtered_medicines(filtered_medicines)
        
        if not filtered_medicines:
            messagebox.showinfo("Filter Results", "No medicines match the filter criteria.")
        else:
            messagebox.showinfo("Filter Results", f"Found {len(filtered_medicines)} medicines matching the filter.")

    def filter_equipment(self):
        """Filter equipment based on selected criteria"""
        filter_type = self.eq_filter_type.get()
        filter_value = self.eq_filter_value.get().strip()
        
        if not filter_value:
            messagebox.showwarning("Warning", "Please enter a filter value!")
            return
        
        filtered_equipment = []
        
        if filter_type == "name":
            filtered_equipment = filter_equipment_by_name_pattern(filter_value)
        elif filter_type == "status":
            filtered_equipment = filter_equipment_by_status_pattern(filter_value)
        elif filter_type == "stock_level":
            # Expected format: "5,above" or "5,below"
            try:
                threshold_str, direction = filter_value.split(",")
                threshold = int(threshold_str.strip())
                above = direction.strip().lower() == "above"
                filtered_equipment = filter_equipment_by_stock_level(threshold, above)
            except ValueError:
                messagebox.showerror("Error", "Stock level format: threshold,direction (e.g., 5,above or 3,below)")
                return
        elif filter_type == "stock_range":
            # Expected format: "1,10"
            try:
                min_stock, max_stock = filter_value.split(",")
                filtered_equipment = filter_equipment_by_stock_range(int(min_stock.strip()), int(max_stock.strip()))
            except ValueError:
                messagebox.showerror("Error", "Stock range format: min,max (e.g., 1,10)")
                return
        
        # Display filtered results
        self.display_filtered_equipment(filtered_equipment)
        
        if not filtered_equipment:
            messagebox.showinfo("Filter Results", "No equipment matches the filter criteria.")
        else:
            messagebox.showinfo("Filter Results", f"Found {len(filtered_equipment)} equipment matching the filter.")

    def display_filtered_medicines(self, filtered_medicines):
        """Display filtered medicines in the table"""
        for row in self.med_tree.get_children():
            self.med_tree.delete(row)
        
        for medicine in filtered_medicines:
            self.med_tree.insert("", "end", values=(
                medicine["id"], 
                medicine["name"], 
                medicine["packs"], 
                medicine["items_per_pack"], 
                medicine["total_qty"], 
                medicine["expiry"]
            ))
        self.highlight_med_low_stock()

    def display_filtered_equipment(self, filtered_equipment):
        """Display filtered equipment in the table"""
        for row in self.eq_tree.get_children():
            self.eq_tree.delete(row)
        
        for eq in filtered_equipment:
            self.eq_tree.insert("", "end", values=(
                eq["id"], 
                eq["name"], 
                eq["stock"], 
                eq["status"]
            ))
        self.highlight_eq_low_stock()

    # ---------- ARRAY OPERATIONS (LIFO) ----------
    def view_last_medicine(self):
        """View the last added medicine in the multidimensional array"""
        if not medicines:
            messagebox.showinfo("View Last Medicine", "No medicines in inventory (multidimensional array is empty)")
            return

        last_index = len(medicines) - 1  # Get last index
        messagebox.showinfo("Last Medicine in Multidimensional Array", 
            f"Last medicine in multidimensional array:\n"
            f"ID: {medicines[last_index][MED_ID]}\n"
            f"Name: {medicines[last_index][MED_NAME]}\n"
            f"Packs: {medicines[last_index][MED_PACKS]}\n"
            f"Items per Pack: {medicines[last_index][MED_ITEMS_PER_PACK]}\n"
            f"Total Qty: {medicines[last_index][MED_TOTAL_QTY]}\n"
            f"Expiry: {medicines[last_index][MED_EXPIRY]}")

    def view_last_equipment(self):
        """View the last added equipment in the multidimensional array"""
        if not equipment:
            messagebox.showinfo("View Last Equipment", "No equipment in inventory (multidimensional array is empty)")
            return
        
        last_index = len(equipment) - 1  # Get last index
        messagebox.showinfo("Last Equipment in Multidimensional Array", 
            f"Last equipment in multidimensional array:\n"
            f"ID: {equipment[last_index][EQ_ID]}\n"
            f"Name: {equipment[last_index][EQ_NAME]}\n"
            f"Stock: {equipment[last_index][EQ_STOCK]}\n"
            f"Status: {equipment[last_index][EQ_STATUS]}")

    def insert_medicine_first(self):
        """Insert a new medicine at the beginning of the list"""
        name = self.med_name.get().strip()
        packs = self.med_packs.get().strip()
        ipp = self.med_items_per_pack.get().strip()
        expiry = self.med_expiry.get().strip()

        if not name or not packs or not ipp or not expiry:
            messagebox.showerror("Error", "Please fill all medicine fields for insertion.")
            return
        if not packs.isdigit() or not ipp.isdigit():
            messagebox.showerror("Error", "Packs and Items/Pack must be integers.")
            return
        if not self.validate_date(expiry):
            messagebox.showerror("Error", "Expiry date must be in YYYY-MM-DD format.")
            return

        packs_i = int(packs)
        ipp_i = int(ipp)
        total = packs_i * ipp_i

        insert_medicine_at_position(0, name, packs_i, ipp_i, total, expiry) # Using list insert(0, item) operation
        self.load_medicines_table()
        self.clear_med_entries()
        messagebox.showinfo("Insert Complete", "Medicine inserted at the beginning of the list.")
        self.log_transaction(f"Inserted medicine at beginning: {name}")

    def insert_equipment_first(self):
        """Insert a new equipment at the beginning of the list"""
        name = self.eq_name.get().strip()
        quantity = self.eq_quantity.get().strip()
        desc = self.eq_description.get().strip()

        if not name or not quantity:
            messagebox.showerror("Error", "Please fill name and quantity for equipment for insertion.")
            return
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be an integer.")
            return
        insert_equipment_at_position(0, name, int(quantity), desc) # Using list insert(0, item) operation
        self.load_equipment_table()
        self.clear_eq_entries()
        messagebox.showinfo("Insert Complete", "Equipment inserted at the beginning of the list.")
        self.log_transaction(f"Inserted equipment at beginning: {name}")

    def view_medicine_slice(self):
        """View the first 3 added medicines in the multidimensional array using slicing"""
        if not medicines:
            messagebox.showinfo("View First 3 Medicines", "No medicines in inventory (multidimensional array is empty)")
            return

        first_three_medicines = get_medicines_slice(0, 3)
        if not first_three_medicines:
            messagebox.showinfo("View First 3 Medicines", "No medicines to display (list is empty or too short).")
            return

        messagebox.showinfo("First 3 Medicines in List", 
            f"First 3 medicines in list:\n" + 
            "\n".join([
                f"ID: {med['id']}, Name: {med['name']}, Packs: {med['packs']}, Items/Pack: {med['items_per_pack']}, Total Qty: {med['total_qty']}, Expiry: {med['expiry']}"
                for med in first_three_medicines
            ])
        )

    def view_equipment_slice(self):
        """View the first 3 added equipment in the multidimensional array using slicing"""
        if not equipment:
            messagebox.showinfo("View First 3 Equipment", "No equipment in inventory (multidimensional array is empty)")
            return

        first_three_equipment = get_equipment_slice(0, 3)
        if not first_three_equipment:
            messagebox.showinfo("View First 3 Equipment", "No equipment to display (list is empty or too short).")
            return

        messagebox.showinfo("First 3 Equipment in List", 
            f"First 3 equipment in list:\n" + 
            "\n".join([
                f"ID: {eq['id']}, Name: {eq['name']}, Stock: {eq['stock']}, Status: {eq['status']}"
                for eq in first_three_equipment
            ])
        )

    def remove_last_medicine(self):
        """Remove the last added medicine from the multidimensional array"""
        if not medicines:
            messagebox.showinfo("Remove Last Medicine", "No medicines to remove (multidimensional array is empty)")
            return

        last_index = len(medicines) - 1
        # Store data before removal
        removed_data = {
            "id": medicines[last_index][MED_ID],
            "name": medicines[last_index][MED_NAME],
            "packs": medicines[last_index][MED_PACKS],
            "items_per_pack": medicines[last_index][MED_ITEMS_PER_PACK],
            "total_qty": medicines[last_index][MED_TOTAL_QTY],
            "expiry": medicines[last_index][MED_EXPIRY]
        }
        
        # Remove entire row from 2D array
        medicines.pop()
        
        self.load_medicines_table()
        messagebox.showinfo("Remove Last Medicine", 
            f"Removed last medicine from multidimensional array:\n"
            f"ID: {removed_data['id']}\n"
            f"Name: {removed_data['name']}\n"
            f"Packs: {removed_data['packs']}\n"
            f"Items per Pack: {removed_data['items_per_pack']}\n"
            f"Total Qty: {removed_data['total_qty']}\n"
            f"Expiry: {removed_data['expiry']}")
        self.log_transaction(f"Removed last medicine: {removed_data['name']}")

    def remove_last_equipment(self):
        """Remove the last added equipment from the multidimensional array"""
        if not equipment:
            messagebox.showinfo("Remove Last Equipment", "No equipment to remove (multidimensional array is empty)")
            return

        last_index = len(equipment) - 1
        # Store data before removal
        removed_data = {
            "id": equipment[last_index][EQ_ID],
            "name": equipment[last_index][EQ_NAME],
            "stock": equipment[last_index][EQ_STOCK],
            "status": equipment[last_index][EQ_STATUS]
        }
        
        # Remove entire row from 2D array
        equipment.pop()
        
        self.load_equipment_table()
        messagebox.showinfo("Remove Last Equipment", 
            f"Removed last equipment from multidimensional array:\n"
            f"ID: {removed_data['id']}\n"
            f"Name: {removed_data['name']}\n"
            f"Stock: {removed_data['stock']}\n"
            f"Status: {removed_data['status']}")
        self.log_transaction(f"Removed last equipment: {removed_data['name']}")

    def remove_medicine_by_id_ui(self):
        """Remove medicine by ID using list operations"""
        id_to_remove = self.med_remove_id_entry.get().strip()
        if not id_to_remove:
            messagebox.showwarning("Warning", "Please enter an ID to remove.")
            return
        try:
            id_int = int(id_to_remove)
            removed_medicine = remove_medicine_by_id(id_int)
            if removed_medicine:
                messagebox.showinfo("Remove Complete", f"Medicine with ID {id_int} removed.")
                self.load_medicines_table()
                self.log_transaction(f"Removed medicine by ID: {id_int}")
            else:
                messagebox.showwarning("Warning", f"No medicine found with ID {id_int}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer ID.")

    def remove_equipment_by_id_ui(self):
        """Remove equipment by ID using list operations"""
        id_to_remove = self.eq_remove_id_entry.get().strip()
        if not id_to_remove:
            messagebox.showwarning("Warning", "Please enter an ID to remove.")
            return
        try:
            id_int = int(id_to_remove)
            removed_equipment = remove_equipment_by_id(id_int)
            if removed_equipment:
                messagebox.showinfo("Remove Complete", f"Equipment with ID {id_int} removed.")
                self.load_equipment_table()
                self.log_transaction(f"Removed equipment by ID: {id_int}")
            else:
                messagebox.showwarning("Warning", f"No equipment found with ID {id_int}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer ID.")

    def update_transaction_log_display(self):
        """Updates the GUI textbox with the current transaction log content"""
        self.log_display.configure(state="normal")
        self.log_display.delete("1.0", "end")
        for entry in self.transaction_log:
            self.log_display.insert("end", entry + "\n")
        self.log_display.configure(state="disabled")

    def update_time(self):
        """Updates the time label in the top right corner"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=f"Time: {current_time}")
        self.after(1000, self.update_time) # Update every second

    def update_medicine_ui(self):
        """Handles the update medicine button click event."""
        if self.selected_medicine_id is None:
            messagebox.showwarning("Warning", "Please select a medicine to update.")
            return

        name = self.med_name.get().strip()
        packs = self.med_packs.get().strip()
        ipp = self.med_items_per_pack.get().strip()
        expiry = self.med_expiry.get().strip()

        if not name or not packs or not ipp or not expiry:
            messagebox.showerror("Error", "Please fill all medicine fields for update.")
            return
        if not packs.isdigit() or not ipp.isdigit():
            messagebox.showerror("Error", "Packs and Items/Pack must be integers.")
            return
        if not self.validate_date(expiry):
            messagebox.showerror("Error", "Expiry date must be in YYYY-MM-DD format.")
            return

        packs_i = int(packs)
        ipp_i = int(ipp)
        total = packs_i * ipp_i

        if update_medicine(self.selected_medicine_id, name, packs_i, ipp_i, total, expiry):
            messagebox.showinfo("Update Complete", f"Medicine ID {self.selected_medicine_id} updated successfully.")
            self.load_medicines_table()
            self.clear_med_entries()
            self.log_transaction(f"Updated medicine: {name} (ID: {self.selected_medicine_id})")
        else:
            messagebox.showerror("Error", f"Failed to update medicine ID {self.selected_medicine_id}.")

    def update_equipment_ui(self):
        """Handles the update equipment button click event."""
        if self.selected_equipment_id is None:
            messagebox.showwarning("Warning", "Please select an equipment to update.")
            return

        name = self.eq_name.get().strip()
        quantity = self.eq_quantity.get().strip()
        desc = self.eq_description.get().strip()

        if not name or not quantity:
            messagebox.showerror("Error", "Please fill name and quantity for equipment for update.")
            return
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be an integer.")
            return
        
        if update_equipment(self.selected_equipment_id, name, int(quantity), desc):
            messagebox.showinfo("Update Complete", f"Equipment ID {self.selected_equipment_id} updated successfully.")
            self.load_equipment_table()
            self.clear_eq_entries()
            self.log_transaction(f"Updated equipment: {name} (ID: {self.selected_equipment_id})")
        else:
            messagebox.showerror("Error", f"Failed to update equipment ID {self.selected_equipment_id}.")

    def on_med_select(self, event):
        """Load selected medicine data into input fields"""
        selected_item = self.med_tree.focus()
        if selected_item:
            values = self.med_tree.item(selected_item, 'values')
            self.selected_medicine_id = int(values[0])  # Convert to int
            self.med_name.delete(0, "end")
            self.med_name.insert(0, values[1])
            self.med_packs.delete(0, "end")
            self.med_packs.insert(0, values[2])
            self.med_items_per_pack.delete(0, "end")
            self.med_items_per_pack.insert(0, values[3])
            # Total qty is read-only, so update its text
            self.med_total_qty.configure(state="normal")
            self.med_total_qty.delete(0, "end")
            self.med_total_qty.insert(0, values[4])
            self.med_total_qty.configure(state="disabled")
            self.med_expiry.delete(0, "end")
            self.med_expiry.insert(0, values[5])
        else:
            self.clear_med_entries()

    def on_eq_select(self, event):
        """Load selected equipment data into input fields"""
        selected_item = self.eq_tree.focus()
        if selected_item:
            values = self.eq_tree.item(selected_item, 'values')
            self.selected_equipment_id = int(values[0])  # Convert to int
            self.eq_name.delete(0, "end")
            self.eq_name.insert(0, values[1])
            self.eq_quantity.delete(0, "end")
            self.eq_quantity.insert(0, values[2])
            self.eq_description.delete(0, "end")
            self.eq_description.insert(0, values[3])
        else:
            self.clear_eq_entries()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    app = ClinicInventoryApp()
    # bind calc total when packs or items per pack change (helpful UX)
    app.med_packs.bind("<KeyRelease>", lambda e: app.calc_med_total())
    app.med_items_per_pack.bind("<KeyRelease>", lambda e: app.calc_med_total())
    app.mainloop()
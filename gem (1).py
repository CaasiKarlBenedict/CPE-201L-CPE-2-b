# clinic_inventory_sqlite.py
import sqlite3
from datetime import datetime
import customtkinter as ctk
from tkinter import ttk, messagebox

# ---------------- APP CONFIG ----------------
ctk.set_appearance_mode("system")  # "dark" / "light" / "system"
ctk.set_default_color_theme("blue")

DB_FILENAME = "clinic_inventory.db"

# ---------------- DATABASE HELPERS ----------------
def init_db():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            packs INTEGER NOT NULL,
            items_per_pack INTEGER NOT NULL,
            total_qty INTEGER NOT NULL,
            expiry TEXT NOT NULL
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

def fetch_medicines():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT id, name, packs, items_per_pack, total_qty, expiry FROM medicines ORDER BY name")
    rows = c.fetchall()
    conn.close()
    return rows

def fetch_equipment():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT id, name, quantity, description FROM equipment ORDER BY name")
    rows = c.fetchall()
    conn.close()
    return rows

def insert_medicine(name, packs, items_per_pack, total_qty, expiry):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("INSERT INTO medicines (name, packs, items_per_pack, total_qty, expiry) VALUES (?, ?, ?, ?, ?)",
              (name, packs, items_per_pack, total_qty, expiry))
    conn.commit()
    conn.close()

def update_medicine(row_id, name, packs, items_per_pack, total_qty, expiry):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("""UPDATE medicines SET name=?, packs=?, items_per_pack=?, total_qty=?, expiry=? WHERE id=?""",
              (name, packs, items_per_pack, total_qty, expiry, row_id))
    conn.commit()
    conn.close()

def delete_medicine(row_id):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("DELETE FROM medicines WHERE id=?", (row_id,))
    conn.commit()
    conn.close()

def insert_equipment(name, quantity, description):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("INSERT INTO equipment (name, quantity, description) VALUES (?, ?, ?)",
              (name, quantity, description))
    conn.commit()
    conn.close()

def update_equipment(row_id, name, quantity, description):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("UPDATE equipment SET name=?, quantity=?, description=? WHERE id=?",
              (name, quantity, description, row_id))
    conn.commit()
    conn.close()

def delete_equipment(row_id):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("DELETE FROM equipment WHERE id=?", (row_id,))
    conn.commit()
    conn.close()

# ---------------- APP CLASS ----------------
class ClinicInventoryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🏥 Clinic Inventory (Medicines & Equipment)")
        self.geometry("1000x600")
        self.minsize(900, 550)

        init_db()

        # Selected item ids
        self.selected_medicine_id = None
        self.selected_equipment_id = None

        self.create_ui()
        self.load_all_tables()

    # ---------- UI ----------
    def create_ui(self):
        # Top area: tabs
        tabview = ctk.CTkTabview(self, width=980, height=580)
        tabview.pack(fill="both", expand=True, padx=10, pady=10)

        tabview.add("Medicines")
        tabview.add("Equipment")

        self.create_medicines_tab(tabview.tab("Medicines"))
        self.create_equipment_tab(tabview.tab("Equipment"))

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

        # Buttons
        add_btn = ctk.CTkButton(frm, text="➕ Add Medicine", command=self.add_medicine)
        add_btn.grid(row=1, column=5, padx=8, pady=5)

        update_btn = ctk.CTkButton(frm, text="✏ Update Selected", fg_color="orange", command=self.update_medicine)
        update_btn.grid(row=1, column=6, padx=8, pady=5)

        del_btn = ctk.CTkButton(frm, text="🗑 Delete Selected", fg_color="red", command=self.delete_medicine)
        del_btn.grid(row=1, column=7, padx=8, pady=5)

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

        # Buttons
        add_btn = ctk.CTkButton(frm, text="➕ Add Equipment", command=self.add_equipment)
        add_btn.grid(row=1, column=3, padx=8, pady=5)

        update_btn = ctk.CTkButton(frm, text="✏ Update Selected", fg_color="orange", command=self.update_equipment)
        update_btn.grid(row=1, column=4, padx=8, pady=5)

        del_btn = ctk.CTkButton(frm, text="🗑 Delete Selected", fg_color="red", command=self.delete_equipment)
        del_btn.grid(row=1, column=5, padx=8, pady=5)

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

        insert_medicine(name, packs_i, ipp_i, total, expiry)
        self.load_medicines_table()
        self.clear_med_entries()

    def on_med_select(self, event):
        sel = self.med_tree.selection()
        if not sel:
            return
        vals = self.med_tree.item(sel[0], "values")
        self.selected_medicine_id = vals[0]
        # fill entries
        self.med_name.delete(0, "end"); self.med_name.insert(0, vals[1])
        self.med_packs.delete(0, "end"); self.med_packs.insert(0, vals[2])
        self.med_items_per_pack.delete(0, "end"); self.med_items_per_pack.insert(0, vals[3])
        # total
        self.med_total_qty.configure(state="normal")
        self.med_total_qty.delete(0, "end"); self.med_total_qty.insert(0, vals[4])
        self.med_total_qty.configure(state="disabled")
        self.med_expiry.delete(0, "end"); self.med_expiry.insert(0, vals[5])

    def update_medicine(self):
        if self.selected_medicine_id is None:
            messagebox.showerror("Error", "Select a medicine to update.")
            return
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

        packs_i = int(packs); ipp_i = int(ipp)
        total = packs_i * ipp_i

        update_medicine(self.selected_medicine_id, name, packs_i, ipp_i, total, expiry)
        self.load_medicines_table()
        self.clear_med_entries()
        self.selected_medicine_id = None

    def delete_medicine(self):
        sel = self.med_tree.selection()
        if not sel:
            messagebox.showerror("Error", "Select a medicine to delete.")
            return
        vals = self.med_tree.item(sel[0], "values")
        rid = vals[0]
        if messagebox.askyesno("Confirm", f"Delete medicine '{vals[1]}'?"):
            delete_medicine(rid)
            self.load_medicines_table()
            self.clear_med_entries()
            self.selected_medicine_id = None

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
        insert_equipment(name, int(quantity), desc)
        self.load_equipment_table()
        self.clear_eq_entries()

    def on_eq_select(self, event):
        sel = self.eq_tree.selection()
        if not sel:
            return
        vals = self.eq_tree.item(sel[0], "values")
        self.selected_equipment_id = vals[0]
        self.eq_name.delete(0, "end"); self.eq_name.insert(0, vals[1])
        self.eq_quantity.delete(0, "end"); self.eq_quantity.insert(0, vals[2])
        self.eq_description.delete(0, "end"); self.eq_description.insert(0, vals[3] if vals[3] else "")

    def update_equipment(self):
        if self.selected_equipment_id is None:
            messagebox.showerror("Error", "Select equipment to update.")
            return
        name = self.eq_name.get().strip()
        quantity = self.eq_quantity.get().strip()
        desc = self.eq_description.get().strip()
        if not name or not quantity:
            messagebox.showerror("Error", "Please fill name and quantity for equipment.")
            return
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be an integer.")
            return
        update_equipment(self.selected_equipment_id, name, int(quantity), desc)
        self.load_equipment_table()
        self.clear_eq_entries()
        self.selected_equipment_id = None

    def delete_equipment(self):
        sel = self.eq_tree.selection()
        if not sel:
            messagebox.showerror("Error", "Select equipment to delete.")
            return
        vals = self.eq_tree.item(sel[0], "values")
        rid = vals[0]
        if messagebox.askyesno("Confirm", f"Delete equipment '{vals[1]}'?"):
            delete_equipment(rid)
            self.load_equipment_table()
            self.clear_eq_entries()
            self.selected_equipment_id = None

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

# ---------------- MAIN ----------------
if __name__ == "__main__":
    app = ClinicInventoryApp()
    # bind calc total when packs or items per pack change (helpful UX)
    app.med_packs.bind("<KeyRelease>", lambda e: app.calc_med_total())
    app.med_items_per_pack.bind("<KeyRelease>", lambda e: app.calc_med_total())
    app.mainloop()

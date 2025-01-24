import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Lead"), "fieldname": "lead", "fieldtype": "Link", "options": "Lead", "width": 200},
        {"label": _("Lead Name"), "fieldname": "lead_name", "fieldtype": "Data", "width": 200},
        {"label": _("Customer"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 200},
        {"label": _("Sales Person"), "fieldname": "custom_sales_person", "fieldtype": "Data", "width": 200},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": _("Custom Conversion Date"), "fieldname": "custom_conversion_date", "fieldtype": "Date", "width": 150},
    ]

def get_data(filters):
    # Prepare filter conditions
    conditions = []
    if filters.get("from_date") :
        start_date = filters.get("from_date")
    else :
        start_date=None
    if filters.get("to_date"):
        end_date = filters.get("to_date")
    else:
        end_date=None
    if filters.get("custom_sales_person"):
       custom_sales_person = filters.get("custom_sales_person")
    else:
       custom_sales_person=None
    
    if custom_sales_person and start_date and end_date:
        # Fetch leads using Frappe ORM with conditions applied
        leads_list = frappe.db.get_list(
            "Lead",
            filters=[
                ["custom_sales_person","=",custom_sales_person],
                ["custom_conversion_date", ">=", start_date],
                ["custom_conversion_date", "<=", end_date]
            ],
            fields=["name as lead", "lead_name", "custom_sales_person", "status", "custom_conversion_date"],
            order_by="custom_conversion_date DESC"
        )
    else:
        leads_list = frappe.db.get_list(
            "Lead",
            fields=["name as lead", "lead_name", "custom_sales_person", "status", "custom_conversion_date"],
            order_by="custom_conversion_date DESC"
        )
    

    # Add Customer data linked by lead_name
    for lead in leads_list:
        # Fetch customer linked to this 
        customer = frappe.db.get_value("Customer", {"lead_name": lead.get("lead")}, "name")
        lead["customer"] = customer
        

    return leads_list

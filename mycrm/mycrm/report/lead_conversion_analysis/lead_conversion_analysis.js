// Copyright (c) 2025, MY CRM and contributors
// For license information, please see license.txt

// report_name.js


frappe.query_reports["Lead Conversion Analysis"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.nowdate(), -1),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.nowdate(),
            "reqd": 1
        },
        {
            "fieldname": "custom_sales_person",
            "label": __("Sales Person"),
            "fieldtype": "Link",
            "options": "User",
            "reqd": 0
        }
    ]
};

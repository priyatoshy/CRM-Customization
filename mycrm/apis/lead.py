import frappe
from .utils import api_response
from datetime import datetime
# from bs4 import BeautifulSoup

#!Paginated Get Customer Details API
@frappe.whitelist(allow_guest=True,methods=["GET"])
def getAllLeads(limit=50,offset=0,custom_sales_person="",status=""):
    #TODO 1: limit offset int format check
    try:
        limit = int(limit)
        offset = int(offset)
    except:
        return api_response(status=False, data=[], message="Please Enter Proper Limit and Offset", status_code=400)
    #!limit and offset upper limit validation
    if limit > 200 or limit < 0 or offset<0:
        return api_response(status=False, data=[], message="Limit exceeded 500", status_code=400)
    lead_filters=None
    if custom_sales_person!="" and status!="":
        
        lead_list = frappe.db.get_list("Lead",
            fields=["*"],
                
                filters={"custom_sales_person":custom_sales_person,"status":status},
                limit=limit,
                start=offset,
                order_by='-modified'
            )
    elif custom_sales_person=="" and status!="":
        lead_list = frappe.db.get_list("Lead",
            fields=["*"],
                
                filters={"status":status},
                limit=limit,
                start=offset,
                order_by='-modified'
            )
    elif custom_sales_person!="" and status=="":
        lead_list = frappe.db.get_list("Lead",
            fields=["*"],
                
                filters={"custom_sales_person":custom_sales_person},
                limit=limit,
                start=offset,
                order_by='-modified'
            )
    
    else:

        lead_list = frappe.db.get_list("Lead",
            fields=["*"],
                
                filters=lead_filters,
                limit=limit,
                start=offset,
                order_by='-modified'
            )
        print("CASE2===================================")
        print(lead_list,"\n\n")
    print("lead list\n",lead_list,"\n\n\n")
    #!=============================================================================================
    if len(lead_list)==0:
        return api_response(status=True, data=[], message="Empty Content", status_code=204)
    else:
        return api_response(status=True, data=lead_list, message="Successfully Fetched All Leads", status_code=200,data_size=len(lead_list))
    
        
                        
   

#!----------------------------------------------------------------------------------------
#!COMMIT

# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os
import csv


#input
Template_file_path = "TEMPLATE" #ไฟล์ เทมเพลตที่เราสร้างไว้
per_page = 4 #จำนวนจ่าหน้าซองพัสดุต่อ 1 หน้ากระดาษ A4 (ณ ที่นี้ใช้เป็น 4 แผ่นต่อ 1 หน้า)
CSV_file_ข้อมูลลูกค้า = "customer.csv" #ไฟล์csv รวมข้อมูลลูกค้า




sample_customers_data = []
with open(CSV_file_ข้อมูลลูกค้า,encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    for i in reader:
        sample_customers_data.append(dict(i))
print(sample_customers_data)

# import json
# with open(Json_file_ข้อมูลลูกค้า,encoding="utf-8") as json_file:
#     sample_customers_data = json.load(json_file)


def create_pdf(customers_data):
    
    currect_file_dir = os.path.dirname(os.path.abspath(__file__))
    saved_path = currect_file_dir
    
    count = 0    
    customers_data = [customers_data[x:x+per_page] for x in range(0, len(customers_data),per_page)]
    for j in customers_data:
        for i in j:
            count += 1
            print ("post address {} has been created".format(count))
        
    if len(customers_data[-1]) <= per_page:
        dummy = {
    "address":"xxx",
    "tel":"xxx"
    },
        for i in range(per_page-len(customers_data[-1])):
            customers_data[-1].append(dummy)
        
    env = Environment(loader=FileSystemLoader(''))
    try:
        template = env.get_template(Template_file_path+".html")
    
    except:
        template = env.get_template(Template_file_path+".htm")
        
    post_html_string = template.render(customers=customers_data).encode('utf-8')
    
    
    Html_file= open(os.path.join(saved_path,"OUTPUT_ADDRESS_LIST.html"),"wb")
    Html_file.write(post_html_string)
    Html_file.close()
    
    print("สร้างไฟล์รวมเสร็จเรียบร้อยแล้ว ที่ Folder :  " + saved_path)
    
    return customers_data

create_pdf(sample_customers_data)

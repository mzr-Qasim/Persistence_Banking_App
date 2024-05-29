
import json
import os

# Adding New Customer Details to Json 




def Add_Records():
    from Program import Customer_Dictionary_Content


    if os.path.getsize("Database.json")>0:
        open_file_read_mode=open("Database.json","r")
        file_content=open_file_read_mode.read()
        parsed_content=json.loads(file_content)
        parsed_content.append(Customer_Dictionary_Content)
        open_file_read_mode.close()
        open_file_writing_mode=open("Database.json","w")
        string_content=json.dumps(parsed_content)
        open_file_writing_mode.write(string_content)
        open_file_writing_mode.close()
    else:
        open_file_writing_mode=open("Database.json","w")
        string_content=json.dumps([Customer_Dictionary_Content])
        open_file_writing_mode.write(string_content)
        open_file_writing_mode.close()
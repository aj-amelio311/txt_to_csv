import os, csv

path = os.getcwd()

count = 0

filenames = []

headers = ["First Name", "Last Name", "Email", "Address", "Apt #", "City", "State", "Zip"]

for i in os.listdir(path):
    if i.endswith(".txt"):
        filenames.append(i)

with open("leadFile.txt", "w") as lead_file:
    for file in filenames:
        with open(file) as combine:
            for line in combine:
                if not line.isspace():
                    lead_file.write(line)
                    count = count + 1
                
row_count = count 

with open("myLeads_" + str(row_count) + ".csv", "w") as my_leads:
    a = csv.writer(my_leads, delimiter=",",lineterminator='\n')
    a.writerow(headers)
    with open("leadFile.txt", "r") as my_file:
        leads = [line.split("|") for line in my_file]
        for each_lead in leads:
            first_name = each_lead[0]
            last_name = each_lead[1]
            email = each_lead[2]
            address = each_lead[3]
            address2 = each_lead[4]
            city = each_lead[5]
            state = each_lead[6]
            zipcode = each_lead[7]
            zipcode_string =  str(zipcode)
            a.writerow([first_name] + [last_name] + [email] + [address] + [address2] + [city] +  [state] + [zipcode_string])

for i in os.listdir(path):
    if i.endswith(".txt"):
        os.unlink(i)
    



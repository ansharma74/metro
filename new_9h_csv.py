import csv
path1='datafiles/A1000_eng_1.csv'
path2='datafiles/top200engg.csv'
path3='datafiles/A1000_eng_1r.csv'
outdata = []
input_file1 = open(path1,'r')
input_file2 = open(path2,'r')
output = open(path3,'w')

reader1 = csv.DictReader(input_file1, delimiter=',',quoting=csv.QUOTE_MINIMAL)
reader2 = csv.DictReader(input_file2, delimiter=',',quoting=csv.QUOTE_MINIMAL)
output.write("S.No.,Name,Main City,State,Rank\n")

added = 0    
    
for row_a in reader1:
    input_file2.seek(0)
    for row_b in reader2:
        if row_a["Name"] in row_b["Name"] and row_a["Main City"] == row_b["Main City"]:
            print(row_b["Name"]+":"+row_b["Rank"]+":"+row_a["Name"])
            print("added rank")
            output.write(row_a["S.No."]+",\""+row_a["Name"]+"\","+row_a["Main City"]+","+row_a["State"]+","+row_b["Rank"]+"\n")
            added = 1
            break
       
    if added == 0:
        output.write("%s,\"%s\",%s,%s\n" % (row_a["S.No."],row_a["Name"],row_a["Main City"],row_a["State"]))
    else:
        added = 0
        
output.close()
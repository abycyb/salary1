from django.shortcuts import render
import openpyxl


def index(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                    row_data.append(str(cell.value))
            excel_data.append(row_data)


        for i in excel_data:
            global a
            if i[0]==("ctc"):
                a=int(i[1])
        my_dict = {"basic salary": [], "HRA": [],"Special Allowance" : [],"Employer PF": [],"Employer ESI":[],"Base Salary":[],"Annual Short-Term Bonus":[],"Other Allowance":[],"Night Shift Allowance":[],"Joining Bonus":[],"Relocation Bonus":[]}
        new_row = list()
        for i in excel_data:
            global basi
            if i[0]==("Basic Salary"):
                a2=int(i[1])
                p2=((a2*100)/a)
                basi=(a*p2)/100
                my_dict["basic salary"].append(basi)
        for i in excel_data:
            global hraa
            if i[0] == ("HRA"):
                a3 = int(i[1])
                p3 = (a3 * 100) / a
                hraa = (a * p3) / 100
                my_dict["HRA"].append(hraa)
        for i in excel_data:
            global spall
            if i[0] == ("Special Allowance"):
                a4 = int(i[1])
                p4 = (a4 * 100) / a
                spall=(a*p4)/100
                my_dict["Special Allowance"].append(spall)
        for i in excel_data:
            global empf
            if i[0] == ("Employer PF"):
                a5 = int(i[1])
                p5 = (a5 * 100) / a
                empf=(a*p5)/100
                my_dict["Employer PF"].append(empf)
        for i in excel_data:
            global emesi
            if i[0] == ("Employer ESI"):
                a6 = int(i[1])
                p6 = 0+(a6 * 100) / a
                emesi=0+(a*p6)/100
                my_dict["Employer ESI"].append(emesi)
        xx = basi + hraa + spall + empf + emesi
        my_dict["Base Salary"].append(xx)
        for i in excel_data:
            if i[0] == ("Annual Short-Term Bonus"):
                a7 = int(i[1])
                p7 = (a7 * 100) / a
                astb=(a*p7)/100
                my_dict["Annual Short-Term Bonus"].append(astb)
        for i in excel_data:
            if i[0] == ("Other Allowance"):
                a8 = int(i[1])
                p8 = 0+(a8 * 100) / a
                otha=0+(a*p8)/100
                my_dict["Other Allowance"].append(otha)
        for i in excel_data:
            if i[0] == ("Night Shift Allowance"):
                a9 = int(i[1])
                p9 = 0+(a9 * 100) / a
                nsa=0+(a*p9)/100
                my_dict["Night Shift Allowance"].append(nsa)
        for i in excel_data:
            if i[0] == ("Joining Bonus"):
                a10 = int(i[1])
                p10 = 0+(a10 * 100) / a
                jb = 0+(a*p10)/100
                my_dict["Joining Bonus"].append(jb)
        for i in excel_data:
            if i[0] == ("Relocation Bonus"):
                a11 = int(i[1])
                p11 = 0+(a11 * 100) / a
                rb = 0+(a*p11)/100
                my_dict["Relocation Bonus"].append(rb)

        new_row.append(my_dict)
        mylist = new_row
        # return render(request, 'index.html', {"excel_data":excel_data})
        return render(request, 'index.html', {"mylist":mylist})




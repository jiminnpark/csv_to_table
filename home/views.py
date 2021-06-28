from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import csv, os

def index(request):
    if request.FILES:
        f=FileSystemStorage()
        file=request.FILES['csvfile']
        if os.path.exists("./media/mediacsv.csv"):
            os.remove("./media/mediacsv.csv")
        filename=f.save("mediacsv.csv",file)
        print(filename)
        head = []
        rowlist = [[]]

        with open("./media/mediacsv.csv","r",encoding="utf-8") as f:
            try:
                reader=csv.reader(f)
                for i,x in enumerate(reader):
                    if i==0:
                        head=x
                    else:
                        rowlist.append(x)
            except:
                return render(request,"error.html")

        return render(request,"table.html",{'head':head,'rowlist':rowlist})
    else:
        return render(request,"index.html")



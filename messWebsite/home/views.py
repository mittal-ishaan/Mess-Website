from django.shortcuts import render
from django.http import HttpResponse
from home.models import About, Update, Carousel, Photos, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact, Rebate, File
from .forms import RebateForm
import pandas as pd

kanaka=900
ajay=900
gauri=500

# Create your views here.
def home(request):
    aboutInfo=About.objects.all()
    update=Update.objects.all()
    caterer=Caterer.objects.all()
    carousel=Carousel.objects.all()
    photos=Photos.objects.all()
    context={'about': aboutInfo, 'updates': update,'caterer':caterer,'carousel':carousel,'photos':photos}
    return render(request,'home.html',context)



def rules(request):
    rules=Rule.objects.all()
    shortRebates=ShortRebate.objects.all()
    LongRebates=LongRebate.objects.all()
    form=Form.objects.all()
    caterer=Caterer.objects.all()
    params={'rule':rules,'shortRebate':shortRebates,'longRebate': LongRebates,'form':form,'caterer':caterer}
   
    return render(request,'rules.html',params)

def kanaka(request):
    caterer=Caterer.objects.all()
    context={'caterer':caterer}
    return render(request,'caterer2.html',context)

def ajay(request):
    caterer=Caterer.objects.all()
    context={'caterer':caterer}
    return render(request,'caterer1.html',context)

def links(request):
    """ allLinks=link.objects.all()
    context={'allLinks': allLinks} """
    caterer=Caterer.objects.all()
    form=Form.objects.all()
    context={'caterer':caterer,'form':form}
    return render(request,'links.html',context)

def cafeteria(request):
    caterer=Caterer.objects.all()
    cafeteria=Cafeteria.objects.all()
    context={'caterer':caterer,'cafeteria':cafeteria}
    return render(request,'cafeteria.html',context)

def contact(request):
    """ allContacts=contact.objects.all()
    context={'allContacts': allContacts} """
    caterer=Caterer.objects.all()
    contact=Contact.objects.all()
    context={'caterer':caterer,'contact':contact}
    return render(request,'contact.html',context)

def rebateForm(request):
    if request.method == 'POST':
        allocation_id = request.POST.get('allocation_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        diff = abs((end_date-start_date).days)
        diff2 = (start_date-datetime.date.today()).days
        if((diff)<=7 and diff2>=2):
            approved = True
        else:
            approved = False
        approved=False
        form=Rebate(allocation_id = allocation_id,start_date=start_date,end_date=end_date,approved=approved)
        form.save()
    return render(request, "rebateForm.html")


def create_db(file_path):
    df = pd.read_csv(file_path,delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for i in list_of_csv:
        global kanaka, gauri, ajay
        student_id = i[2]
        caterer_name = i[4]
        first_pref = i[6]
        second_pref = i[7]
        third_pref = i[8]
        for pref in {first_pref,second_pref,third_pref}:
            if(pref == "kanaka" and kanaka>0):
                student_id="K"+str(kanaka)
                caterer_name = "Kanaka"
                kanaka-=1
                break 
            elif(pref == "ajay" and ajay>0):
                student_id="A"+str(ajay)
                caterer_name = "Ajay"
                ajay-=1
                break
            elif(pref == "gauri" and gauri>0):
                student_id="G"+str(gauri)
                caterer_name = "Gauri"
                gauri-=1
                break
        Allocation.objects.create(
            roll_no = i[1],
            student_id = student_id,
            month = i[3],
            caterer_name = caterer_name,
            high_tea = i[5],
            first_pref = i[6],
            second_pref = i[7],
            third_pref = i[8]
        )


def allocation(request):
    if request.method == 'POST':
        file = request.FILES['file']
        obj = File.objects.create(file = file)
        create_db(obj.file)
    return render(request,"allocation.html")

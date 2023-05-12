from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import About, Update, Carousel, Photos, Rule, Penalty, ShortRebate, LongRebate, Caterer, Form, Cafeteria, Contact, Rebate, Allocation, Student, RebateAutumnSem, RebateSpringSem
import pandas as pd
import datetime
from django.views.generic import TemplateView
import io
from django.core.exceptions import ObjectDoesNotExist
from django.utils.dateparse import parse_date
from django.core.exceptions import MultipleObjectsReturned

# Create your views here.


def home(request):
    """
    Display the Home Page :model:`home.models.home`.

    **Template:**

    :template:`home/home.html`

    """
    aboutInfo = About.objects.all()
    update = Update.objects.all()
    caterer = Caterer.objects.all()
    carousel = Carousel.objects.all()
    photos = Photos.objects.all()
    context = {'about': aboutInfo, 'updates': update,
               'caterer': caterer, 'carousel': carousel, 'photos': photos}
    return render(request, 'home.html', context)


def rules(request):
    """
    Display the Rules Page :model:`home.models.rules`.

    **Template:**

    :template:`home/rules.html`

    """
    rules = Rule.objects.all()
    shortRebates = ShortRebate.objects.all()
    LongRebates = LongRebate.objects.all()
    form = Form.objects.all()
    caterer = Caterer.objects.all()
    params = {'rule': rules, 'shortRebate': shortRebates,
              'longRebate': LongRebates, 'form': form, 'caterer': caterer}

    return render(request, 'rules.html', params)


def caterer(request, name):
    """
    Display the Caterer Page :model:`home.models.caterer`.

    **Template:**

    :template:`home/caterer.html`

    """
    caterer = Caterer.objects.get(name=name)
    context = {'caterer': caterer}
    return render(request, 'caterer.html', context)


def links(request):
    """
    Display the Forms Page :model:`home.models.links`.

    **Template:**

    :template:`home/links.html`

    """
    form = Form.objects.all()
    context = {'form': form}
    return render(request, 'links.html', context)


def cafeteria(request):
    """
    Display the Cafeteria Page :model:`home.models.cafeteria`.

    **Template:**

    :template:`home/cafeteria.html`

    """
    cafeteria = Cafeteria.objects.all()
    context = {'cafeteria': cafeteria}
    return render(request, 'cafeteria.html', context)


def contact(request):
    """
    Display the Contact Page :model:`home.models.contacts`.

    **Template:**

    :template:`home/contact.html`

    """
    contact = Contact.objects.all()
    context = {'contact': contact}
    return render(request, 'contact.html', context)

# def days(s,list):
#     total_days = 0
#     try:
#         count = Rebate.objects.filter(allocation_id = s).count()
#         for i in range(count):
#             rebate = Rebate.objects.filter(allocation_id = s)[i]
#             start_date = rebate.start_date
#             end_date = rebate.end_date
#             list.append([(start_date),(end_date)])
#             total_days += ((end_date-start_date).days)+1
#         return total_days
#     except Exception as e:
#         print(e)
#         return total_days


def count(start, end, sum):
    '''Counts the number of days of rebate applied'''
    sum += ((end-start).days)+1
    return sum


def is_present_autumn(s):
    '''
    Checks if student is registered in the rebate bills of autumn semester, 
    if not the function registers it with that email ID
    '''
    try:
        student = RebateAutumnSem.objects.get(email=str(s.email))
    except:
        print(Exception)
        student = RebateAutumnSem(
            email=str(s.email)
        )
        student.save()
    return student


def is_present_spring(s):
    '''
    Checks if student is registered in the rebate bills of spring semester, 
    if not the function registers it with that email ID
    '''
    try:
        student = RebateSpringSem.objects.get(email=str(s.email))
    except:
        print(Exception)
        print(2)
        student = RebateSpringSem(
            email=str(s.email)
        )
        student.save()
    return student


def check(a, s, start, end, month):
    '''
    Checks what month rebate is being applied, 
    if the rebate doesnot exceeds 8 days for that month approves the rebate and 
    adds the rebate to rebate bills
    '''
    match month:
        case "January":
            student = is_present_spring(s)
            student.january = count(start, end, student.january)
            student.highTeaJanuary = a.high_tea
            if (student.january <= 8):
                student.save(update_fields=["january", "highTeaJanuary"])
                return 1
            if (start.month == 1 and end.month == 1):
                return 2
            else:
                return 0
        case "Feburary":
            student = is_present_spring(s)
            student.feburary = count(start, end, student.feburary)
            student.highTeaFeburary = a.high_tea
            if (student.feburary <= 8):
                student.save(update_fields=["feburary", "highTeaFeburary"])
                return 1
            elif (start.month != 2 and end.month != 2):
                return 2
            else:
                return 0
        case "March":
            student = is_present_spring(s)
            student.march = count(start, end, student.march)
            student.highTeaMarch = a.high_tea
            if (student.march <= 8):
                student.save(update_fields=["march", "highTeaMarch"])
                return 1
            elif (start.month != 3 and end.month != 3):
                return 2
            else:
                return 0
        case "April":
            student = is_present_spring(s)
            student.april = count(start, end, student.april)
            student.highTeaApril = a.high_tea
            if (student.april <= 8):
                student.save(update_fields=["april", "highTeaApril"])
                return True
            elif (start.month != 4 and end.month != 4):
                return 2
            else:
                return False
        case "May":
            student = is_present_spring(s)
            student.may = count(start, end, student.may)
            student.highTeaMay = a.high_tea
            if (student.may <= 8):
                student.save(update_fields=["may", "highTeaMay"])
                return 1
            elif (start.month != 5 and end.month != 5):
                return 2
            else:
                return 0
        case "June":
            student = is_present_spring(s)
            student.june = count(start, end, student.june)
            student.highTeaJune = a.high_tea
            if (student.june <= 8):
                student.save(update_fields=["june", "highTeaJune"])
                return 1
            elif (start.month != 6 and end.month != 6):
                return 2
            else:
                return 0
        case "July":
            student = is_present_autumn(s)
            student.july = count(start, end, student.july)
            student.highTeaJuly = a.high_tea
            if (student.july <= 8):
                student.save(update_fields=["july", "highTeaJuly"])
                return 1
            elif (start.month != 7 and end.month != 7):
                return 2
            else:
                return 0
        case "August":
            student = is_present_autumn(s)
            student.august = count(start, end, student.august)
            student.highTeaAugust == a.high_tea
            if (student.august <= 8):
                student.save(update_fields=["august", "highTeaAugust"])
                return 1
            elif (start.month != 8 and end.month != 8):
                return 2
            else:
                return 0
        case "September":
            student = is_present_autumn(s)
            student.september = count(start, end, student.september)
            student.highTeaSeptember = a.high_tea
            if (student.september <= 8):
                student.save(update_fields=["september", "highTeaSeptember"])
                return 1
            elif (start.month != 9 and end.month != 9):
                return 2
            else:
                return 0
        case "October":
            student = is_present_autumn(s)
            student.october = count(start, end, student.october)
            student.highTeaOctober = a.high_tea
            if (student.october <= 8):
                student.save(update_fields=["october", "highTeaOctober"])
                return 1
            elif (start.month != 10 and end.month != 10):
                return 2
            else:
                return 0
        case "November":
            student = is_present_autumn(s)
            student.november = count(start, end, student.november)
            student.highTeaNovember = a.high_tea
            if (student.november <= 8):
                student.save(update_fields=["november", "highTeaNovember"])
                return 1
            elif (start.month != 11 and end.month != 11):
                return 2
            else:
                return 0
        case "December":
            student = is_present_autumn(s)
            student.december = count(start, end, student.december)
            student.highTeaDecember = a.high_tea
            if (student.december <= 8):
                student.save(update_fields=["december", "highTeaDecember"])
                return 1
            elif (start.month != 12 and end.month != 12):
                return 2
            else:
                return 0
        # case default:
        #     return "something"


def rebate(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.
    
    Gets the data from the rebate form checks for the validity of the rebate filled, 
    adds the rebte to the rebate model and rebate bills of that semester.
    This form can only be accessed by the Institute community

    **Template:**

    :template:`rebateForm.html`
    """
    text = ""
    list = []
    try:
        allocation_id = Allocation.objects.get(
            roll_no__email=str(request.user.email))
        key = str(allocation_id.student_id)
    except Allocation.DoesNotExist:
        key = "Signed in account does not does not have any allocation ID"
    except Allocation.MultipleObjectsReturned:
        allocation_id = Allocation.objects.filter(
            roll_no__email=str(request.user.email)).last()
        key = str(allocation_id.student_id)
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            start_date = parse_date(request.POST['start_date'])
            end_date = parse_date(request.POST['end_date'])
            if (start_date.month == end_date.month):
                diff = ((end_date-start_date).days)+1
                diff2 = (start_date-datetime.date.today()).days
                try:
                    Allocation.objects.filter(
                        student_id=request.POST['allocation_id']).last()
                    try:
                        a = Allocation.objects.get(roll_no__email=str(
                            request.user.email), student_id=request.POST['allocation_id'])
                        s = Student.objects.filter(
                            email=str(request.user.email)).first()
                        month = a.month
                        print(month)
                        # total_days = days(a,list)+diff
                        # print(total_days)
                        # print(list)
                        ch = check(a, s, start_date, end_date, month)
                        if (ch == 2):
                            text = "Please fill the rebate of this month only"
                        elif (ch == 0):
                            text = "You can only apply for max 8 days in a month"
                        else:
                            print(ch)
                            if ((diff) <= 7 and diff >= 2 and diff2 >= 2):
                                r = Rebate(
                                    email=request.user.email,
                                    allocation_id=a,
                                    start_date=request.POST['start_date'],
                                    end_date=request.POST['end_date'],
                                    approved=False
                                )
                                r.save()
                                text = "You have successfully submitted the form. Thank you"
                            else:
                                text = "Your rebate application has been rejected due to non-compliance of the short term rebate rules"
                    except Allocation.DoesNotExist:
                        text = "Email ID does not match with the allocation ID"
                except Allocation.DoesNotExist:
                    text = " The asked allocation ID does not exist. Please enter the correct ID."
            else:
                text = "Please enter the rebate dates within this month only"
        except Exception as e:
            print(e)
            text = "Invalid Dates filled"
    context = {'text': text, "key": key, "list": list}
    return render(request, "rebateForm.html", context)


def allocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/allocation.html`

    Gets the data from the allocation csv, 
    parses each row and allocates each student an allocation ID and caterer for that month.
    Which can be then exported in the admin page.
    CSV should be imported from /allocation/ url only
    Allocation data should only be filled 2 days prior to the next month
    This form can only be accessed by the Institute's admin
    """
    messages = ""
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_staff:
        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )
        print(csv_data.head())

        for record in csv_data.to_dict(orient="records"):
            try:
                first_pref = str(record["first_pref"]).capitalize()
                second_pref = str(record["second_pref"]).capitalize()
                third_pref = str(record["third_pref"]).capitalize()
                high_tea = record["high_tea"]
                r = Student.objects.get(roll_no=record["roll_no"])
                print(r)
                print("hi1")
                for pref in [first_pref, second_pref, third_pref]:
                    kanaka = Caterer.objects.get(name="Kanaka")
                    ajay = Caterer.objects.get(name="Ajay")
                    gauri = Caterer.objects.get(name="Gauri")
                    if (pref == kanaka.name and kanaka.student_limit > 0):
                        student_id = str(kanaka.name[0])
                        if (high_tea == True):
                            student_id += "H"
                        student_id += str(kanaka.student_limit)
                        caterer_name = kanaka.name
                        kanaka.student_limit -= 1
                        kanaka.save(update_fields=["student_limit"])
                        break
                    elif (pref == ajay.name and ajay.student_limit > 0):
                        student_id = str(ajay.name[0])
                        if (high_tea == True):
                            student_id += "H"
                        student_id += str(ajay.student_limit)
                        caterer_name = ajay.name
                        ajay.student_limit -= 1
                        ajay.save(update_fields=["student_limit"])
                        break
                    elif (pref == gauri.name and gauri.student_limit > 0):
                        student_id = str(gauri.name[0])
                        if (high_tea == True):
                            student_id += "H"
                        student_id += str(gauri.student_limit)
                        caterer_name = gauri.name
                        gauri.student_limit -= 1
                        gauri.save(update_fields=["student_limit"])
                        break
                a = Allocation(
                    roll_no=r,
                    student_id=student_id,
                    month=record["month"],
                    caterer_name=caterer_name,
                    high_tea=high_tea,
                    first_pref=first_pref,
                    second_pref=second_pref,
                    third_pref=third_pref
                )
                a.save()
            except Exception as e:
                print(e)
        messages = "Form submitted. Please check the admin page."
    context = {'messages': messages}
    return render(request, "allocation.html", context)


def addAllocation(request):
    """
    Display the Rebate Form Page :model:`home.models.students`.

    **Template:**

    :template:`home/addAllocation.html`

    Gets the data from the allocation form , and 
    allocates an allocation ID and caterer for that month corresponding to the student with submitted email ID.
    This is for students who did not filled the allocation form
    Allocation data should only be filled 2 days prior to the next month
    This form can only be accessed by the Institute's admin
    """
    text = ""
    all_caterers = Caterer.objects.all()
    available_caterer = []
    for caterer in all_caterers:
        current = Caterer.objects.get(name=caterer.name)
        if (current.student_limit > 0):
            available_caterer.append(current.name)
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_staff:
        try:
            high_tea = "on" in request.POST.getlist("high_tea")
            student = Student.objects.filter(email=request.POST["email"])
            if student.exists():
                student = student.first()
                caterer = Caterer.objects.get(name=request.POST["caterer"])
                student_id = str(caterer.name[0])
                # print(high_tea)
                if (high_tea == True):
                    student_id += "H"
                student_id += str(caterer.student_limit)
                caterer_name = caterer.name
                caterer.student_limit -= 1
                caterer.save(update_fields=["student_limit"])
                month = str(request.POST["month"]).capitalize()
                a = Allocation(
                    roll_no=student,
                    student_id=student_id,
                    month=month,
                    caterer_name=caterer_name,
                    high_tea=high_tea,
                    first_pref=caterer_name,
                    second_pref=caterer_name,
                    third_pref=caterer_name
                )
                a.save()
                text = "Allocation successful with allocation id {}".format(
                    student_id)
            else:
                print(1)
                text = "Email is not present in the Database"
        except Exception as e:
            print(e)
            print(12121)
    context = {'text': text, 'caterers': available_caterer}
    return render(request, "addAllocation.html", context)
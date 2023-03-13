from django.shortcuts import render,redirect
from .models import Hodregister,teacherregister,studentregister,leave,exam,mark
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login




# Create your views here.

from django.contrib.auth.models import User
from .models import Hodregister,teacherregister,studentregister,leave,exam


def index(request):
    return render(request,'public_user_home.html')

    
def indexlogin(request):
    return render(request,'login.html')  


def indexadmin(request):
    return render(request,'admin_home.html') 

def indexhodreg(request):
    return render(request,'hodregister.html')

def indexhodhom(request):
    return render(request,'hod.html')

def indexteacherreg(request):
    return render(request,'teacher_register.html')

def indexteacherhom(request):
    return render(request,'teacher.html') 

def indexstudentsreg(request):
    return render(request,'student_register.html')

def indexstudenthom(request):
    return render(request,'students.html')  

def adminapprovehod(request):
    return render(request,'adminviewapprovedhod.html')    




def teacheraddleave(request):
    return render(request,'teacheraddleave.html')    

def hodapproveteacherleave(request):
    return render(request,'hodapproveteacherleaves.html')    




def adminapprovedstudents(request):
    return render(request,'adminviewapprovedstudent.html')





def teacherapprovestudentleave(request):
    return render(request,'studentaddleave.html')    



def teacheraddstudentexam(request):
    return render(request,'teacheraddstudentexam.html')   


def hodapproveviewexam(request):
    return render(request,'hodviewexamapprovel.html')

def studentviewexamlist(request):
    return render(request,'studentviewexamlist.html')    


#admin




def adminviewteacher(request):
    teacherlist=teacherregister.objects.all()
    return render(request,"adminviewteacher.html",{'teacherlist':teacherlist})

def adminviewstudent(request):
    studentlist=studentregister.objects.all()
    return render(request,"adminviewstudent.html",{'studentlist':studentlist})

def admindeletehod(request,hodid):
    data=Hodregister.objects.get(id=hodid)
    data.delete()
    return redirect('viewhod')    

def admindeleteteacher(request,teacherid):
    teacherlist=teacherregister.objects.get(id=teacherid)
    teacherlist.delete()
    return redirect('viewteacher')

def admindeletestudent(request,studentid):
    studentlis=studentregister.objects.get(id=studentid)
    studentlis.delete()
    return redirect('viewstudent')    



def adminviewapprovehod(request,hodid):
    data = Hodregister.objects.get(id=hodid)
    data.status = 1
    data.save()
    return redirect('adminapprovehod')

def adminapprovedhod(request):
    data=Hodregister.objects.all()
    return render(request,'adminviewapprovedhod.html',{'data':data})


def adminapproveteacher(request,teacherid):
    teacherlist = teacherregister.objects.get(id=teacherid)
    teacherlist.status = 1
    teacherlist.save()
    return redirect('adminapprovedteacher')


def adminapprovedteacher(request):
    teacherlist=teacherregister.objects.all()
    return render(request,'adminviewapprovedteacher.html',{'teacherlist':teacherlist})


def adminapprovestudent(request,studentid):
    studentlist=studentregister.objects.get(id=studentid)
    studentlist.status = 1
    studentlist.save()
    return redirect('adminapprovedstudent') 

def adminapprovedstudent(request):
    studentlist=studentregister.objects.all()
    return render(request,'adminviewapprovedstudent.html',{'studentlist':studentlist})      


def adminviewleave(request):
    return render(request,'adminapproveleave.html')   


def adminpendleave(request):
    leavelist=leave.objects.all()
    print("hi",leavelist)
    return render(request,'adminapproveleave.html',{'leavelist':leavelist})

def adminleaveapproved(request):
    leavelist=leave.objects.all()
    return render(request,'adminleave.html',{'leavelist':leavelist})    


def adminapproveleavehod(request,leaveid):
    leavelist=leave.objects.get(id=leaveid)
    leavelist.status=1
    leavelist.save()
    return redirect('adminapprovedhodleaveshow')


def adminapprovedhodleaveshow(request):
    return render(request,'adminleave.html')    


def adminapproveleave(request,leaveid):
    leavelist=leave.objects.get(id=leaveid)
    leavelist.status=1
    leavelist.save()
    return redirect('adminleaveapproved')

def adminrejectleave(request,leaveid):
    leavelist=leave.objects.get(id=leaveid)
    leavelist.delete()
    return redirect('adminviewleave')   

def admindeleteleave(request,leaveid):
    leavelist=leave.objects.get(id=leaveid)
    leavelist.delete()
    return redirect('adminleaveapproved') 


#hod


def hoddeleteteaher(request,teacherid):
    teacherlist=teacherregister.objects.get(id=teacherid)
    teacherlist.delete()
    return redirect('viewteacher')

def adminreg(request):
    data=Hodregister.objects.all()
    return render(request,"adminviewhod.html",{'data':data})



def saveinfo(request):
    data=Hodregister.objects.all()
    if request.method == "POST":
        fullname=request.POST.get('fullname')
        hod_img=request.FILES['hod_img']
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        username=request.POST.get('username')
        department=request.POST.get('department')
        phoneno=request.POST.get('phoneno')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        address=request.POST.get('address')
        status='0'
        role='hod'

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('hodreg')


            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Aready Exists")
                return redirect('hodreg')

            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()



                data1=Hodregister(user=user,fullname=fullname,hod_img=hod_img,email=email,department=department,phoneno=phoneno,gender=gender,qualification=qualification,address=address,status=status,role=role)
                data1.save()


                print("HOD Created")
        else:
            messages.info(request,"Password is not matching")
            return redirect('hodreg')    


        return redirect('adminhome') 
    else:
        return render(request,'admin_home.html')


def hodaddleave(request):
    return render(request,'hodaddleave.html')


img=""
name=""
dept=""
def hodaddleavefun(request):
    global img
    global name
    global dept
    if request.user:
        user = request.user
        if request.method=="POST":
            reason=request.POST.get("purpose")
            date=request.POST.get("date")
            role=request.POST.get("role")
            status='0'
            leavelist=leave(user=user,purpose=reason,date=date,role=role,status=status)
            leavelist.save()

    return render(request,'hod.html')


def adminviewhodleave(request):
    a=Hodregister.objects.filter(role="hod")
    for i in a:
        role=i['role']
    b=leave.objects.filter(role=role)
    return render(request,'adminapproveleave.html',{'b':b})


# img=""  
# name=""
# dept=""     
# def hodaddleavefun(request):
#     global img
#     global name
#     global dept
#     leavelist=leave.objects.all()
#     if request.user:
#         user=request.user
#         print(user)

#         if request.method=='POST':
#             purpose=request.POST.get('purpose')
#             date=request.POST.get('date')
#             status="0"
#             role='hod'
#             data=Hodregister.objects.filter(user=user).values()
#             print("Hooo",data)
#             for i in data:
#                 img=i['hod_img']
#                 name=i['fullname']
#                 dept=i['department']


#             leavelist1=leave(user=user,purpose=purpose,date=date,status=status,role=role)
#             leavelist1.save()
#     return render(request,'hod.html')            

def hodapproveteacherleave(request):
    leavelist1=leave.objects.all()
    print("hi",leavelist1)
    return render(request,'hodapproveteacherleaves.html',{'leavelist1':leavelist1})



def hodleacherleave(request):
    leavelist1=leave.objects.all()

    return render(request,'hodteacherleave.html',{'leavelist1':leavelist1})    



#teacher

def teacherdeletestudent(request,studentid):
    studentlist=studentregister.objects.get(id=studentid)
    studentlist.delete()
    return redirect('viewstudent')

def teacherview(request):
    teacherlist=teacherregister.objects.all()
    return render(request,'hodviewteacher.html',{'teacherlist':teacherlist})

def teacherinfo(request):
    teacherlist=teacherregister.objects.all()
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        username=request.POST.get('username')
        department=request.POST.get('department')
        phoneno=request.POST.get('phoneno')
        gender=request.POST.get('gender')
        qualification=request.POST.get('qualification')
        address=request.POST.get('address')
        status='0'
        role='teacher'

        if password1==password2:
            if User.objects.filter(username=username).exists(): 
                messages.info(request,"Username Taken")
                return redirect('teacherreg')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Aready Exists")
                return redirect('teacherreg')  
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()

                teacherlist1=teacherregister(user=user,fullname=fullname,email=email,department=department,phoneno=phoneno,gender=gender,qualification=qualification,address=address,status=status,role=role)
                teacherlist1.save()    
        
                print("Teacher Created")
        else:
            messages.info(request,"Password is not matching")
            return redirect('teacherreg')


        return redirect('hodhom') 
    else:
        return render(request,'hod.html')


       
img=""
name=""
dept=""
def teacheraddleavefun(request):
    global img
    global name
    global dept
    if request.user:
        user = request.user
        if request.method=="POST":
            reason=request.POST.get("purpose")
            date=request.POST.get("date")
            # department=request.POST.get("department")
            role=request.POST.get("role")
            status='0'
            leavelist1=leave(user=user,purpose=reason,date=date,role=role,status=status)
            leavelist1.save()

    return render(request,'teacher.html')


def hodviewteacherleave(request):
    a=teacherregister.objects.filter(role="teacher")
    for i in a:
        role=i['role']
    b=leave.objects.filter(role=role)
    return render(request,'hodapproveteacherleaves.html',{'b':b})



def hodteacherleaveone(request,leaveid):
    leavelist=leave.objects.get(id=leaveid)
    leavelist.status=1
    leavelist.save()
    return render('hodteacherleavegot')

# def hodapproveleavehod(request,leaveid):
#     leavelist=leave.objects.get(id=leaveid)
#     leavelist.status=1
#     leavelist.save()
#     return redirect('adminapprovedhodleaveshow')

def hodteacherleavegot(request):
    return render(request,'hodteacherleave.html')


#student

def studentview(request):
    studentlist=studentregister.objects.all()
    return render(request,'teacherviewstudent.html',{'studentlist':studentlist})


def studentreg(request):
    studentlist=studentregister.objects.all()
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        username=request.POST.get('username')
        course=request.POST.get('course')
        year=request.POST.get('year')
        phoneno=request.POST.get('phoneno')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        status='0'
        role='student'


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('studentreg')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Aready Exists")
                return redirect('studentreg')

            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()


                studentlist1=studentregister(user=user,fullname=fullname,email=email,course=course,year=year,phoneno=phoneno,gender=gender,address=address,status=status,role=role)
                studentlist1.save()


                print("Student Created")
        else:
            messages.info(request,"Password is not matching")
            return redirect('studentreg')


        return redirect('teacherhom') 
    else:
        return render(request,'teaccher.html')  

def hodaddleave(request):
    return render(request,'hodaddleave.html')


img=""
name=""
dept=""
def studentaddleavefun(request):
    global img
    global name
    global dept
    if request.user:
        user = request.user
        if request.method=="POST":
            reason=request.POST.get("purpose")
            date=request.POST.get("date")
            role=request.POST.get("role")
            status='0'
            leavelist=leave(user=user,purpose=reason,date=date,role=role,status=status)
            leavelist.save()

    return render(request,'student.html')


def adminviewhodleave(request):
    a=studentregister.objects.filter(role="student")
    for i in a:
        role=i['role']
    b=leave.objects.filter(role=role)
    return render(request,'teacherapprovestudentleave.html',{'b':b})




#exam

def teacheraddstudentexam(request):
    if request.method =="POST":
        user=request.User
        date=request.POST["date"]
        status='0'
        role=''
        department=request.POST["department"]
        examlist=exam(user=user,date=date,status=status,role=role,department=department)
        examlist.save()
        data=exam.objects.all()
        return render (request,'teacheraddstudentexam.html',{'data':data})
    else:
        return render (request,'teacheraddstudentexam.html')        

# def teacherexamdetail(request):
#     examlist=exam.objects.all()
#     return render(request,'hodviewexamapprovel.html',{'examlist':examlist}) 

def hodapproveviewexam(request):
    if request.User:
        user=request.User
        print(user)
        dept=''
        data=Hodregister.objects.filter(user=User).values()
        for i in data:
            dept=i["department"]
            print(dept)
        datas=exam.objects.filter(department=dept)
        print(datas)
        return render (request,'hodviewexamapprovel.html',{'data':datas})        




def hodonapprovelview(request):
    if request.user:
        user=request.user
        department=""
        ex=Hodregister.objects.filter(user=user).values()
        for i in ex:
            department=i["department"]
        exa=exam.objects.filter(department=department)
        return render(request,'hodviewexamapprovel.html',{'ex':exa})    














#mark

def markupload(request):
    return render(request,"mark.html") 

def publish(request):
    if request.User:
        User=request.User
        print("bvjkdsf",User)
        if request.method =="POST":
            department=request.POST["department"]
            subject=request.POST["subject"]
            total=request.POST["total"]
            mymark=request.POST["mymark"]
            status='0'
            result=mark(User=User,department=department,subject=subject,total=total,mymark=mymark,status=status)
            result.save()
            print("jdbjnb",mymark)
            return render (request,'mark.html')
        else:
             return render(request,'mark.html')

def publishview(request):
    if request.user:
        user=request.user 
        dept=''
        sub=''
        data=studentregister.objects.filter(user=user).values()
        for i in data:
            dept=i["Sdepartment"]
            sub=i["Ssubject"]
        dataas=mark.objects.filter(Q(department=dept) & Q(subject=sub))
        return render (request,'mark2.html',{'datas':dataas})


#login

stat=''
rol=''
def login(request):
    global stat
    global rol
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)

        user= authenticate(username=username,password=password)
        print("Hi",user)
       
        log = User.objects.filter(username = username).values()
        print("userModelData==>",log)
        for i in log:
            u_name = i['username']
            print(u_name)
            id=i['id']

            studentlog=studentregister.objects.filter(user_id=id).values()
            print("studentdata==>",studentlog)
            for i in studentlog:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)

            teacherlog=teacherregister.objects.filter(user_id=id).values()
            print("teacherdata==>",teacherlog)
            for i in teacherlog:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)


            hodlog=Hodregister.objects.filter(user_id=id).values()
            print("hoddata==>",hodlog)
            for i in hodlog:
                stat=i['status']
                rol=i['role']
                print("status=",stat)
                print("role=",rol)    

            if user is not None and rol =='student' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('studenthom')

            elif user is not None and rol =='teacher' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('teacherhom')

            elif user is not None and rol =='hod' and username==u_name and stat=='1':
                auth_login(request,user)
                return redirect('hodhom')
                
            elif username=="sanalmohmd" and password=='9744861757.ju':
                auth_login(request,user)
                return redirect('adminhome')    

            else:pass

        else:
            messages.info(request,'Invalid Credentials')  
            return redirect('loginpage')

    else:
        return render(request,'login.html')        





            
        
           

       




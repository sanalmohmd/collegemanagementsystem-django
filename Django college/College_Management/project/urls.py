from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('admin_home/',views.indexadmin,name='adminhome'),
    path('hodregister',views.indexhodreg,name='hodreg'),
    path('hod',views.indexhodhom,name='hodhom'),
    path('teacher_register',views.indexteacherreg,name='teacherreg'),
    path('teacher',views.indexteacherhom,name='teacherhom'),
    path('student_register',views.indexstudentsreg,name='studentreg'),
    path('indexstudenthom',views.indexstudenthom,name='indexstudenthom'),
    path('login',views.indexlogin,name='loginpage'),

    path('hodregister',views.saveinfo,name='addhod'),
    path('teacherregister',views.teacherinfo,name='addteacher'),
    path('studentregister',views.studentreg,name='addstudent'),

    path('adminhod',views.adminreg,name='viewhod'),
    path('hodteacher',views.teacherview,name='viewteacher'),
    path('teacherstudent',views.studentview,name='viewstudent'),

    path('adminviewteacher',views.adminviewteacher,name='adminviewteacher'),
    path('adminviewstudent',views.adminviewstudent,name='adminviewstudent'),



    path('admindeletehod/<int:hodid>/',views.admindeletehod,name='admindeletehod'),
    path('hoddeleteteacher/<int:teacherid>/',views.hoddeleteteaher,name='hoddeleteteacher'),
    path('teacherdeletestudent/<int:studentid>/',views.teacherdeletestudent,name='teacherdeletestudent'),

    path('admindeleteteacher/<int:teacherid>/',views.admindeleteteacher,name='admindeleteteacher'),
    path('admindeletestudent/<int:studentid>/',views.admindeletestudent,name='admindeletestudent'),

    path('adminapprovedhod/<int:hodid>/',views.adminviewapprovehod,name='adminapprovedhod'),
    path('adminapprovehod',views.adminapprovedhod,name='adminapprovehod'),

    path('adminapprovedteacher',views.adminapprovedteacher,name='adminapprovedteacher'),

    path('adminapproveteacher/<int:teacherid>/',views.adminapproveteacher,name='adminapproveteacher'),

    path('adminapprovedstudent',views.adminapprovedstudent,name='adminapprovedstudent'),
    path('adminapprovestudent/<int:studentid>/',views.adminapprovestudent,name='adminapprovestudent'),

    path('adminapprovedstudents',views.adminapprovedstudents,name='adminapprovedstudents'),




    path('alllogin',views.login,name='alllogin'),

    path('hodaddleave',views.hodaddleave,name='hodaddleaverequest'),
    path('hodleavefun',views.hodaddleavefun,name='hodaddleavefun'),

    path('adminviewleave',views.adminviewleave,name='adminviewleave'),

    path('adminpendleave',views.adminpendleave,name='adminpendleave'),

    path('adminleaveapproved',views.adminleaveapproved,name='adminleaveapproved'),

    path('adminapproveleavehod',views.adminapproveleavehod,name='adminapproveleavehod'),

    path('adminviewhodleave',views.adminviewhodleave,name='adminviewhodleave'),

    path('adminapprovedhodleaveshow',views.adminapprovedhodleaveshow,name='adminapprovedhodleaveshow'),


    path('adminapproveleave/<int:leaveid>/',views.adminapproveleave,name='adminapproveleave'),

    path('adminrejectleave/<int:leaveid>/',views.adminrejectleave,name='adminrejectleave'),

    path('admindeleteleave',views.admindeleteleave,name='admindeleteleave'),

    path('hodteacherleavegot',views.hodteacherleavegot,name='hodteacherleavegot'),

    path('hodteacherleaveone/<int:leaveid>/',views.hodteacherleaveone,name='hodteacherleaveone'),



     
    path('teacheraddleave',views.teacheraddleave,name='teacheraddleave'),

    path('teacheraddleavefun',views.teacheraddleavefun,name='teacheraddleavefun'),

    path('hodapproveteacherleave',views.hodapproveteacherleave,name='hodapproveteacherleave'),



    

    path('teacherapprovestudentleave',views.teacherapprovestudentleave,name='teacherapprovestudentleave'),


    path('studentaddleavefun',views.studentaddleavefun,name='studentaddleavefun'),

   





   path('teacheraddstudentexam',views.teacheraddstudentexam,name='teacheraddstudentexam'),

  

   path('hodapproveviewexam',views.hodapproveviewexam,name='hodapproveviewexam'), 

   path('studentviewexamlist',views.studentviewexamlist,name='studentviewexamlist'),







    path('publish',views.publish,name="publish"),
    path('markupload',views.markupload,name="markupload"),
    path('publishview',views.publishview,name="publishview"),

]

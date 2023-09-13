from django.shortcuts import render
from school.models import School 

# Create your views here.


def home(request):

    # # get -------------------------------------
    # student_data = School.objects.get(name="nikita") # alos do like id or pk 
    # print("return" , student_data)
    print("------------------------")

    # first() --------------------------------------

    # student_data = School.objects.first()
    # student_data = School.objects.order_by("name").first()

    # last() --------------------------------------------------------

    # student_data = School.objects.order_by("name").last()

    # latest() -----------------------------------------------

    # student_data = School.objects.latest("pass_date")

    # earliest() -------------------------------------------
    # student_data = School.objects.earliest("pass_date")


    # exist() --------------------------------------------------------- return true or false 
    student_data = School.objects.all() # this is show not data becasue we set template for object not for entire object.
    # print(student_data)

    # print(student_data.exists() , "i am checking data have or not ")

    # exitstfor single objects ---------------------------------------
    # 

    one_data = School.objects.get(pk=1)
    print(student_data.filter(pk=one_data.pk).exists())



    # ----------------create methods ------------------

    # student_data = School.objects.create(name="priyanshu" , roll=2345678 , city="muradabad" , marks=543 , pass_date='2020-5-4')
    # student_data.save()


    # get and create incase data not have ---- get_or_create() ---------------------------------------------

    # student_data , created = School.objects.get_or_create(name="gaurav" , roll=2345676 , city="muradabad" , marks=543 , pass_date='2020-5-4')

    # print(created , " check get or create ")


    #-------------------------------------------------------------------

    # update(**kwargs) -------------------------------------------------

    # student_data = School.objects.filter(id=13).update(name="nikita murari" ,marks=665)
    # print(student_data) #check how many row it can update 

    # update multiple user data targetting similar marks or simmilar city -----------------------

    
    # student_data = School.objects.filter(marks=345).update(city="jahanabad")

    #-------------------------------------update or create ---------------------

    # student_data , created = School.objects.update_or_create(id=15 , name="gaurav" ,marks=543 , defaults={'name':'gau kumar'})
    # print(created) # if created it rru either false . 

    # bulk create -----------------------------------------------------

    # objs = [
    #     School(name="madhu" , roll=100, city="jahanabad" , pass_date="2022-06-12" , marks=567),
    #     School(name="madhu sahrma" , roll=101 , city="rahanabad" , pass_date="2022-06-12" , marks=567),
    #     School(name="madhu bhatia" , roll=1002 , city="mahanabad" , pass_date="2022-06-12" , marks=567),
    #     School(name="madhu malhotra" , roll=1003, city="gahanabad" , pass_date="2022-06-12" , marks=567),

    # ]

    # student_data = School.objects.bulk_create(objs) # other paramete is not usefull


    # ----------------------------bulkUpdate------------------------------------

    # all_student_date = School.objects.all()
    # for stu in all_student_date:
    #     stu.city = 'uttarpradesh'
    # student_data = School.objects.bulk_update(all_student_date , ['city'])

    # --------------------------------------------------------------------------in_bulk -- use for getting two onject at same time ---

    # student_data = School.objects.in_bulk([12 ,14])
    # print(student_data[12].name)
    # print(student_data[14].name)

    # # with blank list --------------
    # student_data = School.objects.in_bulk([])
    # print(student_data)# give emplty list . 

    # with all data ----------------

    # student_data = School.objects.in_bulk()
    # print(student_data) # its give all data from database .

    #---------------------------------------------------delete() -----------------------
    













    return render(request , 'home.html',  {'student' : student_data})

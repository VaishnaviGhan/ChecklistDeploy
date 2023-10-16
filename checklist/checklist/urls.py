"""checklist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from checkapp.forms import LoginForm
from checkapp import views
from checkapp import administration
from checkapp import display


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'), 
    path('register-customer/',views.register_customer,name='register-customer'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('add_project/',administration.add_project,name='add_project'),
    path('add_site/',administration.add_site,name='add_site'),
    path('add_department/',administration.add_department,name='add_department'),
    path('Add_CheckList_Header/',administration.Add_CheckList_Header,name='Add_CheckList_Header'),
    path('Add_CheckList_Footer/',administration.Add_CheckList_Footer,name='Add_CheckList_Footer'),
    path('Add_CheckList_Trans_Header/',administration.Add_CheckList_Trans_Header,name='Add_CheckList_Trans_Header'),
    path('User_Rights/',administration.User_Rights,name='User_Rights'),
    #path('checklist-queue/',display.checklist_queue,name='checklist_queue'),
    path('DHEQA_checklist_Queue/',display.DHEQA_checklist_Queue,name='DHEQA_checklist_Queue'),
    path('ProjectQA_checklist_Queue/',display.ProjectQA_checklist_Queue,name='ProjectQA_checklist_Queue'),
    path('ProjectHead_checklist_Queue/',display.ProjectHead_checklist_Queue,name='ProjectHead_checklist_Queue'),
    path('checklistbyyou/',display.Checklist_By_You,name='checklistbyyou'),
    path('checklist_avtar/<int:pk>/',display.checklist_avtar,name='checklist_avtar'),
    #------------- Checklist Header part ---------------------------
    path('create_checklistpre/', display.create_checklist_detailpre, name='create_checklist'),
    path('preview_checklist/', display.preview_checklist_detailpre, name='preview_checklist'),
    path('save_checklist/', display.save_checklist, name='save_checklist'),
    #------------ Checklist Footer part with site Engineer 
    path('start1_one/<str:checklist_id>/<str:saved_form1>/',display.start1_one, name='start1_one'),
    path('start1_two/<str:checklist_id>/<str:saved_form1>/',display.start1_two, name='start1_two'),
    path('start1_three/<str:checklist_id>/<str:saved_form1>/',display.start1_three, name='start1_three'),
    #------------ Checklist Footer part with DH Status and comment
    path('DHPre_one/<int:pk>/',display.DHPre_one, name='DHPre_one'),
    path('DHPre_two/<int:pk>/',display.DHPre_two, name='DHPre_two'),
    path('DHPre_three/<int:pk>/',display.DHPre_three, name='DHPre_three'),
    #--------------Other mechanism-----
    path('accept_checklist/<int:pk>/',display.accept_checklist,name='accept_checklist'),
    path('accept_checklist_ByDHEQA/<int:pk>/',display.accept_checklist_ByDHEQA,name='accept_checklist_ByDHEQA'),
    path('accept_checklist_ByProjectQA/<int:pk>/',display.accept_checklist_ByProjectQA,name='accept_checklist_ByProjectQA'),
    path('accept_checklist_ByProjectHead/<int:pk>/',display.accept_checklist_ByProjectHead,name='accept_checklist_ByProjectHead'),
    #path('checklist-queue/',display.checklist_queue,name='checklist-queue'),
    #path('workspace/',display.workspace,name='workspace'),
    path('DHEQA_workspace/',display.DHEQA_workspace,name='DHEQA_workspace'),
    path('ProjectQA_workspace/',display.ProjectQA_workspace,name='ProjectQA_workspace'),
    path('ProjectHead_workspace/',display.ProjectHead_workspace,name='ProjectHead_workspace'),
    path('closed-checklist/<int:pk>/',display.closed_checklist,name='closed-checklist'),
    path('all-closed-checklists/',display.all_closed_checklists,name='all-closed-checklists'),
    path('all_checklist_sendTo_ProjectQA/',display.all_checklist_sendTo_ProjectQA,name='all_checklist_sendTo_ProjectQA'),
    path('all_checklist_sendTo_ProjectHead/',display.all_checklist_sendTo_ProjectHead,name='all_checklist_sendTo_ProjectHead'),
    #-----------Project AQ Work---------
    path('observation-PQA/<int:pk>/',display.observation,name="observation-PQA"),
    path('observation_PQA_Queue/',display.observation_PQA_Queue,name='observation_PQA_Queue'),
    path('project_head/<int:pk>/',display.project_head,name="project_head"),
    path('Projrct_Head_Queue/',display.Projrct_Head_Queue,name='Projrct_Head_Queue'),
    path('rejected/<int:pk>/',display.Rejected_checklist,name='Rejected_checklist'),
    path('rejected_chechlists/',display.rejected_checklists,name='rejected_chechlists'),
    #path('edit_checklist/<int:pk>/',display.edit_checklist,name='edit_checklist'),
    path('edit_checklist/<int:pk>/',display.edit_checklist, name='edit_checklist'), 
    #------------------User -------------------
    path('addUser/',administration.addUser,name='addUser'),
    path('edit_user/<int:user_id>/', administration.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', administration.delete_user, name='delete_user'),
    path('usermaster/',administration.UserMaster,name='usermaster'),
    #------------------Project------------------------------------
    path('edit_project/<int:pk>/', administration.edit_project, name='edit_project'),
    path('delete_project/<int:pk>/', administration.delete_project, name='delete_project'),
    #-------------------Site-------------------------------------
    path('edit_site/<int:pk>/', administration.edit_site, name='edit_site'),
    path('delete_site/<int:pk>/', administration.delete_site, name='delete_site'),
     #-------------------Checklist Name-------------------------------------
    path('edit_checklistname/<int:pk>/', administration.edit_CheckList_Header, name='edit_checklistname'),
    path('delete_checklistname/<int:pk>/', administration.delete_CheckList_Header, name='delete_checklistname'),
    #-------------------Checklist Questions-------------------------------------
    path('edit_checklistQuestion/<int:pk>/', administration.edit_CheckList_Footer, name='edit_checklistQuestion'),
    path('delete_checklistQuestion/<int:pk>/', administration.delete_CheckList_Footer, name='delete_checklistQuestion'),
    #-------------------Add_Structural-Elements----------------
    path('Add_Structural_Elements/',administration.Add_Structural_Elements,name='Add_Structural_Elements'),
    path('edit_Structural_Elements/<int:pk>/',administration.edit_Structural_Elements,name='edit_Structural_Elements'),
    path('delete_Structural_Elements/<int:pk>/',administration.delete_Structural_Elements,name='delete_Structural_Elements'),
    #------------------------history--------------------------
    path('history/',administration.history,name='history'),
    
    
]

    



   

  
  
    




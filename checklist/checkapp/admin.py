from django.contrib import admin
from .models import Department,Project_Master,History,Site_Master,CustomUser,UserMaster,CheckList_Header,CheckList_Footer,CheckList_Trans_Header,CheckList_Trans_Details ,User_Rights,LogData,Structural_Element,LogDataNew
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class adminDepartment(admin.ModelAdmin):
    list_display = ['Department_ID','Department_Name']
    
admin.site.register(Department,adminDepartment)

class adminProject_Master(admin.ModelAdmin):
    list_display = ['Project_ID','Project_Name']
    
admin.site.register(Project_Master,adminProject_Master)

class adminSite_Master(admin.ModelAdmin):
    list_display = ['Site_ID', 'Site_Name', 'get_project_id', 'Project_Name']

    def get_project_id(self, obj):
        return obj.Project_ID
    get_project_id.short_description = 'Project ID'

admin.site.register(Site_Master,adminSite_Master)


class adminCustomUser(UserAdmin):
    fieldsets = (
       *UserAdmin.fieldsets,
       (
           'Custom Field Heading',
           {
               'fields':(
                   'is_SiteEngineer',
                   'is_DHEQA',
                   'is_ProjectQA',
                   'is_ProjectHead',
                   
               )
           }
       )
   )
admin.site.register(CustomUser,adminCustomUser)

class adminUserMaster(admin.ModelAdmin):
    list_display = ['User_ID','username','Department_ID','Department_Name','Project_ID','Project_Name','Site_ID','Site_Name']
    
    def get_user_id(self, obj):
        return obj.User_ID
    get_user_id.short_description = 'User_ID'
    
    def get_department_id(self, obj):
        return obj.Department_ID
    get_department_id.short_description = 'Department_ID'
    
    def get_Project_id(self, obj):
        return obj.Project_ID
    get_Project_id.short_description = 'Project_ID'
    
    def get_site_id(self, obj):
        return obj.Site_ID
    get_site_id.short_description = 'Site_ID'
    
admin.site.register(UserMaster,adminUserMaster)

class adminCheckList_Header(admin.ModelAdmin):
    list_display = ['CheckList_ID','CheckList_Title']
    
admin.site.register(CheckList_Header,adminCheckList_Header)

class adminUser_Rights(admin.ModelAdmin):
    list_display = ['User_Rights_ID','username','CheckList_ID']
    
    def get_user_id(self, obj):
        return obj. User_ID
    get_user_id.short_description = ' User_ID'
    
admin.site.register(User_Rights,adminUser_Rights)



#--------------------------------------------------------

class adminCheckList_Footer(admin.ModelAdmin):
    list_display = ['CheckList_Item_ID','CheckList_ID','CheckList_Title','CheckList_Item_Desc']
    
    def get_checklist_id(self, obj):
        return obj.CheckList_ID
    get_checklist_id.short_description = 'CheckList ID'
    
admin.site.register(CheckList_Footer,adminCheckList_Footer)


class adminCheckList_Trans_Header(admin.ModelAdmin):
   
    #list_display = ['Doc_ID','CheckList_ID','Project_Name','Site_Name','Name_Of_ABLStaff','inspection_Start_Date','inspection_End_Date','Contractor','Location','Structural_Element','Quality_Engineer_status','Project_Head_Status','assigned_to','assigned_to_ProjectQA','assigned_to_ProjectHead','is_resolved','checklist_status']
    list_display = ['Doc_ID','CheckList_ID','Project_Name','Site_Name','Name_Of_ABLStaff','inspection_Start_Date','Contractor','Location','Structural_Element','Quality_Engineer_status','Quality_Engineer_Comment','Project_Head_Status','assigned_to','assigned_to_ProjectQA','assigned_to_ProjectHead','is_resolved','checklist_status','rejected_byDHEQA']
    
    
admin.site.register(CheckList_Trans_Header,adminCheckList_Trans_Header)

class adminCheckList_Trans_Details(admin.ModelAdmin):
    list_display = ['CheckList_Trans_Details_ID','Doc_ID','CheckList_ID','CheckList_Item_ID','Site_Engineer_Status','Site_DH_EQA_Status','Site_Engineer_Comment','Site_DH_EQA_Comment']
  
    
admin.site.register(CheckList_Trans_Details,adminCheckList_Trans_Details)

'''class AdminLogData(admin.ModelAdmin):
    list_display = ['LogData_ID', 'Doc_ID', 'get_user_id', 'username','Next_User_Name', 'Date_Time']
        
    def get_user_id(self, obj):
        return obj.User_ID
    get_user_id.short_description = 'User_ID'
    
    def get_next_user_id(self, obj):
        return obj.User_ID
    get_user_id.short_description = 'next_User_ID'
    
    
admin.site.register(LogData, AdminLogData)'''

class AdminStructural_Element(admin.ModelAdmin):
    list_display = ['Struc_Ele_ID','Structural_Element']
    
admin.site.register(Structural_Element,AdminStructural_Element)

'''class AdminLogDataNew(admin.ModelAdmin):
    list_display = ['LogData_ID','Doc_ID','Name_Of_ABLStaff','assigned_to','assigned_to_ProjectQA','assigned_to_ProjectHead','Date_Time']
admin.site.register(LogDataNew,AdminLogDataNew)'''

class AdminHistory(admin.ModelAdmin):
    list_display = ['History_ID','Doc_ID','Date_Time','Comment']

admin.site.register(History,AdminHistory)
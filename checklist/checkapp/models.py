from django.db import models
from multiselectfield import MultiSelectField
from checkapp.config import Site_Engineer_Status,Quality_Engineer_status,Project_Head_Status,Site_DH_EQA_Status
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models import Max
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True)
    Department_Name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Department_Name
    
class Project_Master(models.Model):
    Project_ID = models.AutoField(primary_key=True)
    Project_Name = models.CharField(max_length=100)
           
    def __str__(self):
        return self.Project_Name
         
        
class Site_Master(models.Model):
    Site_ID = models.AutoField(primary_key=True)
    Site_Name = models.CharField(max_length=100)
    Project_Name = models.ForeignKey(Project_Master,on_delete=models.CASCADE)  # New field for project name
    Project_ID = models.IntegerField()
    def save(self, *args, **kwargs):
        self.Project_ID = self.Project_Name.Project_ID # Assign project name based on Project_ID
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.Site_Name
    
    
class CustomUser(AbstractUser):
     User_ID = models.AutoField(primary_key=True)
     username = models.CharField(max_length=100,unique=True) 
     is_SiteEngineer = models.BooleanField(default=False)
     is_DHEQA = models.BooleanField(default=False)
     is_ProjectQA = models.BooleanField(default=False)
     is_ProjectHead = models.BooleanField(default=False)
     
     def __str__(self):
        return self.username
    
    
class UserMaster(models.Model):
    User_ID = models.IntegerField()
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    Department_ID = models.IntegerField()
    Department_Name = models.ForeignKey(Department,on_delete=models.CASCADE)
    Project_ID = models.IntegerField()
    Project_Name = models.ForeignKey(Project_Master,on_delete=models.CASCADE)
    Site_ID = models.IntegerField()
    Site_Name =  models.ForeignKey(Site_Master,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.User_ID = self.username.User_ID
        self.Department_ID = self.Department_Name.Department_ID
        self.Project_ID = self.Project_Name.Project_ID
        self.Site_ID = self.Site_Name.Site_ID
        super().save(*args, **kwargs)

    
          
class CheckList_Header(models.Model):
    CheckList_ID = models.AutoField(primary_key=True)
    CheckList_Title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.CheckList_Title
    
class User_Rights(models.Model):
    User_Rights_ID = models.AutoField(primary_key=True)
    User_ID = models.IntegerField()
    username = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    CheckList_ID = models.ForeignKey(CheckList_Header,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.User_ID = self.username.User_ID
        super().save(*args, **kwargs)    
    
class CheckList_Footer(models.Model):
    CheckList_Item_ID = models.AutoField(primary_key=True)
    CheckList_ID = models.IntegerField()
    CheckList_Title = models.ForeignKey(CheckList_Header, on_delete=models.CASCADE, related_name='checklistID')
    Initial_Checks = models.BooleanField(default=False)
    Inprocess_Checks = models.BooleanField(default=False)
    Post_Checks = models.BooleanField(default=False)
    CheckList_Item_Desc = models.TextField()
    
    def save(self, *args, **kwargs):
        self.CheckList_ID = self.CheckList_Title.CheckList_ID # Assign project name based on Project_ID
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.CheckList_Item_Desc
    
class Structural_Element(models.Model):
    Struc_Ele_ID = models.AutoField(primary_key=True)
    Structural_Element = models.CharField(max_length=100)   
    @classmethod
    def reset_primary_key_sequence(cls):
        max_id = cls.objects.aggregate(Max('Struc_Ele_ID')).get('Struc_Ele_ID__max')
        if max_id is None:
            max_id = 0
        cls._meta.pk.sequence = max_id + 1
        
    def __str__(self):
        return self.Structural_Element

class CheckList_Trans_Header(models.Model):
    Status_choices = (
        ('Completed_By_SiteEngineer & Pending_By_DHEQA','Completed_By_SiteEngineer & Pending_By_DHEQA'),
        ('Completed_By_SiteEngineer & Active_At_DHEQA','Completed_By_SiteEngineer & Active_At_DHEQA'),
        ('Completed_By_DHEQA & Pending_By_ProjectQA','Completed_By_DHEQA & Pending_By_ProjectQA'),
        ('Completed_By_DHEQA & Active_At_ProjectQA','Completed_By_DHEQA & Active_At_ProjectQA'),
        ('Completed_By_ProjectQA & Pending_By_ProjectHead','Completed_By_ProjectQA & Pending_By_ProjectHead'),
        ('Completed_By_ProjectQA & Active_At_ProjectHead','Completed_By_ProjectQA & Active_At_ProjectHead'),
        ('Completed_By_ProjectHead','Completed_By_ProjectHead'),
        ('Rejected','Rejected'),
    
    )
    Doc_ID = models.AutoField(primary_key=True)   
    CheckList_ID = models.ForeignKey(CheckList_Header, on_delete=models.CASCADE)
    Project_Name = models.ForeignKey(Project_Master,on_delete=models.CASCADE)
    Site_Name = models.ForeignKey(Site_Master,on_delete=models.CASCADE,default=True)
    Name_Of_ABLStaff = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='created_by')
    inspection_Start_Date = models.DateTimeField(auto_now_add=True)
    inspection_End_Date = models.DateTimeField(null=True, blank=True)
    Contractor = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Structural_Element = models.ForeignKey(Structural_Element,on_delete=models.CASCADE)
    Chainage = models.CharField(max_length=100)
    Quality_Engineer_status = models.CharField(max_length=70, choices=Quality_Engineer_status,default='Unspecified')
    Quality_Engineer_Comment = models.CharField(max_length=220,editable=True,blank=True)
    Project_Head_Status = models.CharField(max_length=70, choices=Project_Head_Status,default='Unspecified')
    assigned_to = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,default=None,related_name='assigned_to')
    assigned_to_DHEQA = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,null=True,blank=True,default=None,related_name='assigned_to_DHEQA')
    assigned_to_ProjectQA = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True,default=None,related_name='assigned_to_ProjectQA')
    assigned_to_ProjectHead = models.ForeignKey(CustomUser,on_delete=models.DO_NOTHING,blank=True,null=True,default=None,related_name='assigned_to_ProjectHead')
    is_resolved = models.BooleanField(default=False)
    checklist_status = models.CharField(max_length=70,choices=Status_choices)
    rejected_byDHEQA = models.BooleanField(default=False)

    def __str__(self):
        return f"Doc ID: {self.Doc_ID}, CheckList ID: {self.CheckList_ID}"
   
class CheckList_Trans_Details(models.Model):
    CheckList_Trans_Details_ID = models.AutoField(primary_key=True)   
    Doc_ID = models.ForeignKey(CheckList_Trans_Header, on_delete=models.CASCADE,related_name='doc_id_details')
    CheckList_ID = models.ForeignKey(CheckList_Trans_Header, on_delete=models.CASCADE, related_name='checklist_id_details')
    CheckList_Item_ID = models.CharField(max_length=200)
    Site_Engineer_Status = models.CharField(max_length=70, choices=Site_Engineer_Status,default='Unspecified')
    Site_DH_EQA_Status = models.CharField(max_length=70, choices=Site_DH_EQA_Status,default='Unspecified')
    Site_Engineer_Comment = models.CharField(max_length=220,editable=True,blank=True)
    Site_DH_EQA_Comment = models.CharField(max_length=220,editable=True,blank=True)
    
    def __str__(self):
        return f"Doc ID: {self.Doc_ID}"

class LogData(models.Model):
    LogData_ID = models.AutoField(primary_key=True)
    Doc_ID = models.ForeignKey(CheckList_Trans_Header, on_delete=models.CASCADE)
    User_ID = models.IntegerField()
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='logdata_username')
    Next_User_ID = models.IntegerField()
    Next_User_Name = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True,related_name='logdata_nextusername')
    Date_Time = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        self.User_ID = self.username.User_ID
        self.Next_User_ID = self.username.User_ID
        super().save(*args, **kwargs)
        
class LogDataNew(models.Model):
     LogData_ID = models.AutoField(primary_key=True)
     Doc_ID = models.CharField(max_length=100)
     Name_Of_ABLStaff = models.CharField(max_length=100)
     assigned_to = models.CharField(max_length=100,null=True)
     assigned_to_ProjectQA = models.CharField(max_length=100,null=True)
     assigned_to_ProjectHead = models.CharField(max_length=100,null=True)
     Date_Time = models.DateTimeField()
     
     def save(self, *args, **kwargs):
        if not self.Date_Time:
            self.Date_Time = timezone.now()
        super().save(*args, **kwargs)
        
class History(models.Model):
    History_ID = models.AutoField(primary_key=True)
    Doc_ID =  models.CharField(max_length=100)
    Date_Time = models.DateTimeField()
    Comment =  models.CharField(max_length=100,null=True)
    
    def save(self, *args, **kwargs):
        if not self.Date_Time:
            self.Date_Time = timezone.now()
        super().save(*args, **kwargs)
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,UserCreationForm
from .models import CustomUser,Structural_Element,Project_Master,Site_Master,UserMaster,Department,CheckList_Header,CheckList_Footer,CheckList_Trans_Header,User_Rights,CheckList_Trans_Details,CheckList_Trans_Details
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput())
    password= forms.CharField(label='Password', widget=forms.PasswordInput())

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Repeat New Password', widget=forms.PasswordInput())

class CheckMaterialStockForm(forms.Form):
    materialcode = forms.CharField(label='Material Code', widget=forms.TextInput())
    agingdate = forms.DateField(label='Date Of Aging', widget=forms.DateInput(attrs={'type': 'date'}))
    
class addUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','password1','password2','last_name','is_superuser','email','is_staff','is_active','username','is_SiteEngineer','is_DHEQA','is_ProjectQA','is_ProjectHead']
      
class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','is_superuser','email','is_staff','is_active','username','is_SiteEngineer','is_DHEQA','is_ProjectQA','is_ProjectHead']    

class UserMasterForm(forms.ModelForm):
    class Meta:
        model = UserMaster     
        fields = ['username','Department_Name','Project_Name','Site_Name'] 
      
      
        
class RegisterCustomerForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','username']
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project_Master
        fields = ['Project_Name']
        
        
class SiteForm(forms.ModelForm):
    class Meta:
        model = Site_Master
        fields = ['Site_Name','Project_Name']
        
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Department_Name']
        
class CheckList_HeaderForm(forms.ModelForm):
    class Meta:
        model = CheckList_Header
        fields = ['CheckList_Title']
        
        
class CheckList_FooterForm(forms.ModelForm):
    class Meta:
        model = CheckList_Footer
        fields = ['CheckList_Title','CheckList_Item_Desc']
        
        
class CheckList_Trans_HeaderForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        #fields = ['CheckList_ID','Project_Name','inspection_Start_Date','inspection_End_Date','Contractor','Location','Structural_Element']
        fields = ['CheckList_ID','Project_Name','inspection_End_Date','Contractor','Location','Structural_Element']
        
class UserRightsForm(forms.ModelForm):
     class Meta:
        model = User_Rights
        fields = ['username','CheckList_ID']
        
class CheckListTransHeaderFormfill(forms.ModelForm):

    class Meta:
        model = CheckList_Trans_Header
        fields = ['CheckList_ID','Project_Name','Site_Name','Contractor','Location','Structural_Element','Chainage','assigned_to']
  
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
          
            self.fields['assigned_to'].queryset = CustomUser.objects.filter(is_DHEQA=True)

            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit','Save'))
            
class stucturalElemForm(forms.ModelForm):
    class Meta:
        model = Structural_Element       
        fields = ['Structural_Element']   
            
class CheckList_Trans_DetailsFormFill(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Details
        fields = ['Site_Engineer_Status','Site_Engineer_Comment']
        widgets = {
            'Site_Engineer_Status': forms.RadioSelect()
        }

class CheckList_Trans_DetailsFormFill2(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Details
        fields = ['Site_DH_EQA_Status','Site_DH_EQA_Comment']
        widgets = {
            'Site_DH_EQA_Status': forms.RadioSelect,
        }
        
class ProjectQAForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        fields = ['Quality_Engineer_status','Quality_Engineer_Comment']
        widgets = {
            'Quality_Engineer_status': forms.RadioSelect()
        }
class ProjectHeadForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        fields = ['Project_Head_Status']
        widgets = {
            'Project_Head_Status': forms.RadioSelect()
        }
 
class assigned_to_ProjectQAForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        fields = ['assigned_to_ProjectQA']
        labels = {
            'assigned_to_ProjectQA': 'Submited to - ProjectQA',    
        }
        
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['assigned_to_ProjectQA'].queryset = CustomUser.objects.filter(is_ProjectQA=True)
        
class rejected_from_ProjectQAForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        fields = ['rejected_byDHEQA']
       
        
class assigned_to_ProjectHeadForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        fields = ['assigned_to_ProjectHead']
        
        
    def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['assigned_to_ProjectHead'].queryset = CustomUser.objects.filter(is_ProjectHead=True)
       
#--trying----
class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Header
        fields = ['CheckList_ID','Project_Name','Site_Name','Contractor','Location','Structural_Element','Chainage','assigned_to']
    

class CheckListDetailsForm(forms.ModelForm):
    class Meta:
        model = CheckList_Trans_Details
        fields = ['Site_Engineer_Status','Site_Engineer_Comment']

class CombinedCheckListForm(forms.Form):
    header_form = CheckListForm
    details_form = CheckListDetailsForm
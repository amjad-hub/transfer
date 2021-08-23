# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import user_account



# class transferForm(forms.ModelForm):
#     def get_users_names():
#         users = User.objects.all()
#         print (users)
#         i = 1
#         users_names = []
#         for u in users:
#             users_names.append((u,u.username))
#             i += 1
#         # GEEKS_CHOICES =( 
#         #     ("1", "One"), 
#         #     ("2", "Two"), 
#         #     ("3", "Three"), 
#         #     ("4", "Four"), 
#         #     ("5", "Five"), 
#         # ) 
#         return users_names
  
#     transfer_From = forms.ChoiceField(choices = get_users_names() )
#     transfer_To_TIN = forms.CharField(max_length=400)
#     amount_money = forms.DecimalField(max_digits=100, decimal_places=1)
#     class Meta:
#         model = user_account
#         fields = ['transfer_From','transfer_To_TIN','amount_money']
    
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['transferFrom'].queryset = User.objects.none()
    


from django import forms
from django.contrib.auth.models import User

from .models import UserProfile



# =========================
# User Update Form
# =========================

class UserForm(forms.ModelForm):

    class Meta:

        model = User


        fields = [

            "first_name",
            "last_name",
            "email"

        ]


        widgets = {


            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter first name"
                }
            ),


            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter last name"
                }
            ),


            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter email address"
                }
            ),

        }




# =========================
# Profile Update Form
# =========================

class ProfileForm(forms.ModelForm):


    class Meta:


        model = UserProfile


        fields = [

            "profile_picture",

            "phone",

            "date_of_birth",

            "gender"

        ]



        widgets = {


            "profile_picture": forms.FileInput(

                attrs={

                    "class": "form-control",

                    "accept": "image/*"

                }

            ),



            "phone": forms.TextInput(

                attrs={

                    "class": "form-control",

                    "placeholder": "Enter phone number"

                }

            ),




            "date_of_birth": forms.DateInput(

                attrs={

                    "class": "form-control",

                    "type": "date"

                }

            ),




            "gender": forms.Select(

                attrs={

                    "class": "form-select"

                }

            )

        }
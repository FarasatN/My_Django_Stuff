from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    name = forms.CharField()#validators=[check_for_z]
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again!')
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH")

    # def form_name_view(request):
    #     if request.method == "POST":
    #         formObject = form.FormName(request.POST)
    #
    #         if formObject.is_valid():
    #             print("Sucess!!!!!")
    #             # do some redirection
    #     else:
    #         # if a GET (or any other method) we'll create a blank form
    #         formObject = form.FormName()
    #     return render(request, 'basicapp/form_page.html', {'form': formObject})



    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise form.Validation("GOTCHA BOT!")
    #     return botcatcher

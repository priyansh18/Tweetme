from django import forms
from django.forms.utils import ErrorList

class FormUserMixins(object):
    def form_valid(self, form):
            if self.request.user.is_authenticated:
                form.instance.user = self.request.user
                return super(FormUserMixins,self).form_valid(form)
            else:
                form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must bve logged in to continue'])    
                return self.form_invalid(form)

class UserOwnerMixin(FormUserMixins,object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormUserMixins,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['this user is unable to change this tweet'])    
            return self.form_invalid(form)
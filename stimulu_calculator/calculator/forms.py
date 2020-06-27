from django import forms

type_of_person = ((0, 'Single'), (1, 'Married'), (2, 'Head of House Hold'))

class UsaForm(forms.Form):
    type_of_person = forms.ChoiceField(choices=type_of_person, label='Filling Status')
    Income = forms.IntegerField(min_value=1, initial=1000)
    Number_children = forms.IntegerField(min_value=0, initial=0, label='Number of Children Under 17')

class GermanyForm(forms.Form):
    Income = forms.IntegerField(min_value=1, initial=1000)
    Number_children = forms.IntegerField(min_value=0, initial=0,
                                         label='Number Of Children Under 17')


class CanadaForm(forms.Form):
    Number_children = forms.IntegerField(min_value=0, initial=0,
                                         label='Number Of Children Under 17')

class IncomeForm(forms.Form):
    Income = forms.IntegerField(min_value=1, initial=1000)
class AustraliaForm(forms.Form):
    Income = forms.IntegerField(min_value=1, initial=1000,label='Income Per Fortnight')

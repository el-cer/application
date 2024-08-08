from django import forms
import pandas as pd



class UploadCsv(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')




class ColumnSelectionForm(forms.Form):
    column = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        columns = kwargs.pop('columns', [])
        super(ColumnSelectionForm, self).__init__(*args, **kwargs)
        self.fields['column'].choices = [(col, col) for col in columns]

class SelectionDomain(forms.Form):
    choices = ['Computer Vision', 'Classification', 'Regression problem']
    CHOICES = [('', '')] + [(choice, choice) for choice in choices]

    Ml_domain = forms.ChoiceField(choices=CHOICES, label="Select a Problem")

from django import forms

class SelectionModel(forms.Form):
    model_domain = forms.ChoiceField(label="Select a Problem")

    def __init__(self, dict_of_models, domain, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if domain:
            print(domain)
            list_of_model = dict_of_models.get(domain, [])
            choices = [('', '')] + [(choice, choice) for choice in list_of_model]
            self.fields['model_domain'].choices = choices

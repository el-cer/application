from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import UploadCsv, ColumnSelectionForm, SelectionDomain, SelectionModel
import pandas as pd
import os
from .Ml import MachineLearning

def upload_csv(request):
    upload_form = UploadCsv()
    selection_form = None
    domain_form = SelectionDomain()
    columns = []
    data_html = None
    score = None
    domain = None
    mform = None

    current = os.getcwd()
    for i in os.listdir(current):
        if i.endswith('.sh'):
            script_path = os.path.join(current, i)

    if request.method == 'POST':
        if 'Ml_domain' in request.POST:
            domain_form = SelectionDomain(request.POST)
            if domain_form.is_valid():
                domain = domain_form.cleaned_data['Ml_domain']
                request.session['domain'] = domain
                return redirect('upload_csv')  # Redirect to avoid form resubmission issues

            if "model_domain" in request.POST:
                        domain = request.session.get('domain')
                        dict_of_models = MachineLearning().dict_of_models
                        mform = SelectionModel(dict_of_models, domain, request.POST)
                        if mform.is_valid():
                            model = mform.cleaned_data['model_domain']
                            request.session['model'] = model
                            print(model)
                            return redirect('upload_csv')

        if 'csv_file' in request.FILES:
            upload_form = UploadCsv(request.POST, request.FILES)
            if upload_form.is_valid():
                csv_file = request.FILES['csv_file']
                file_name = default_storage.save(csv_file.name, ContentFile(csv_file.read()))
                file_path = default_storage.path(file_name)

                data = pd.read_csv(file_path)
                columns = data.columns.tolist()
                request.session['columns'] = columns  # Store columns in session
                selection_form = ColumnSelectionForm(columns=columns)
            else:
                print('Upload form is not valid:', upload_form.errors)

        elif 'select_column' in request.POST:
            columns = request.session.get('columns', [])
            selection_form = ColumnSelectionForm(request.POST, columns=columns)
            if selection_form.is_valid():
                selected_column = selection_form.cleaned_data['column']
                file_path = default_storage.path(default_storage.listdir('')[1][0])  # assuming only one CSV file
                data = pd.read_csv(file_path)

                ml = MachineLearning()
                score = ml.RegressionLin(data, selected_column)
            else:
                print('Selection form is not valid:', selection_form.errors)

    if not selection_form and 'columns' in request.session:
        selection_form = ColumnSelectionForm(columns=request.session.get('columns'))

    if request.session.get('domain'):
        domain = request.session['domain']
        dict_of_models = MachineLearning().dict_of_models
        mform = SelectionModel(dict_of_models, domain, request.POST)
       

    return render(request, 'home.html', {
        'upload_form': upload_form,
        'selection_form': selection_form,
        'domain_form': domain_form,
        'columns': columns,
        'score': score,
        'domain': domain,
        'model_form': mform,
        'model': request.session.get('model')
    })

def modeles_available(request):
    return render(request, "model_list.html")

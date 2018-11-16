# -*- encoding:utf8 -*-
from mdeditor.fields import MDTextFormField
from django import forms


class MDEditorForm(forms.Form):
    name = forms.CharField()
    content = MDTextFormField()


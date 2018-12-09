# -*- encoding:utf8 -*-
from mdeditor.fields import MDTextFormField
from django import forms


# mdedtior富文本编辑器的前端form表单
class MDEditorForm(forms.Form):
    name = forms.CharField()
    content = MDTextFormField()


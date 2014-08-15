__author__ = 'liangnaihua'

from  django import forms
from models import Devices, Server, Status
from django.forms import ModelChoiceField

class DevicesForm(forms.ModelForm):

	class Meta:
		model = Devices
		# exclude = [] # uncomment this line and specify any field to exclude it from the form

	def __init__(self, *args, **kwargs):
		super(DevicesForm, self).__init__(*args, **kwargs)


class ServerForm(forms.ModelForm):

	class Meta:
		model = Server
		# exclude = [] # uncomment this line and specify any field to exclude it from the form

	def __init__(self, *args, **kwargs):
		super(DevicesForm, self).__init__(*args, **kwargs)

class ServersSearchForm(forms.Form):
	asset           =forms.CharField(label='资产编号', max_length=60, required=False)
	asset_old       =forms.CharField(label='旧资产编号', max_length=60, required=False)
	type            =forms.CharField(label='类别', max_length=60, required=False)
	subtype         =forms.CharField(label='子类别', max_length=60, required=False)
	manufacturer    =forms.CharField(label='品牌', max_length=60, required=False)
	model           =forms.CharField(label='型号', max_length=100, required=False)
	status		    =ModelChoiceField(label='使用状态', queryset=Status.objects.all(), required=False)
	building        =forms.CharField(label='机房(所处位置)',max_length=60, required=False)
	location        =forms.CharField(label='机柜',max_length=60, required=False)
	consignee       =forms.CharField(label='托管编号',max_length=60, required=False)
	hostname        =forms.CharField(label='主机名',max_length=60, required=False)
	vendor          =forms.CharField(label='供应商',max_length=200, required=False)
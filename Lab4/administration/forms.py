from django import forms

from cleaning.models import Service, ServicePack, ServicePackInstance


class ServicePackInstanceForm(forms.ModelForm):
    date_created = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ServicePackInstance
        fields = ['status', 'price', 'date_created']

    def __init__(self, service_pack, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service_pack = service_pack

    def save(self, commit=True):
        servicepackinstance = super().save(commit=False)
        servicepackinstance.service_pack = self.service_pack

        if commit:
            servicepackinstance.save()
        self.save_m2m()
        return servicepackinstance


class ServicePackForm(forms.ModelForm):
    class Meta:
        model = ServicePack
        fields = ('naming', 'service')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Edit existing object
            self.fields['service'].initial = self.instance.service.all()

    def save(self, commit=True):
        servicepack = super().save(commit=False)
        if commit:
            servicepack.save()
        if self.cleaned_data['service']:
            servicepack.service.set(self.cleaned_data['service'])
        else:
            servicepack.service.clear()
        self.save_m2m()
        return servicepack

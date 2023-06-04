from django import forms
from cleaning.models import Service, ServicePack

class ServicePackForm(forms.ModelForm):
    # category = forms.ModelMultipleChoiceField(
    #     queryset=Service.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    class Meta:
        model = ServicePack
        fields = ('naming', 'service', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
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

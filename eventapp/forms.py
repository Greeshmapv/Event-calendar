from django import forms
from.models import Event
class DateInput(forms.DateInput):
    input_type='date'


class EventForm(forms.ModelForm):
    
    class Meta:
        model= Event
        fields= "__all__"

        widgets={
            "date":DateInput(),
        }


        labels={
            'date':"Date",
            'name':'Event Name',
            'payment_details':"Payment Details",
            'contact_phone':"Phone Number",
        }
from django.core.mail import send_mail
from django.shortcuts import render
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

def contact_view(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid() and not form.cleaned_data.get("honeypot"):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Message from {name} <{email}>:\n\n{message}"

            send_mail(
                subject="New Contact Form Message",
                message=full_message,
                from_email=email,
                recipient_list=["jorge.vargas@studiobaca.com"],
            )
            success = True
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "success": success})
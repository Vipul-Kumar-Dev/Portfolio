from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactForm
from .forms import FAQForm
from django.core.mail import send_mail
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)

def homepage(request):
    return render(request, 'Portfolio.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data.get('phone', 'Not provided')
            preferred_contact = form.cleaned_data.get('preferred_contact', 'Not specified')
            best_time = form.cleaned_data.get('best_time', 'Not specified')
            message = form.cleaned_data['message']

            full_message = (
                f"New Contact Form Submission:\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Preferred Contact Method: {preferred_contact}\n"
                f"Best Time to Contact: {best_time}\n\n"
                f"Message:\n{message}"
            )

            send_mail(
                subject=f"New message from {name}",
                message=full_message,
                from_email=email,
                recipient_list=['vipulsam1234@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "Thank you for your message. I’ll get back to you soon!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def about(request):
    return render(request, 'about.html')

def FAQ(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            question = form.cleaned_data['question']

            send_mail(
                subject=f"FAQ Question from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nQuestion:\n{question}",
                from_email=email,
                recipient_list=['vipulsam1234@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, "Your question has been sent successfully!")
            return redirect('faq')
    else:
        form = FAQForm()

    return render(request, 'faq.html', {'form': form})

def Main(request):
    return render(request, 'Main.html')
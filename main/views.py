from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Formadan kelgan ma'lumotlarni ishlatish
            your_name = form.cleaned_data['your_name']
            your_email = form.cleaned_data['your_email']
            # Boshqa kerakli ishlarni bajaring
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
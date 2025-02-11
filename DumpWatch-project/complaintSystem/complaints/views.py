from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


def raise_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ComplaintForm()
    return render(request, 'user_dashboard.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Please enter correct details')
    return render(request, 'complaints/admin_login.html')

def user_dashboard(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/user_dashboard.html', {'form': form})

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    complaints = Complaint.objects.all().order_by('marked', '-id')
    sorted_complaints = sorted(complaints, key=lambda c: (c.marked, c.date))
    return render(request, 'complaints/admin_dashboard.html', {'complaints': sorted_complaints})

def delete_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    complaint.delete()
    return redirect('admin_dashboard')

def mark_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        marked = request.POST.get('marked') == '1'
        complaint.marked = marked
        complaint.save()

        # Send email if marked as done
        if marked:
            subject = 'Complaint Acknowledgment'
            message = f'Dear {complaint.name},\n\nYour complaint has been resolved. Thank you for reporting the issue.\n\nRegards,\nAdmin.'
            from_email = 'replaceyourmail@gmail.com'  # Replace with your email
            recipient_list = [complaint.email]  # Send to the user's email
            send_mail(subject, message, from_email, recipient_list)

        return redirect('admin_dashboard')


    

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Document,Share
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
import pdb


@login_required
def dashboard(request):
    user= request.user

    total_documents = Document.objects.filter(user_id=user).count()
    shared_documents = Share.objects.filter(Q(shared_by=user) | Q(shared_with=user)).count()
    recent_documents = Document.objects.filter(user_id=user).order_by('-created_at')[:5]

    context = {
        'total_documents': total_documents,
        'shared_documents': shared_documents,
        'recent_documents': recent_documents,
    }

    return render(request, 'dashboard.html', context)

@login_required
def upload_new_document(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        title = request.POST.get('title')
        document_type = request.POST.get('document_type')
        description = request.POST.get('description', '')
        
        if file and title:
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_path = fs.url(filename)

            document = Document(
                user_id=request.user,
                title=title,
                description=description,
                file_path=file_path,
                document_type=document_type,
                size=file.size
            )
            document.save()
            return redirect('/dashboard')  
        else:
            return HttpResponse("Missing file or name", status=400)

    return render(request, 'home_templates/upload_new_document.html')


@login_required
def view_all_documents(request):
    documents = Document.objects.filter(user_id=request.user)
    return render(request, 'home_templates/view_all_documents.html', {'documents': documents})
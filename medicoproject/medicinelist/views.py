from django.shortcuts import render,redirect,get_object_or_404
from .models import Medicine
from .forms import MedicineForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse
from django.urls import reverse


@login_required(login_url='/login/')
def medicine_list(request):
    medicines = Medicine.objects.all()
    paginator = Paginator(medicines, 2)
    page_number = request.GET.get('page')
    try:
        medicines = paginator.page(page_number)
    except PageNotAnInteger:
        medicines = paginator.page(1)
    except EmptyPage:
        medicines = paginator.page(paginator.num_pages)
    return render(request, 'medicine_list.html',{'medicines':medicines})

def count_medicines():
    return Medicine.objects.count()
def can_add_medicine():
    return count_medicines() < 5

@login_required(login_url='/login/')
def add_medicine(request):
    if request.method == 'POST':
        if can_add_medicine():
            form = MedicineForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Medicine successfully added.')
                return redirect('medicine_list')
        else:
            messages.error(request, 'Cannot add more than 5 medicines.')

        form = MedicineForm(request.POST) 
    else:
        form = MedicineForm()
    return render(request, 'add_medicine.html', {'form': form})

@login_required(login_url='/login/')
def medicine_update(request, id):
    med = get_object_or_404(Medicine, pk=id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=med)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=med)
    
    return render(request, 'update.html', {'form': form})

@login_required(login_url='/login/')
def medicine_delete(request, id):
    med = get_object_or_404(Medicine,id=id)
    if request.method == 'POST':
        med.delete()
        return redirect('medicine_list')
    
    return render(request,'delete.html',{'med':med})

def search_medicines(request):
    search_term = request.GET.get('search_term')
    medicines = Medicine.objects.filter(name__icontains=search_term)
    
    html = ''
    for medicine in medicines:
        update_url = reverse('update_med', args=[medicine.id])
        delete_url = reverse('delete_med', args=[medicine.id])
        html += f'''
        <tr>
            <td>{medicine.id}</td>
            <td>{medicine.name}</td>
            <td>{medicine.stocks}</td>
            <td>{medicine.date_and_time}</td>
            <td><a href="{update_url}" class="btn btn-secondary">Update</a></td>
            <td><a href="{delete_url}" class="btn btn-secondary">Delete</a></td>
        </tr>
        '''
    
    return JsonResponse(html, safe=False)













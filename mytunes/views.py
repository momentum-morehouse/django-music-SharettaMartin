from django.shortcuts import render
from .models import mytunes
# Create your views here.
# def add_albums(request, pk):
#     contact = get_object_or_404(Contact, pk=pk)
#     if request.method == 'POST':
#         contact.delete()
#         return redirect(to='list_contacts')

#     return render(request, "contacts/delete_contact.html",
#                   {"contact": contact})
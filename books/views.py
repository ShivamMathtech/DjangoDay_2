from django.shortcuts import render ,redirect
from .forms import NewBookForm
from .models import NewBook
# Create your views here.
def index_view(req):
    books= NewBook.objects.all()
    if req.method=='POST':
        form =NewBookForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req,'index.html')
    else:
        form =NewBookForm()     

    return render(req,'index.html',{'books':books})

# #list all the books
def book_list(req):
    books= NewBookForm.objects.all()
    return render(req,'index.html',{'books':books})

# #create a book
# def book_create(req):
#     if req.method=='POST':
#         form =Bookform(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list_book')  
#     else:
#         form =Bookform()
#     return  render(req,'book_form.html',{'form':form})           

# #update books
# def book_update(req,pk):
#     book =get_object_or_404(Book,pk=pk)
#     if req.method=='POST':
#         form=Bookform(req.POST,instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('list_book')
#     else:
#         form =Bookform(instance=book)
#     return render(req,'book_forms.html',{'form':form})            

# def book_delete(req,pk):
#     book= get_object_or_404(Book,pk=pk)
#     if request.method == "POST":
#         book.delete()
#         return redirect('book_list')
#     return render(req, 'books/delete_confirm.html', {'book': book})    
from django.shortcuts import render

# Create your views here.
# By Gobs 08032020
def post_list(request):
    return render(request, 'blog/post_list.html', {})
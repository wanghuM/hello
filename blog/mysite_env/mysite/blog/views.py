from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,BlogType

def blog_list(request):
    
    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list,7)#每7篇进行分页
    page_num = request.GET.get('page',1) #获取url的页面参数(GET请求)
    page_of_blogs = paginator.get_page(page_num)#get_page django自带函数 page=后面是错误时i


    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    #context['blogs'] = Blog.objects.all()
    context['blog_types']= BlogType.objects.all()
    #context['blogs_count'] = Blog.objects.all().count()另一种统计博客方法
    return render_to_response('blog/blog_list.html',context)

def blog_detail(request,blog_pk):  #pk 为主键

    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html',context)

def blogs_with_type(request,blog_type_pk):
    
    blog_type= get_object_or_404(BlogType,pk=blog_type_pk)
    blogs_types_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs_types_list,7)
    page_num = request.GET.get('page',1)
    page_of_blogs = paginator.get_page(page_num)

    context={}
    context['blog_type']= blog_type
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    #context['blogs'] = Blog.objects.filter(blog_type=blog_type)#删选具体类型
    context['blog_types']= BlogType.objects.all()

    return render_to_response('blog/blogs_with_type.html',context)

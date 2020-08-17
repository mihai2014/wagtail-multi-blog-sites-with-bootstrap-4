from home.models import Root
from wagtail.core.models import Page
from blog.models import BlogIndex, BlogPage, BlogTagIndex, BlogCategory
from debug.models import DebugIndex, DebugPage1

#page = DebugIndex.objects.all()[0]

#def traverse(item):
#    print(item.title,item.url)
#    items = item.get_children()    #.live().in_menu()
#    for item in items:
#        if(len(item.get_children())!=0):
#            traverse(item)
#        else:
#            print(item.title,item.url)


#def traverse2(item):
#    print("-",item.title,item.url)
#    for item in item.get_children():
#        traverse2(item)

#traverse2(page)

index = BlogIndex.objects.filter(title='Posts')[0]
categories = BlogCategory.objects.order_by("name")
#all tree
#posts = BlogPage.objects.live().descendant_of(index)
#only 1st level descendants
posts = index.get_children().live()

for category in categories:
    #print(category.name, category.id)
    for post in posts:
        if(len(post.specific.categories.all()) > 0):
            if(post.specific.categories.all()[0].name == category.name):
                print(post.title,category.name)

# posts with no category assigned
for post in posts:
    if(len(post.specific.categories.all()) == 0):
        print(post.title,"No category")






#/home/mihai/all/data/wagtail/mysite
#from home.models import Root
#from site1.models import Root
#print(Root)

from wagtail.core.models import Page
print(Page)
from site1.models import *

print(dir())

index = Site1Index.objects.filter(title='Posts')[0]
#posts = index.get_children().live()
print(index.id)


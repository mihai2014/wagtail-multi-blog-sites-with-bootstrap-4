import datetime, pytz
from site1.models import Site1Index

Posts = Site1Index.objects.all()[0]
#blogpages = Posts.get_children().live().order_by('-first_published_at')
blogpages = Posts.get_children().filter(first_published_at__gte=datetime.datetime(2020, 8, 9, 0, 0, 0, 0, tzinfo=pytz.utc))
#year, month, day, hour, minute, second, microsecond

for page in blogpages:
    print(page)
    page.delete()

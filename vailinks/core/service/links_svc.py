from ..models import Link


def add_link(new_link):
    link = Link(description=new_link)
    link.save()
    return link.to_dict_json()


def list_links():
    links = Link.objects.all()
    return [item.to_dict_json() for item in links]


def find(query):
    return Link.objects.filter(keyword__icontains=query).first()

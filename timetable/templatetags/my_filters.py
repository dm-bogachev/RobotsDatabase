from django.template.defaulttags import register


@register.filter
def get_range(value):
    list = []
    for i in range(value):
        list.append("{:02}:{:02}".format(int(30 * i / 100), int(30 * i % 100)))#str(int(30 * i / 100)) + ":" + str(int(30 * i % 100)))
    return list

@register.filter
def get_time_by_id(id):
    return str(int(30*id/100)) + ":" + str(int(30*id % 100))
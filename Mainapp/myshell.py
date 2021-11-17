import os
os.environ.setdefault("DANGO_SETTING_MODULE","learning_log_settings")

import django
django.setup()

from Mainapp.models import Topic, Entry

topics = Topic.objects.all()


for topic in topics:
    print(topic.id,topic)


t=Topic.objects.get(id=1)

print(t.text)

print(t.date_added)





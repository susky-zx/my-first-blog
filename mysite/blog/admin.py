from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)

# 我们导入了前面定义的Post模型，为了让我们在admin页面上可见，
# 我们需要使用admin.site.register(Post)来注册模型

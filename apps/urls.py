from django.urls import path,includefrom .user import urls as user_urlsurlpatterns = [    path('user_api/', include(user_urls)),    #path('course/', include(course_urls)),]
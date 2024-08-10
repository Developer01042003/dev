from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='regist'),
    path('login/',views.SignIn,name='login'),
    path('reset/',views.passwordreset,name='reset'),
    path('logout/',views.logout_view,name='logout'),

    #work link direct and task related
    path('liveWork/',views.newCamps,name='liveWork'),
    path('linkredirect/<str:id>/',views.redirectit,name='redlink'),
    path('task_click/<str:id>/', views.handle_task_click, name='handle_task_click'),

    #profile related
    path('profile/',views.profile,name="profile"),
    path('withhistory/',views.withhistory,name='withhistory'),
    path('payout/',views.payout,name='payout'), #payout page
    path('withdrawb/',views.withdraw_balance,name='withdraw_balance'),
    path('task-work/',views.task_record,name="taskhistory"),

    #htmx= payment detail update ,



]

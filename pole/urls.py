from django.urls import path
from .views import home_view, voter_register_view, officer_login_view, registration_success_view, candidate_add_view, success_view, officer_dashboard_view, result_view, candidate_list_view, candidate_edit_view, candidate_delete_view ,voter_list_view, voter_edit_view, voter_delete_view, voting_pole_view, voter_login_view, failure_view, voting_success_view


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', voter_register_view, name='register'),
    path('voters/', voter_list_view, name='voter_list'),
    path('voter/edit/<int:pk>/', voter_edit_view, name='voter_edit'),
    path('voter/delete/<int:pk>/', voter_delete_view, name='voter_delete'),



    path('officer_login/', officer_login_view, name='officer_login'),
    path("officer_dashboard/", officer_dashboard_view, name="officer_dashboard"),
    path('registration_success/<int:voter_id>/', registration_success_view, name='registration_success'),


    path('candidate_add/', candidate_add_view, name='candidate_add'),
    path('candidates/', candidate_list_view, name='candidate_list'),
    path('candidates/edit/<int:pk>/', candidate_edit_view, name='candidate_edit'),
    path('candidates/delete/<int:pk>/', candidate_delete_view, name='candidate_delete'),
    path('success/', success_view, name='success'),


    path("voter_pole_login/", voter_login_view, name="voter_login"),
    path("voting_pole/", voting_pole_view, name="voting_pole"),
    path('failure/',failure_view, name="failure" ),
    path('voting_success/<int:candidate_sl_number>/',voting_success_view, name="voting_success" ),
    path("result/",result_view, name="result"),
]

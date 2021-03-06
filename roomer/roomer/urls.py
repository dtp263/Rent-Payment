from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #Auth URLs
    url(r'^auth_login/$', 'django.contrib.auth.views.login', name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/' }, name='logout'),
    url(r'^account/password_change/$', 'django.contrib.auth.views.password_change',
            name='password_change'),
    url(r'^account/password_change/done/$', 'django.contrib.auth.views.password_change_done',
            name='password_change_done'),
    url(r'^account/password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^account/password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
            name='password_reset_done'),
    url(r'^account/reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^account/reset/done/$', 'django.contrib.auth.views.password_reset_complete',
            name='password_reset_complete'),

    #Core URLs
    url(r'^$', TemplateView.as_view(template_name='core/index.html'), name='index'),
    url(r'^account/$', 'core.views.account', name='account'),

    url(r'^profile_photo_upload/(?P<profile_id>\d+)/$',
            'core.views.upload_profile_pic'),

    url(r'^property_addition/(?P<property_id>\d+)/$','core.views.add_tenant_to_property',
            name='add_tenant_to_property'),
    #Core registration and login
    url(r'^registerLandlord/$', 'core.views.registerLandlord', name='registerLandlord'),
    url(r'^registerTenant/$', 'core.views.registerTenant', name='registerTenant'),
    url(r'^login/$', 'core.views.loginView', name='loginView'),
    url(r'^signup/', 'core.views.sign_up_in'),

    url(r'^user_profile/(?P<user_id>\d+)$', 'core.views.user_profile', name="user_profile"),
    url(r'^edit_account_settings/$', 'core.views.editAccountSettings', name="edit_user_settings"),

    #Property URLs
    url(r'^newPropertyForm/$', 'core.views.newProperty', name='new_property'),
    url(r'^propertyProfile/(?P<property_id>\d+)/$', 'core.views.property_profile', name='property_profile_url'),
    url(r'^property_photo_upload/(?P<property_id>\d+)/$', 'core.views.upload_property_pic'),
    url(r'^$', 'core.views.secured'),
    url(r'^edit_property_info/(?P<property_id>\d+)/$', 'core.views.edit_property_info',
            name='edit_property_info'),

    url(r'^all_properties/$', 'core.views.viewAllProperties', name='all_properties'),


)
urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT,}),)
urlpatterns += staticfiles_urlpatterns()
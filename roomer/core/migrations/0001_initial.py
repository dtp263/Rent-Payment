# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'propertyProfile'
        db.create_table('core_propertyprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('numberOfbedrooms', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('num_of_bathrooms', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('parking', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cats_allowed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dogs_allowed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('totalcost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('property_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='(No description provided.)')),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('core', ['propertyProfile'])

        # Adding model 'UserProfile'
        db.create_table('core_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(default='0.0.0.0', max_length=15)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('hometown', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_landlord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('profile_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('living_in', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.propertyProfile'], null=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('core', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'propertyProfile'
        db.delete_table('core_propertyprofile')

        # Deleting model 'UserProfile'
        db.delete_table('core_userprofile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.propertyprofile': {
            'Meta': {'object_name': 'propertyProfile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cats_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'(No description provided.)'"}),
            'dogs_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_of_bathrooms': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numberOfbedrooms': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'parking': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'property_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'street_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'totalcost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15'}),
            'is_landlord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'living_in': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.propertyProfile']", 'null': 'True'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['core']
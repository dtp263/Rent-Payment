# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'addressType'
        db.create_table(u'core_addresstype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.TextField')(max_length=15)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'core', ['addressType'])

        # Adding model 'propertyProfile'
        db.create_table(u'core_propertyprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.addressType'])),
            ('numberOfbedrooms', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('totalcost', self.gf('django.db.models.fields.IntegerField')(default='n/a')),
            ('property_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='(No description provided.)')),
        ))
        db.send_create_signal(u'core', ['propertyProfile'])

        # Adding model 'UserProfile'
        db.create_table(u'core_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(default='0.0.0.0', max_length=15)),
            ('islandlord', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('profile_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['UserProfile'])

        # Adding M2M table for field properties on 'UserProfile'
        db.create_table(u'core_userprofile_properties', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'core.userprofile'], null=False)),
            ('propertyprofile', models.ForeignKey(orm[u'core.propertyprofile'], null=False))
        ))
        db.create_unique(u'core_userprofile_properties', ['userprofile_id', 'propertyprofile_id'])


    def backwards(self, orm):
        # Deleting model 'addressType'
        db.delete_table(u'core_addresstype')

        # Deleting model 'propertyProfile'
        db.delete_table(u'core_propertyprofile')

        # Deleting model 'UserProfile'
        db.delete_table(u'core_userprofile')

        # Removing M2M table for field properties on 'UserProfile'
        db.delete_table('core_userprofile_properties')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.addresstype': {
            'Meta': {'object_name': 'addressType'},
            'city': ('django.db.models.fields.TextField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'core.propertyprofile': {
            'Meta': {'object_name': 'propertyProfile'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.addressType']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "'(No description provided.)'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numberOfbedrooms': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'property_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'totalcost': ('django.db.models.fields.IntegerField', [], {'default': "'n/a'"})
        },
        u'core.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'default': "'0.0.0.0'", 'max_length': '15'}),
            'islandlord': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'properties': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.propertyProfile']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['core']
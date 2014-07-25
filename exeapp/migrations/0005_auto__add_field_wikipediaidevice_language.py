# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WikipediaIdevice.language'
        db.add_column('exeapp_wikipediaidevice', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WikipediaIdevice.language'
        db.delete_column('exeapp_wikipediaidevice', 'language')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'exeapp.activityidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'ActivityIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Activity'", 'max_length': '100'})
        },
        'exeapp.appletidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'AppletIdevice'},
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'java_file': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        },
        'exeapp.caseactivity': {
            'Meta': {'object_name': 'CaseActivity'},
            'activity': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'feedback': ('exeapp.models.idevices.fields.FeedbackField', [], {'blank': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idevice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exeapp.CaseStudyIdevice']", 'related_name': "'terms'"})
        },
        'exeapp.casestudyidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'CaseStudyIdevice'},
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'story': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Case Study'", 'max_length': '100'})
        },
        'exeapp.clozeidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'ClozeIdevice'},
            'cloze_text': ('exeapp.models.idevices.fields.ClozeTextField', [], {'blank': 'True', 'default': "''"}),
            'description': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'feedback': ('exeapp.models.idevices.fields.FeedbackField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Cloze'", 'max_length': '100'})
        },
        'exeapp.commentidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'CommentIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Remark'", 'max_length': '100'})
        },
        'exeapp.dublincore': {
            'Meta': {'object_name': 'DublinCore'},
            'contributors': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '256'}),
            'coverage': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'creator': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'language': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '32'}),
            'publisher': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'relation': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256'}),
            'rights': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256'}),
            'source': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'subject': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256'}),
            'title': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '128'}),
            'type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256'})
        },
        'exeapp.externalurlidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'ExternalURLIdevice'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '300'}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '200'})
        },
        'exeapp.feedbackidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'FeedbackIdevice'},
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'default': "''", 'max_length': '50'}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '200'})
        },
        'exeapp.freetextidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'FreeTextIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'})
        },
        'exeapp.genericidevice': {
            'Meta': {'db_table': "'exeapp_idevice'", 'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'proxy': 'True', 'object_name': 'GenericIdevice'}
        },
        'exeapp.glossaryidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'GlossaryIdevice'},
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Glossary'", 'max_length': '100'})
        },
        'exeapp.glossaryterm': {
            'Meta': {'object_name': 'GlossaryTerm'},
            'definition': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idevice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exeapp.GlossaryIdevice']", 'related_name': "'terms'"}),
            'title': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''", 'max_length': '100'})
        },
        'exeapp.idevice': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Idevice'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'child_type': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '32'}),
            'edit': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exeapp.Node']", 'related_name': "'idevices'"})
        },
        'exeapp.multichoiceidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'MultiChoiceIdevice'},
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'question': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Multiple Choice'", 'max_length': '100'})
        },
        'exeapp.multichoiceoptionidevice': {
            'Meta': {'object_name': 'MultiChoiceOptionIdevice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idevice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exeapp.MultiChoiceIdevice']", 'related_name': "'options'"}),
            'option': ('exeapp.models.idevices.fields.MultiChoiceOptionField', [], {'blank': 'True', 'default': "''"}),
            'right_answer': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'exeapp.node': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Node'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_root': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['exeapp.Package']", 'related_name': "'nodes'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['exeapp.Node']", 'null': 'True', 'related_name': "'children'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'exeapp.objectivesidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'ObjectivesIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Objectives'", 'max_length': '100'})
        },
        'exeapp.package': {
            'Meta': {'object_name': 'Package'},
            'author': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'backgroundImg': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'backgroundImgTile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'collaborators': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False', 'related_name': "'shared_packages'"}),
            'description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '256'}),
            'dublincore': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.DublinCore']", 'unique': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '50'}),
            'footer': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '100'}),
            'footerImg': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level1': ('django.db.models.fields.CharField', [], {'default': "'Topic'", 'max_length': '20'}),
            'level2': ('django.db.models.fields.CharField', [], {'default': "'Section'", 'max_length': '20'}),
            'level3': ('django.db.models.fields.CharField', [], {'default': "'Unit'", 'max_length': '20'}),
            'license': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50'}),
            'resourceDir': ('django.db.models.fields.files.FileField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'exeapp.pdfidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.Idevice'], 'object_name': 'PDFIdevice'},
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'modified_pdf_file': ('django.db.models.fields.FilePathField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'page_list': ('django.db.models.fields.CharField', [], {'blank': 'True', 'default': "''", 'max_length': '50'}),
            'pdf_file': ('filebrowser.fields.FileBrowseField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        },
        'exeapp.preknowledgeidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'PreknowledgeIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Preknowledge'", 'max_length': '100'})
        },
        'exeapp.readingactivityidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'ReadingActivityIdevice'},
            'activity': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'feedback': ('exeapp.models.idevices.fields.FeedbackField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Reading Activity'", 'max_length': '100'}),
            'to_read': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"})
        },
        'exeapp.reflectionidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'ReflectionIdevice'},
            'activity': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'answer': ('exeapp.models.idevices.fields.FeedbackField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Reflection'", 'max_length': '100'})
        },
        'exeapp.rssidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'RSSIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'rss_url': ('exeapp.models.idevices.fields.URLField', [], {'blank': 'True', 'default': "''", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'RSS'", 'max_length': '100'})
        },
        'exeapp.tocidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'TOCIdevice'},
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'})
        },
        'exeapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'related_name': "'profile'"})
        },
        'exeapp.wikipediaidevice': {
            'Meta': {'ordering': "('_order',)", '_ormbases': ['exeapp.GenericIdevice'], 'object_name': 'WikipediaIdevice'},
            'article_name': ('exeapp.models.idevices.fields.URLField', [], {'blank': 'True', 'default': "''", 'max_length': '100'}),
            'content': ('exeapp.models.idevices.fields.RichTextField', [], {'blank': 'True', 'default': "''"}),
            'idevice_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['exeapp.Idevice']", 'unique': 'True', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Wiki Article'", 'max_length': '100'})
        }
    }

    complete_apps = ['exeapp']
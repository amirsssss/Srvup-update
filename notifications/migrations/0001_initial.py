# Generated by Django 2.0.4 on 2018-04-14 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_object_id', models.PositiveIntegerField()),
                ('verb', models.CharField(max_length=255)),
                ('action_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('target_object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_action', to='contenttypes.ContentType')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('sender_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nofity_sender', to='contenttypes.ContentType')),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.ContentType')),
            ],
        ),
    ]

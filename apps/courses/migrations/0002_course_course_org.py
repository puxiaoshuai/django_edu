# Generated by Django 2.1.5 on 2019-01-29 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20190128_1120'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_Org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organization.CourseOrg', verbose_name='所属机构'),
        ),
    ]
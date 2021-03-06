# Generated by Django 3.1.5 on 2021-03-30 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkingGenie', '0006_merge_20210327_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['email', 'name']},
        ),
        migrations.RemoveField(
            model_name='account',
            name='accntType',
        ),
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='account',
            name='userType',
            field=models.PositiveSmallIntegerField(choices=[(1, 'customer'), (2, 'owner'), (3, 'manager'), (4, 'attendant')], default=1),
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20.0, help_text='Cost of a normal parking spot', max_digits=5),
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='tailgatePrice',
            field=models.DecimalField(decimal_places=2, default=30.0, help_text='Cost of a tailgate parking spot', max_digits=5),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(help_text='Email of the user', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkingLots', models.JSONField(help_text='List of this owners parking lots', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.account')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.account')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The long name of the event, with spaces', max_length=50)),
                ('shortName', models.CharField(help_text="Short event name, used when creating attendant 'email' addresses", max_length=15)),
                ('address', models.CharField(help_text='Address of the Event', max_length=100)),
                ('manager', models.ForeignKey(help_text='Manager who created the Event', on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.manager')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carMake', models.CharField(help_text='Make of the customers car', max_length=15)),
                ('carModel', models.CharField(help_text='Model of the customers car', max_length=15)),
                ('carColor', models.CharField(help_text='Color of the customers car', max_length=15)),
                ('carPlate', models.CharField(help_text='Licence plate of the customers car', max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.account')),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(help_text='Owner of above parking lot', on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.owner')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.account')),
            ],
        ),
        migrations.AddField(
            model_name='parkinglot',
            name='event',
            field=models.ManyToManyField(help_text='Event(s) that will use this parking lot', to='parkingGenie.Event'),
        ),
        migrations.AlterField(
            model_name='parkinglot',
            name='owner',
            field=models.ForeignKey(help_text='Owner of the parking lot', on_delete=django.db.models.deletion.CASCADE, to='parkingGenie.owner'),
        ),
    ]

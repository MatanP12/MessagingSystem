from django.db import migrations, transaction


class Migration(migrations.Migration):
    def generate_user_test_data(apps, schema_editor):
        from django.contrib.auth.models import User

        # Create a super user
        superuser = User()
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.username = 'admin'
        superuser.email = 'admin@gmail.com'
        superuser.set_password('admin1234')
        superuser.save()
        # Create normal users
        users_test_data = [
            ("MatanPeretz", "Matan", "Peretz", "matan1234","matan@gmail.com"),
            ("MotiLuchim", "Moti", "Luchim", "moti1234","moti@gmail.com"),
            ("KerenLaser", "Keren", "Laser", "keren1234","keren@gmail.com")
        ]

        with transaction.atomic():
            for USERNAME, FIRSTNAME, LASTNAME, PASSWORD, EMAIL in users_test_data:
                user = User(username=USERNAME, first_name=FIRSTNAME, last_name=LASTNAME, email=EMAIL)
                user.set_password(PASSWORD)
                user.save()
    operations = [
        migrations.RunPython(generate_user_test_data),
    ]

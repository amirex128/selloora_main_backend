from django_seed import Seed

from user.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        seeder.add_entity(User, 100, {
            'name': lambda x: seeder.faker.name(),
            'email': lambda x: seeder.faker.email(),
            'password': lambda x: seeder.faker.password(),
            'gender': lambda x: seeder.faker.random_element(elements=('man', 'woman')),
            'full_name': lambda x: seeder.faker.name(),
            'mobile': lambda x: seeder.faker.phone_number(),
            'expire_at': lambda x: seeder.faker.date(),
            'status': lambda x: seeder.faker.random_element(elements=('ok', 'block')),
            'verify_code': lambda x: seeder.faker.random_number(digits=6),
            'cart_number': lambda x: seeder.faker.random_number(digits=16),
            'shaba': lambda x: seeder.faker.random_number(digits=24),
            'is_admin': lambda x: seeder.faker.boolean(),
            'last_send_sms_at': lambda x: seeder.faker.date_time(),
            'profile_photo_path': lambda x: seeder.faker.image_url(),
            'created_at': lambda x: seeder.faker.date_time(),
            'updated_at': lambda x: seeder.faker.date_time(),
        })

        seeder.execute()

        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))


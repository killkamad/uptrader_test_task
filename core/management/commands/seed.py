from django.core.management.base import BaseCommand
from core.models import MenuItem


class Command(BaseCommand):
    help = 'Creates menu samples in the database'

    def handle(self, *args, **options):
        # Create some test samples
        if MenuItem.objects.filter(name='Menu').exists():
            self.stdout.write(self.style.ERROR('Menu already was created'))
            return

        root = MenuItem(name='Menu')
        root.save()

        games = MenuItem(name='Games', parent=root)
        games.save()

        action = MenuItem(name='Action Games', parent=games)
        action.save()

        rpg = MenuItem(name='RPG Games', parent=games)
        rpg.save()

        moba = MenuItem(name='MOBA', parent=games)
        moba.save()

        mmorpg = MenuItem(name='MMORPG Games', parent=rpg)
        mmorpg.save()

        shooter = MenuItem(name='Shooter Games', parent=games)
        shooter.save()

        strategy = MenuItem(name='Strategy Games', parent=root)
        strategy.save()

        turnbased = MenuItem(name='Turn-based Strategy Games', parent=strategy)
        turnbased.save()

        realtime = MenuItem(name='Real-time Strategy Games', parent=strategy)
        realtime.save()

        simulation = MenuItem(name='Simulation Games', parent=root)
        simulation.save()

        citybuilder = MenuItem(name='City-builder Games', parent=simulation)
        citybuilder.save()

        life = MenuItem(name='Life Simulation Games', parent=simulation)
        life.save()

        adventure = MenuItem(name='Adventure Games', parent=root)
        adventure.save()

        puzzle = MenuItem(name='Puzzle Games', parent=root)
        puzzle.save()

        dota2 = MenuItem(name='Dota 2', parent=moba)
        dota2.save()

        lol = MenuItem(name='LoL', parent=moba)
        lol.save()

        csgo = MenuItem(name='CS GO', parent=shooter)
        csgo.save()

        atomic_heart = MenuItem(name='Atomic Heart', parent=action)
        atomic_heart.save()

        call_of_duty = MenuItem(name='Call of Duty', parent=shooter)
        call_of_duty.save()

        wow = MenuItem(name='World of Warcraft', parent=mmorpg)
        wow.save()

        self.stdout.write(self.style.SUCCESS('Menu created successfully'))

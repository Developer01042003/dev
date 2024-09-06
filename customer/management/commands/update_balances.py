# customer/management/commands/update_balances.py

from django.core.management.base import BaseCommand
from customer.models import Persons, CampHistory, Withdraw_history
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Update user balances based on approved tasks and withdrawals'

    def handle(self, *args, **kwargs):
        yesterday = timezone.now() - timedelta(days=1)

        approved_tasks = CampHistory.objects.filter(is_verified=True, is_rejected=False, date__gte=yesterday)
        user_rewards = {}
        for task in approved_tasks:
            if task.email not in user_rewards:
                user_rewards[task.email] = 0
            user_rewards[task.email] += task.amount

        processed_withdrawals = Withdraw_history.objects.filter(is_verified=True, is_cancel=False, date_time__gte=yesterday)
        user_withdrawals = {}
        for withdrawal in processed_withdrawals:
            if withdrawal.email not in user_withdrawals:
                user_withdrawals[withdrawal.email] = 0
            user_withdrawals[withdrawal.email] += withdrawal.amount

        for email, reward in user_rewards.items():
            user = Persons.objects.filter(email=email).first()
            if user:
                user.wallet += reward
                user.save()

        for email, withdrawal in user_withdrawals.items():
            user = Persons.objects.filter(email=email).first()
            if user:
                user.wallet -= withdrawal
                user.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated user balances'))

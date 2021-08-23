from rest_framework import serializers
from .models import user_account,transfer
#from .forms import transferForm
from django.contrib.auth.models import User
from transfer.settings import logger

class user_accountSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_account
        fields = '__all__'
    
    def create(self,validated_data):
        username = validated_data.get('user').username
        TIN = validated_data.get('TIN')
        invoice = validated_data.get('invoice')
        logger.info(f'New user_account has been created.\n  \
                    Account Info: username: {username}- TIN:{TIN} - invoice: {invoice}')

        return user_account.objects.create(**validated_data)


class transferSerializer(serializers.ModelSerializer):
    def get_users_names():
        users = user_account.objects.all()
        users_names = []
        for u in users:
            users_names.append((u.TIN,u.user.username))
        return users_names

    transfer_From = serializers.ChoiceField(choices = get_users_names() )

    class Meta:
        model = transfer
        fields = ['transfer_From','transfer_To_TIN','amount_money']

    def create(self,validated_data):
        transfer_From_User = user_account.objects.filter(TIN = validated_data.get('transfer_From'))[0]
        transfer_To_TINS = [int(num) for num in validated_data.get('transfer_To_TIN').split(',')]
        transfer_To_Users = user_account.objects.filter(TIN__in = transfer_To_TINS)
        amount_money = validated_data.get('amount_money')
        amount_forUser = amount_money/len(transfer_To_Users)
        transfer_From_User.invoice -= amount_money
        transfer_From_User.save()
        for user in transfer_To_Users:
            user.invoice += amount_forUser
            user.save()
        transfer_To_UsersTINS = [u.TIN for u in transfer_To_Users]
        logger.info(f'The transfer operation has done.\n  \
                            {amount_money} has been transfered from {transfer_From_User.TIN} to {transfer_To_UsersTINS}')

        return transfer.objects.create(**validated_data)

    def validate(self, data):
        user_transfer_From = user_account.objects.filter(TIN = data['transfer_From'])[0]
        #TINS_transfer_To = validated_data.get('transfer_To_TIN')
        TINS_transfer_To = [int(num) for num in data['transfer_To_TIN'].split(',')]
        accounts = user_account.objects.all()
        accounts_TINS = [account.TIN for account in accounts]
        check_TINS = True if all(tin in accounts_TINS for tin in TINS_transfer_To) else False

        if not check_TINS:
            raise serializers.ValidationError('the TINS aren\'t valid')

        amount_money = data['amount_money']
        print(f'################# from:{user_transfer_From} to:{TINS_transfer_To} :{amount_money}')
        if user_transfer_From.invoice > amount_money:
            return data
        else:
            raise serializers.ValidationError('the user has\'t the amount of money')

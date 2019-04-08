from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from core import models


class IndexPageView(View):
    def get(self, request):
        # total amount takes 28 rowrequest.session.get('user_id')
        total_amount = request.session.get('total_amount')

        last_amount = request.session.get('for_message')
        name_for_message = request.session.get('name_for_message')


        if last_amount:
            request.session.pop('for_message')

        return render(request, 'index_page.html', {
            'total_amount': total_amount,
            'last_amount': last_amount,
            'name_for_message': name_for_message

        })


class Pay(View):
    def get(self, request, amount):
        print(request.session)
        #в сесію під назвою тотал емаунт записую значення. тотал то моя назва її ніде нема
        request.session['total_amount'] = request.session.get('total_amount', 0) + amount

        request.session['for_message'] = amount

        #з сесії берется юзер айді. передається в базу дних щоб знайти по цьому айді і результат передаєтьсся в юзер !!!!!!!
        user = models.User.objects.get(id=request.session['user_id'])

        user_amount = models.Amount(amount=amount, user_id=user)
        user_amount.save()

        return redirect('/')


class SignUp(View):
    def get (self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        print(request.POST)

        login = request.POST['email']
        password = request.POST['password']

        if not models.User.objects.filter(login=login, password=password):

            new_user = models.User(login=login, password=password)
            new_user.save()
        else:
            does_exist_login = login
            return render(request, 'index_page.html', {
            'does_exist_login': does_exist_login,


        })



        #нижній рядок взагалі для того щоб коли людина зареєстувалась щоб не приходилось логінитись
        request.session['user_id'] = new_user.id
        # юзер айді то моя придумана назва а new user я витягую з створеного нев юзер з попереднього рядка (назва крапка для переходу по властивості (айді логін пароль

        request.session['name_for_message'] = login
        # name_for_message = request.session.get('name_for_message')

        #сесіями можна користуватись в різних вюхах. я роблю редірект на іншу вюху того мені це требв

        return redirect('/')

class Exit(View):
    def get (self, request):

        if request.session.get('user_id'):
            #бо це дікшинарі* не так само як на темплейті
            request.session.pop('user_id')

        return render(request, 'index_page.html')

class Login(View):
    def get(self, request):
        print('1111 ', request.session.get('user_id'))

        if request.session.get('user_id'): # get returns value or None if not exists
            print('0000 ',request.session.get('user_id'))

            return redirect('/')

        return render(request, 'login_page.html')

    def post(self, request):
        input_login = request.POST['email']  # post це властивість. request is an object. it has post. post is a dict
        input_password = request.POST['password']

        try:
            new_user = models.User.objects.get(login=input_login, password=input_password)

        except models.User.DoesNotExist as e:
            return HttpResponse('user doesnt exist')

        #нижній рядок треба треба щоб верхній рядок нев юзер світився тобто десь використовувався
        #я придумала назву ключа 'user_id' і в нього записую змінну  new_user і беру з того його айді (.id_)
        #потім цей рядок викорстовую в вюсі Пей щоб витягути юзер айді
        request.session['user_id'] = new_user.id



        return redirect('/')

class Features(View):
    def get(self, request):




        request.session['sraka'] = '123'

        return HttpResponse(request.session['sraka'])


class About(View):
    def get(self, request):


        try:
            sraka = request.session['sraka']
        except:
            return HttpResponse('шнема такого клюяа ')

        return HttpResponse(sraka)


class History(View):
    def get(self, request, ):

        #берется з сесї. при реєстраії записується в сесію юзер айді
        # це було записано в логіні в нев юзер айді
        #user_id = request.session.get('user_id')

        #йді = попеедньому ядку
        # user = models.User.objects.get(id=user_id)

        #user повертає ціли обєкт і він передається в амагнт як обєкті2

        #то що юзеер айді айді в базі даних то в нижньому рядку юзер айді
        #amounts = models.Amount.objects.filter(user_id=user)

        amounts = models.Amount.objects.all()
        list_of_amounts = []
        for amount in amounts:
            list_of_amounts.append(amount.__dict__)

        return HttpResponse(str(list_of_amounts))






from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth import authenticate,login,logout # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.http import HttpResponse # type: ignore
from .models import *
from django.contrib.auth.decorators import login_required # type: ignore


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        upi = request.POST['upi']

        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already exists')
        
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already Exists')

        Persons.objects.create(username=username,email=email,password=password,upi=upi)
        user = User.objects.create_user(username,email,password)
        
        
        user.save()
        return redirect('login')

    return render(request,'register.html')

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,"login.html")

@login_required
def newCamps(request):
    
    camps = LatestCamp.objects.filter(is_active=True)
    return render(request,"camps.html",{'tasks':camps})

@login_required
def handle_task_click(request, id):
    task = LatestCamp.objects.get(id=id)

    if task:
        
        email = request.user.email
        
        
        links = task.link.format(username=request.user.username)

        pastCamp = CampHistory.objects.filter(link=links)

        if pastCamp:
            return redirect(links)
        
        else:
            CampHistory.objects.create(
        email = request.user.email,
        name = task.name,
        link = links,
        amount = task.amount,
        ),
            return redirect(links)
    else:
        
        return HttpResponse("May be the campaign is closed!")
        

@login_required 
def redirectit(request,id):
    if id:
        Camps = LatestCamp.objects.get(id=id)



        pastCamp = CampHistory.objects.filter()

        if Camps:
            link = Camps.link
            CampHistory.objects.create(
                email = request.user.email,
                link = link,
                amount=Camps.amount,
                name=Camps.name,
            )
            return redirect(link)
        else:
            return HttpResponse("some error occured!")
        
    else:
        return HttpResponse("Some error occured !")



def passwordreset(request):
    pass


@login_required
def logout_view(request):
    logout(request)  # This logs out the user by flushing their session.
    return redirect('login')


@login_required()
def profile(request):
    user_email = request.user.email
    user_check = Persons.objects.filter(email=user_email)

    if user_check is not None:
        print('helo')
        user_data = Persons.objects.get(email=user_email)
        context = {
            'username': user_data.username,
            'amount':user_data.wallet
        }
        
        return render(request,'home.html',context)
    else:
        return redirect('login')
        



@login_required
def payout(request):
    user_e = request.user.email
    _user_main = Persons.objects.get(email=user_e)
    wallet_b = _user_main.wallet
    

    # If not a POST request, render the wallet page
    return render(request, 'wallet.html', {'user_balance':wallet_b})

   





@login_required
def withdraw_balance(request):
    user_e = request.user.email

    if request.method == 'POST':
        amount = int(request.POST['amount'])
        if user_e:
            try:
                _user = Persons.objects.get(email=user_e)
                _wallet_balance = _user.wallet

                if _wallet_balance >= amount:
                    new_balance = _wallet_balance - amount
                    _user.wallet = new_balance
                    _user.save()

                    Withdraw_history.objects.create(email=user_e,amount=amount)

                    # HTMX response to update balance and show success message
                    response = f"""
                    <div id="message-container" class="success-message">
                        Withdrawal of ₹{amount} was successful!
                    </div>
                    <script>
                        document.getElementById('balance-container').innerText = '₹{new_balance}';
                    </script>
                    """

                    return HttpResponse(response, status=200)
                else:
                    # Insufficient balance error message
                    error_message = """
                    <div id="message-container" class="success-message" style="color: red;">
                        Insufficient balance for this withdrawal!
                    </div>
                    """
                    return HttpResponse(error_message, status=400)
            except Persons.DoesNotExist:
                # User not found error message
                error_message = """
                <div id="message-container" class="success-message" style="color: red;">
                    User not found. Please try again.
                </div>
                """
                return HttpResponse(error_message, status=404)
        else:
            # General error message
            error_message = """
            <div id="message-container" class="success-message" style="color: red;">
                An error occurred. Please try again.
            </div>
            """
            return HttpResponse(error_message, status=400)
    else:
        # Invalid request method error message
        error_message = """
        <div id="message-container" class="success-message" style="color: red;">
            Invalid request method.
        </div>
        """
        return HttpResponse(error_message, status=405)



@login_required
def task_record(request):
    email = request.user.email

    task = CampHistory.objects.filter(email=email)

    if task :
         return render(request,"history.html",{'get_data':task})
    else:
        return render(request,"history.html",{'get_data':None})


    



@login_required
def withhistory(request):
    email = request.user.email

    transactions = Withdraw_history.objects.filter(email=email)

    if transactions is not None:
    
      
      return render(request, 'withdrawhistory.html',{'get_data':transactions} )
    
    


def customer_service(request):
    telegram_link = "https://t.me/Publisher_support"

    return redirect(telegram_link)
               
def Monetize_us(request):

    form_link = "https://forms.gle/6rrJyPLkJSVsijet6"
    return redirect(form_link)


def payment_page(request):
    pass



def notice_board(request):
    notices = Notice.objects.all().order_by('-created_at')  # Fetch all notices ordered by creation date
    return render(request, 'notice.html', {'notices': notices})
                   
                   





from django.shortcuts import render
from .models import InfoForPage, Projects
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main_app/index.html')


def user_page(request, name):
    first_name, last_name = name.split('_')
    client_info = InfoForPage.objects.get(first_name=first_name, last_name=last_name)
    client_projects = Projects.objects.filter(user=client_info.user).all()



    return render(request, f'ready_made_templates/{client_info.template_name}.html', context={'client_info': client_info,
                                                                                  'client_projects': client_projects})

@login_required
def create_page(request):

    if request.method == 'POST':
        user_picture = request.FILES.get('user_picture')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        type_of_activity = request.POST.get('type_of_activity')
        about = request.POST.get('about')
        mail = request.POST.get('mail')
        instagram = request.POST.get('instagram')
        telegram = request.POST.get('telegram')
        tiktok = request.POST.get('tiktok')
        facebook = request.POST.get('facebook')
        tel = request.POST.get('tel')
        template_name = request.POST.get('template_name')

        texts = request.POST.getlist('text')
        image_urls = request.FILES.getlist('image')



        InfoForPage.objects.create(user=request.user,
                                   user_picture=user_picture,
                                   first_name=first_name,
                                   last_name=last_name,
                                   type_of_activity=type_of_activity,
                                   about=about,
                                   mail=mail,
                                   instagram=instagram,
                                   telegram=telegram,
                                   tiktok=tiktok,
                                   facebook=facebook,
                                   tel=tel,
                                   template_name=template_name)

        for text, image_url in zip(texts, image_urls):
            Projects.objects.create(user=request.user, text=text, image_url=image_url)

    return render(request, 'main_app/create_template.html')
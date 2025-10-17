from django.shortcuts import render, redirect
from .models import InfoForPage, Projects
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main_app/index.html')


@login_required
def user_page(request, name):
    result = name.replace(" ", "")
    first_name, last_name = result.split('_')
    client_info = InfoForPage.objects.get(first_name=first_name, last_name=last_name)
    client_projects = Projects.objects.filter(user=client_info.user).all()
    return render(request, f'ready_made_templates/{client_info.template_name}.html', context={'client_info': client_info,
                                                                                  'client_projects': client_projects})

@login_required
def create_page(request):

    try:
        info = InfoForPage.objects.get(user=request.user)
    except InfoForPage.DoesNotExist:
        info = None

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

        if info is None:
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
        else:
            Projects.objects.filter(user=request.user).delete()
            InfoForPage.objects.filter(user=request.user).delete()

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
        return redirect('cabinet')

    return render(request, 'main_app/create_template.html')

@login_required
def cabinet(request):
    user = request.user
    try:
        client_info = InfoForPage.objects.get(user=user)
        url_page = f'{client_info.first_name}_{client_info.last_name}'
    except InfoForPage.DoesNotExist:
        client_info = None
        url_page = None

    try:
        client_projects = Projects.objects.filter(user=user).all()
    except Projects.DoesNotExists:
        client_projects = None

    context = {
        'user': user,
        'client_info': client_info,
        'client_projects': client_projects,
        'url_page': url_page
    }

    return render(request, 'main_app/cabinet.html', context)


def bill_gates(request):
    client_info = {}
    client_projects = [
        {'text': 'Microsoft: In 1975, he co-founded Microsoft with Paul Allen.', 'image_url': {'url': 'media/uploads/bill_gates/microsoft.jpeg'}},
        {'text': 'Bill & Melinda Gates Foundation: Founded a charitable foundation that is one of the largest in the world.Microsoft: In 1975, he co-founded Microsoft with Paul Allen.', 'image_url': {'url': 'media/uploads/bill_gates/maxresdefault.jpg'}},
        {'text': 'Access to Clean Water: Invests in projects to provide access to drinking water in developing countries.Microsoft: In 1975, he co-founded Microsoft with Paul Allen.', 'image_url': {'url': 'media/uploads/bill_gates/how-can-we-improve-access-1.jpg'}}
    ]


    client_info['user_picture'] = {'url': 'media/uploads/bill_gates/bill.jpg'}
    client_info['first_name'] = 'Bill'
    client_info['last_name'] = 'Gates'
    client_info['type_of_activity'] = 'American business magnate, philanthropist, co-founder of Microsoft, and a leading figure in the personal computer revolution'
    client_info['about'] = 'Investor: Through Cascade Investment, he remains a major investor in various companies and is the director of Berkshire Hathaway. Author: He has co-authored several books, including How to Avoid a Climate Disaster and Business @ the Speed of Thought. Lifestyle: He is known for his interest in exercise and is a big reader.'
    client_info['mail'] = 'bill_gates@icloud.com'
    client_info['instagram'] = '@bill_gates'
    client_info['tiktok'] = '@bill_gates'
    client_info['facebook'] = '@bill_gates'
    client_info['tel'] = '11111111111111'

    return render(request, f'ready_made_templates/1.html', context={'client_info': client_info,
                                                                                         'client_projects': client_projects})

def curtis_james_jackson(request):
    client_info = {}
    client_projects = [
        {"text": "Debut and shooting: Jackson's first album, Power of the Dollar, was never released after he was shot nine times days before its scheduled release in 2000.", "image_url": {"url": "media/uploads/fiftic/album.jpg"}},
        {"text": "Discovery and major success: After being discovered by Eminem and signing with Shady Records, his 2003 major-label debut, Get Rich or Die Tryin', and his 2005 follow-up, The Massacre, became massive commercial successes.", "image_url": {"url": "media/uploads/fiftic/eminem.webp"}},
        {"text": "Record label: In 2003, he founded G-Unit Records, signing artists like Young Buck, Lloyd Banks, and Tony Yayo.", "image_url": {"url": "media/uploads/fiftic/g.jpg"}}
    ]


    client_info['user_picture'] = {'url': 'media/uploads/fiftic/fiftic.jpg'}
    client_info['first_name'] = 'Curtis James'
    client_info['last_name'] = 'Jackson III'
    client_info['type_of_activity'] = 'Grammy-winning American rapper, actor, and producer'
    client_info['about'] = 'Early life: He was born in Queens, New York, and was raised by his grandmother after his mother, a drug dealer, was murdered when he was eight years old.'\
                            'Name origin: He adopted the stage name 50 Cent from a 1980s Brooklyn criminal named Kelvin Martin. He chose the name to symbolize his ability to provide for himself by any means necessary.'\
                            'Criminal past: Before his music career took off, Jackson was involved in drug dealing and served time in a boot camp for drug possession.'\
                            'Acting and entrepreneurship: He is also an actor and has appeared in a variety of films, including the biographical film Get Rich or Die Tryin. He has also been involved in other ventures, including a successful beverage and clothing brand'
    client_info['mail'] = '50cent@icloud.com'
    client_info['instagram'] = '@b51cent'
    client_info['tiktok'] = '@52cent'
    client_info['facebook'] = '@53cent'
    client_info['tel'] = '+34543575789999'

    return render(request, f'ready_made_templates/2.html', context={'client_info': client_info,
                                                                                         'client_projects': client_projects})

def leonardo_dicaprio(request):
    client_info = {}
    client_projects = [
        {"text": "Breakthrough: Began with roles in television and films like This Boy's Life (1993) and What's Eating Gilbert Grape (1993), the latter earning him his first Academy Award nomination.", "image_url": {"url": "media/uploads/leo/first.jpg"}},
        {"text": "Superstardom: Became a global heartthrob after starring in the box-office smash Titanic (1997).", "image_url": {"url": "media/uploads/leo/titanic.jpg"}},
        {"text": "Collaborations: Has frequently collaborated with director Martin Scorsese, including films such as Gangs of New York (2002), The Departed (2006), and The Wolf of Wall Street (2013)", "image_url": {"url": "media/uploads/leo/prem.webp"}}
    ]


    client_info['user_picture'] = {'url': 'media/uploads/leo/leonardo.jpg'}
    client_info['first_name'] = 'Leonardo'
    client_info['last_name'] = 'DiCaprio'
    client_info['type_of_activity'] = 'Highly acclaimed American actor and producer known for his roles in films like Titanic, The Revenant, and Once Upon a Time in Hollywood'
    client_info['about'] = "Founder: Established the Leonardo DiCaprio Foundation in 1998 to raise awareness about environmental issues."\
                "UN Messenger: Is a United Nations Messenger of Peace for climate change."\
                "Media projects: Produced documentary films like The 11th Hour (2007) and Before the Flood (2016) to highlight climate change."\
                "Board member: Serves on the boards of several environmental organizations, including the World Wildlife Fund and the Natural Resources Defense Council. "
    client_info['mail'] = 'leonardo_dicaorio@icloud.com'
    client_info['instagram'] = '@dicaorio'
    client_info['tiktok'] = '@dicaorio'
    client_info['facebook'] = '@dicaorio'
    client_info['tel'] = '+77777474777'

    return render(request, f'ready_made_templates/3.html', context={'client_info': client_info,
                                                                                         'client_projects': client_projects})

def homer_jay_simpson(request):
    client_info = {}
    client_projects = [
        {"text": "Homer can easily do somersaults, survives beatings without any consequences, and recovers quickly from car accidents. He's thrown people with ease many times. He's a solid average fighter – he'll punch as much as he gets punched in the face, assuming it's a one-on-one fight. But more often than not, he's attacked in a crowd.", "image_url": {"url": "media/uploads/gomer/one.png"}},
        {"text": "Homer, like almost all the male Simpsons, is officially mentally disabled. His behavior isn't simply a result of his upbringing or a bad temper; it's a genetic defect. However, this doesn't correspond to any specific diagnosis in the real world. Despite this, Homer is capable of displaying remarkable ingenuity, intuition, and good behavior to get his hands on food or beer. He can also be quite resourceful in extreme situations.", "image_url": {"url": "media/uploads/gomer/two.jpg"}},
        {"text": "Despite all his shortcomings, Homer clearly has musical talent; in his youth, he played in several bands and even won a Grammy. He also became (albeit briefly) an opera singer – a tenor – and even tried to give singing advice to the renowned Placido Domingo.", "image_url": {"url": "media/uploads/gomer/three.jpg"}}
    ]


    client_info['user_picture'] = {'url': 'media/uploads/gomer/HS.jpg'}
    client_info['first_name'] = 'Homer Jay'
    client_info['last_name'] = 'Simpson'
    client_info['type_of_activity'] = 'Low-level safety inspector at the Springfield'
    client_info['about'] = "He is a crude, ignorant, and slobbish individual, although he is fundamentally a good person and shows great caring and loyalty to his family, friends and on occasion, to those he barely knows or those he considers his enemies."
    client_info['mail'] = "D'oh!@icloud.com"
    client_info['instagram'] = "D'oh!"
    client_info['tiktok'] = "D'oh!"
    client_info['facebook'] = "D'oh!"
    client_info['tel'] = '+00000000000000'

    return render(request, f'ready_made_templates/4.html', context={'client_info': client_info,
                                                                                         'client_projects': client_projects})


def matthew_david_mcconaughey(request):
    client_info = {}
    client_projects = [
        {"text": "He won an Academy Award for Best Actor and a Golden Globe for his role in Dallas Buyers Club.", "image_url": {"url": "media/uploads/met/oskar.jpg"}},
        {"text": "In a November 2020 appearance on The Late Show with Stephen Colbert, McConaughey denied he was interested in running for governor. The Texas Tribune reported on McConaughey's lack of involvement in politics, saying that he had not voted in a primary race since at least 2012 and had never donated to a political campaign at the state or federal level up through 2021. He had voted in the 2018 Texas elections and the 2020 United States elections.", "image_url": {"url": "media/uploads/met/white_house.png"}},
        {"text": "McConaughey started the 'just keep livin foundation', which is 'dedicated to helping teenage kids lead active lives and make healthy choices to become great men and women'. On February 25, 2016, McConaughey received the Creative Conscience award from humanity for his work with his foundation.", "image_url": {"url": "media/uploads/met/philant.jpg"}}
    ]


    client_info['user_picture'] = {'url': 'media/uploads/met/met.jpg'}
    client_info['first_name'] = 'Matthew'
    client_info['last_name'] = 'David McConaughey'
    client_info['type_of_activity'] = 'American actor'
    client_info['about'] = "He is known for his breakthrough role in Dazed and Confused (1993), his dramatic turn in Dallas Buyers Club (2013), for which he won an Academy Award for Best Actor, and his lead role in the TV series True Detective. McConaughey has also starred in romantic comedies and numerous other films, and is married to Camila Alves, with whom he has three children."
    client_info['mail'] = "McConaughey@icloud.com"
    client_info['instagram'] = "@McConaughey"
    client_info['tiktok'] = "@McConaughey"
    client_info['facebook'] = "@McConaughey"
    client_info['tel'] = '+45666666677777'

    return render(request, f'ready_made_templates/5.html', context={'client_info': client_info,
                                                                                         'client_projects': client_projects})
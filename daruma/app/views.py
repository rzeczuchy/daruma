from django.shortcuts import render
from .forms import ContactForm
from .models import *
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.http import HttpResponseServerError

# Create your views here.
def index(request):
    home = Home.objects.first()
    company_detail = CompanyDetail.objects.first()
    contact_form = ContactForm()
    team_members = TeamMember.objects.all()[:3]
    partner_logos = PartnerLogo.objects.all()

    context = {
        'home': home,
        'ptitle': home.title,
        'pdescription': home.meta_description,
        'cdetail': company_detail,
        'cform': contact_form,
        'tmembers': team_members,
        'plogos': partner_logos,
    }
    return render(request, 'app/index.html', context)

def team(request):
    company_detail = CompanyDetail.objects.first()
    team_members = TeamMember.objects.all()

    context = {
        'ptitle': 'ABCD | Team',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
        'tmembers': team_members,
    }
    return render(request, 'app/team.html', context)

def blog(request):
    company_detail = CompanyDetail.objects.first()
    post_list = Post.objects.order_by('-published_time')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'ptitle': 'ABCD | Blog',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
        'page_obj': page_obj
    }
    return render(request, 'app/blog.html', context)

class PostDetail(DetailView):
    model = Post
    template_name = 'app/post.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['cdetail'] = CompanyDetail.objects.first()
            context['ptitle'] = 'ABCD | Blog'
            context['pdescription'] = 'Meta description for this page'
            return context

def privacy(request):
    company_detail = CompanyDetail.objects.first()
    privacy_policy = PrivacyPolicy.objects.first()
    context = {
        'ptitle': 'ABCD | Privacy Policy',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
        'pobject': privacy_policy
    }
    return render(request, 'app/simple.html', context)

def terms(request):
    company_detail = CompanyDetail.objects.first()
    terms_of_service = TermsOfService.objects.first()
    context = {
        'ptitle': 'ABCD | Terms of Service',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
        'pobject': terms_of_service
    }
    return render(request, 'app/simple.html', context)

def disclaimer(request):
    company_detail = CompanyDetail.objects.first()
    disclaimer = Disclaimer.objects.first()
    context = {
        'ptitle': 'ABCD | Disclaimer',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
        'pobject': disclaimer
    }
    return render(request, 'app/simple.html', context)

def send_inquiry(request):
    company_detail = CompanyDetail.objects.first()
    context = {
        'ptitle': 'ABCD | Inquiry sent',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            i = Inquiry(name=cd['name'], email=cd['email'], message=cd['message'])
            i.save()
        
    return render(request, 'app/thanks.html', context)

def handler404(request, exception):
    company_detail = CompanyDetail.objects.first()
    context = {
        'ptitle': 'ABCD | Page not found',
        'pdescription': 'Meta desciption for this page',
        'cdetail': company_detail,
    }
    return render(request, 'app/404.html', context)
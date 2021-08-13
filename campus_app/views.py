from django.urls import reverse_lazy
from .models import Noticia, WhatsAppAccount
from django.contrib.auth.models import Group
from .forms import NoticiaForm, WhatsAppAccountCreateForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.dates import DayArchiveView
import datetime


class HomeView(TemplateView):

    template_name = "campus_app/home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')[:20]
        context['data'] = datetime.date.today()
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class NoticiaDataView(DayArchiveView):

    template_name = "campus_app/noticia_archive_day.html"
    date_field = "dia_publicacao"
    queryset = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')
    allow_future = True
    allow_empty = True

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        queryset = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')
        context['noticias'] = queryset
        context['data'] = datetime.date(self.get_year(), self.get_month(), self.get_day())
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class NoticiaView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):

    permission_required = 'campus_app.view_noticia'
    template_name = "campus_app/noticia_list.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-data_publicacao').all
        context['perfil'] = Group.objects.filter(user = self.request.user)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

      
class NoticiaCreate(LoginRequiredMixin, PermissionRequiredMixin, FormView):

    permission_required = 'campus_app.add_noticia'
    template_name = 'campus_app/noticia_form.html'
    form_class = NoticiaForm
    success_url = reverse_lazy('noticia_list')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NoticiaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'campus_app.change_noticia'
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticia_list')
    template_name = 'campus_app/noticia_update_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class NoticiaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    
    permission_required = 'campus_app.delete_noticia'
    model = Noticia
    success_url = reverse_lazy('noticia_list')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


###################################### WhatsApp Account Views ######################################


class WhatsAppAccountView(TemplateView):

    template_name = "campus_app/whatsapp_account_list.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['whatsapp_accounts'] = WhatsAppAccount.objects.all()
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


class WhatsAppAccountCreate(FormView):

    model = WhatsAppAccount
    template_name = 'campus_app/whatsapp_account_create_form.html'
    form_class = WhatsAppAccountCreateForm
    success_url = reverse_lazy('whatsapp_account_list')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

        context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context

    def form_valid(self, form):

        form.save()

        return super().form_valid(form)
        

class WhatsAppAccountUpdate(UpdateView):
    
    model = WhatsAppAccount
    form_class = WhatsAppAccountCreateForm
    success_url = reverse_lazy('whatsapp_account_list')
    template_name = 'campus_app/whatsapp_account_update_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'
    
        return context

    def form_valid(self, form):
        
        form.save()

        return super().form_valid(form)


class WhatsAppAccountDelete(DeleteView):

    model = WhatsAppAccount
    success_url = reverse_lazy('whatsapp_account_list')
    template_name = 'campus_app/whatsapp_account_delete_confirmation.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        record = WhatsAppAccount.objects.order_by('-cod')[:1]
        number = None
        context['whatsapp'] = None

        if record:

            number = record[0]

            context['whatsapp'] = 'https://wa.me/' + str(number) + '?text=Ol%C3%A1,%20peguei%20esse%20n%C3%BAmero%20no%20App%20Campus%20Online'

        return context


from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Project
from utils.secure_utils import generate_nonce, create_csp

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/feed.html'
    context_object_name = 'projects'
    paginate_by = 8

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset.order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'nonce': generate_nonce()
        })

        return context
    
    def get(self, request, *args, **kwargs):
        request.session['previous_posts_page'] = request.get_full_path()
        return super().get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Security-Policy'] = create_csp(context['nonce'])
        return response


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/single_project.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'return_url': self.request.session.get('previous_projects_page', '/projects/'),
            'nonce': generate_nonce()
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Security-Policy'] = create_csp(context['nonce'])
        return response
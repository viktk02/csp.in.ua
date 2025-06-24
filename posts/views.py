from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Post
from .validators import dates_validator
from utils.secure_utils import generate_nonce, create_csp

class PostListView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self):
        queryset = Post.objects.all()
        self.invalid_date_range = False

        sort_by = self.request.GET.get('sort', '-date_posted')
        allowed_fields = ['date_posted', '-date_posted', 'title', '-title', 'author']

        if sort_by not in allowed_fields:
            sort_by = '-date_posted'

        search_query = self.request.GET.get('q','')[:100]
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(preview_text__icontains=search_query) |
                Q(author__icontains=search_query)
            ).distinct()

        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')


        if not dates_validator(date_from, date_to):
            self.invalid_date_range = True
            return queryset.order_by(sort_by)

        if date_from:
            queryset = queryset.filter(date_posted__gte=date_from)
        if date_to:
            queryset = queryset.filter(date_posted__lte=date_to)

        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'current_sort': self.request.GET.get('sort', '-date_posted'),
            'search_query': self.request.GET.get('q', ''),
            'date_from': self.request.GET.get('date_from', ''),
            'date_to': self.request.GET.get('date_to', ''),
            'invalid_date_range': getattr(self, 'invalid_date_range', False),
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



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/single_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'return_url': self.request.session.get('previous_posts_page', '/posts/'),
            'nonce': generate_nonce()
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response['Content-Security-Policy'] = create_csp(context['nonce'])
        return response
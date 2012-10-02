from dateutil import parser
from devotionals.models import Devotional
from django.views.generic.base import TemplateView

class DevotionalTemplateView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        _context = TemplateView.get_context_data(self, **kwargs)
        _date_str = self.kwargs.get('date')
        _current_date = parser.parse(_date_str)
        
        _result = Devotional.objects.filter(month = _current_date.month, day = _current_date.day)
        
        if len(_result) > 0:
            _context.setdefault('object', _result[0])
    
        return _context
    
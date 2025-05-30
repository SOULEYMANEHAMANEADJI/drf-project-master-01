import django_filters

from employees.models import Employee


class EmployeeFilter(django_filters.FilterSet):

    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_gender = django_filters.CharFilter(field_name='emp_gender', lookup_expr='iexact')
    # emp_id = django_filters.RangeFilter(field_name='emp_id')
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From EMP NINEA')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To EMP NINEA')

    class Meta:
        model = Employee
        fields = ['emp_name', 'designation', 'emp_gender']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(ninea__gte=value)
        elif name == 'id_max':
            return queryset.filter(ninea__lte=value)
        return queryset
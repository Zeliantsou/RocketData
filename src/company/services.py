from django.db.models import Avg, QuerySet
from rest_framework.exceptions import ValidationError

from company.models import Company


def validate_company_data(data: dict) -> None:
    company_type = data.get('type')
    shipper = data.get('shipper')
    city = data.get('city')
    country = data.get('country')

    if shipper and ((company_type == 0) or (company_type <= shipper.type)):
        raise ValidationError(
            detail='Company type can not be less than or equal shipper type'
        )

    if not city or not country or city.country != country:
        raise ValidationError(detail='City does not match country')


def get_companies_with_debt_more_avg() -> QuerySet:
    average_debt = Company.objects.aggregate(Avg('debt'))

    return Company.objects.filter(debt__gt=average_debt.get('debt__avg'))

from rest_framework.exceptions import ValidationError


def validate_company_data(data):
    company_type = data.get('type')
    shipper = data.get('shipper')
    city = data.get('city')
    country = data.get('country')

    if shipper and ((company_type == 0) or (company_type <= shipper.type)):
        raise ValidationError(detail='Company type can not be less than or equal shipper type')

    if not city or not country or city.country != country:
        raise ValidationError(detail='City does not match country')

import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

COMPARATOR = {
    ">": "=gt",
    "<": "=lt",
    ">=": "=gte",
    "<=": "=lte",
    "=": "=",
}
PHY_TYPES = [
    ("stars", "star"),
    ("galaxies", "galaxy"),
    ("interstellar matter", "interstellar_matter")
    ]
PHY_CRT = ['plx', 'mes', 'vmag', 'redshift']
URL = 'http://api.skywatch.co'


def validate_string(search_string):
    """
    Small string search validation
    :param search_string: string to be validated
    :return:
    """
    if search_string == "":
        return False

    exist_phy_types = False
    for tuple in PHY_TYPES:
        if tuple[0] in search_string:
            exist_phy_types = True
            break

    exist_phy_criterias = False
    for item in PHY_CRT:
        if item in search_string:
            exist_phy_criterias = True
            break

    if exist_phy_types:
        return True

    if exist_phy_criterias:
        return True

    return False


def query_api(search_string):
    """
    Convert string literal to string search url
    :param search_string: string to be converted into string search url
    :return: search url
    """

    if not validate_string(search_string):
        return ""
    #removing with and and,
    #only grouping by category is sufficient to create a search string
    if "with " in search_string:
        search_string = search_string.replace("with ", "")
    if "and " in search_string:
        search_string = search_string.replace("and ", "")

    #replacing to singular
    for tuple in PHY_TYPES:
        if tuple[0] in search_string:
            search_string = search_string.replace(tuple[0], tuple[1])

    #categorizing items into physical types and criteria
    physical_types = []
    criteria = []
    for item in search_string.split(" "):
        item = item.replace(",", "")
        if item in [tuple[1] for tuple in PHY_TYPES]:
            physical_types.append(item)
        else:
            criteria.append(item)

    #generating types string
    str_response = "types=" if len(physical_types) > 0 else ""
    for item in physical_types:
        item = item.replace(" ", "")
        if physical_types.index(item) == 0:
            str_response = "{}{}".format(str_response, item)
        else:
            str_response = "{}+{}".format(str_response, item)

    if len(criteria) > 0 and len(physical_types) > 0:
        str_response = "{}&".format(str_response)

    #generating criterias string
    for item in criteria:
        if criteria.index(item) == 0:
            str_response = "{}{}".format(str_response, item)
        elif item in PHY_CRT:
            str_response = "{}&{}".format(str_response, item)
        elif item in COMPARATOR:
            str_response = "{}{}".format(str_response, COMPARATOR[item])
        else:
            str_response = "{}{}".format(str_response, item)

    full_string = ""
    #generating full string
    if len(str_response) > 0:
        full_string = "{}/?{}".format(URL, str_response)

    return full_string


def is_url_valid(url):
    return regex.match(url)


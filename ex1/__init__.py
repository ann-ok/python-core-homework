def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []

    for categoryId in mapping['categoryIdsSorted']:
        category = mapping['categories'][categoryId]
        items = []

        for roleId in category['roleIds']:
            role = mapping['roles'][roleId]
            items.append({
                'id': role['id'],
                'text': role['name']
            })

        categories.append({
            'id': 'category-' + category['id'],
            'text': category['name'],
            'items': items
        })

    return {'categories': categories}

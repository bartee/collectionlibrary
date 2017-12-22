from django.db import migrations

tag_names = ['snel', 'slank', 'vegetarisch', 'pasta', 'aziatisch', 'soep', 'stamppot', 'dessert', 'Baksel', 'lunch',
                'winter', 'zomer', 'lente', 'herfst', 'uitproberen!', 'wild', 'speciaal', 'mexicaans', 'rijst',
                'hartige taart', 'snackvoer']

def forwards_func(apps, schema_editor):
    """
    Apply this migration: create the initial tags from a predefined list

    We get the model from the versioned app registry;
    if we directly import it, it'll be the wrong version

    :param apps:
    :param schema_editor:
    :return:
    """
    TagModel = apps.get_model("catalog", "Tag")
    db_alias = schema_editor.connection.alias
    tag_list = []
    for tag in tag_names:
        tag_list.append(TagModel(name=tag))

    TagModel.objects.using(db_alias).bulk_create(tag_list)


def reverse_func(apps, schema_editor):
    """
    Revert this migration: remove the initial tags

    We get the model from the versioned app registry;
    if we directly import it, it'll be the wrong version

    :param apps:
    :param schema_editor:
    :return:
    """
    TagModel = apps.get_model("catalog", "Tag")
    db_alias = schema_editor.connection.alias
    for tag in tag_names:
        TagModel.objects.using(db_alias).filter(name=tag).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20171222_1445' )
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]


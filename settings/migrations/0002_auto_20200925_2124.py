

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplicationInstruction',
            new_name='Instruction',
        ),
        migrations.RenameModel(
            old_name='ApplicationInstructionList',
            new_name='InstructionList',
        ),
        migrations.AlterModelOptions(
            name='instruction',
            options={'verbose_name': 'Instruction',
                     'verbose_name_plural': '2.Instruction'},
        ),
    ]

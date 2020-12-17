from django import forms
from catalogue.models import StorageUpdate, Sample, Shelf


class StorageUpdateForm(forms.ModelForm):

    def save(self, commit=True):
        updates = self.cleaned_data.get('entry_content', None)
        update_split = updates.splitlines()

        for entry in update_split:
            if 'bat' in entry.lower():
                entry = entry.replace('_', '-', 1)
                sample_queries = Sample.objects.filter(barcode__iexact=entry)
                for sample in sample_queries:
                    sample.shelf = current_shelf
                    sample.save()
            else:
                shelf_queries = Shelf.objects.filter(shortname__iexact=entry)
                for shelf in shelf_queries:
                    current_shelf = shelf

        return super(StorageUpdateForm, self).save(commit=commit)

    class Meta:
        model = StorageUpdate
        fields = ['entry_date', 'entry_content', 'entry_author']

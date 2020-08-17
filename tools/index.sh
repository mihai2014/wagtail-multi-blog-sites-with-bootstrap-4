# rebuilds the search index ... 
# whenever any pages have been created through a script (after an import, for example)
# whenever any changes have been made to models or search configuration

python ../manage.py update_index

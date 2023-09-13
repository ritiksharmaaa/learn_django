from django import forms 
# by default form id = id_name , sirname , email and name = what we give in field name , help in css and js 
# we have to manually type table tag form tag and submit butoon 
# labble name is change as ifjust like your right hanf = and if you give _ it will assume as spaces



# form rendring options -----
# form.as_table = wrap this form in table tag 
# fporms.as_p = wrap into a p tage 
#form.as_ul = wrap into a li tage 
# form.name_of_field  render from field manually 






class user(forms.Form):
    name = forms.CharField()
    
    email = forms.EmailField()

  
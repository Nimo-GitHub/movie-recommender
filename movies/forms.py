from django import forms
from .models import Movie
class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = [
			'title',       
		    'year',        	 
		    'certificate' , 
		    'duration' ,   
		    'genre' ,      
		    'rating',      
		    'metascore' ,  
		    'description' ,
		    'director',   
		    'cast' ,       
		    'poster'     
		]



# class RawMovieForm(forms.Form):
# 	title       = forms.TextField()
#    	year        = forms.TextField()
#     certificate = forms.TextField() 
#     duration    = forms.TextField() 
#     genre       = forms.TextField()
#     rating      = forms.TextField()
#     metascore   = forms.TextField()
#     description = forms.TextField()
#     director    = forms.TextField()
#     cast        = forms.TextField()
#     poster      = forms.ImageField(upload_to='images/', default='Photo Unavaliable') 
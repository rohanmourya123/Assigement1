#from django import forms
#from ..User.models import Post
from .models import Product

# class form(forms.ModelForm):
#     class meta:
#         model = Post
#         fields =('__all__')


class ProductRouter:
    router_app_lable ={"Products"}
    def db_for_read(self,model,**hints):
        if model._meta_app_label in self.router_app_lable:
            return "Products_db"
        return None

    def db_for_write(self,model,**hints):
        if model._meta_app_label in self.router_app_lable:
            return "Products_db"
        return None
    def allow_relation(self,obj1,obj2,**hints):
        if obj1._meta_app_label in self.router_app_lable or obj2._meta_app_label in self.router_app_lable:
            return True
        return None
    def allow_migrate(self,db,app_label,model_name=None,**hints):
        if app_label in self.router_app_lable:
            return db == "Products_db"
        return None


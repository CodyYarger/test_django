from django.contrib import admin
from blogging.models import Post, Category

# Below two lines are the basic way to register a model if the user does not need to customize any values
# admin.site.register(Post)
# admin.site.register(Category)

# From Assignment
# "2 You’ll need to create a customized  ModelAdmin  class for the  Post  and  Category  models.""

#* The class ModelAdmin(admin.ModelAdmin): is the representation of a model in the admin interface.
#* The above is exactly the same as [admin.site.register(Author)] implemented in lesson 06.
#  It just gives the user the opportunity to define custom values.  Below we use the class to exclude
#  posts from the Category model.

# Rewritten to utilize custom ModelAdmin class
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # exclued posts form the Category admin page (posts is defined in the Category model not to be confused with the Post model)    
    exclude = ('posts',)

# From Assignment
# "3 And you’ll need to create an  InlineModelAdmin  to represent Categories on the Post admin view.""

# ModelInline allows us to edit the Category model on the same page as the Post (parent model) model.
# TabularInline is the template used to render the page 
# 
# Admin widgets () for many-to-many relations will be displayed on whichever model contains the actual
# reference to the ManyToManyField. So we use the .through method in our Category model as it conatins the
# many to many relationship. The through attribute is a reference to the model that manages the many-to-many
# relation. This model is automatically created by Django when you define a many-to-many field.
# 
# A widget is Django’s representation of an HTML input element. The widget handles the rendering of the
# HTML, and the extraction of data from a GET/POST dictionary that corresponds to the widget.
class CategoryInline(admin.TabularInline):
    model = Category.posts.through

# Here we register the Post model and add a custome value for inlines and add the CategoryInline class
# If you want to display many-to-many relations using an inline, you can do so by defining an InlineModelAdmin
# object for the relationship.So here we add the CatogoryInline object to our PostAdmin 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
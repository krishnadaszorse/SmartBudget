from django.shortcuts import render
from .forms import SetMonthStartDateForm,SetWeekDaysForm,SetCountryForm,SetTypeForm,CategoriesForm,CategoryForm
# Create your views here.
#  _____________________________________________________________________
# |               settings_dashboard.                                   |
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on settings link									|
# |---------------------------------------------------------------------|
# | Output 					: User can view settings dashboard		|
# | --------------------------------------------------------------------|
# | Models 					:											|
# | --------------------------------------------------------------------|
# | Forms 					:										|
# |_____________________________________________________________________|
def settings_dashboard(request):
	variables = RequestContext(request,{})
	return render_to_response('settings_dashboard.html', variables)

#  _____________________________________________________________________
# |               set_month_start_date.                                 |
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: Click on set month start date				|
# |---------------------------------------------------------------------|
# | Output 					: Months start date changes in database
# | --------------------------------------------------------------------|
# | Models 					: AppUser									|
# | --------------------------------------------------------------------|
# | Forms 					: SetMonthStartDateForm						|
# |_____________________________________________________________________|
def set_month_start_date(request):
	form = SetMonthStartDateForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('set_month_start_date.html', variables)

#  _____________________________________________________________________
# |               set_weekdays 	                                 		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: Click on set weekdays					|
# |---------------------------------------------------------------------|
# | Output 					: Months start date changes in database	|
# | --------------------------------------------------------------------|
# | Models 					: AppUser									|
# | --------------------------------------------------------------------|
# | Forms 					: SetWeekDaysForm							|
# |_____________________________________________________________________|
def set_weekdays(request):
	form = SetWeekDaysForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('set_weekdays.html', variables)

#  _____________________________________________________________________
# |                      set_country 	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: Click on set country				|
# |---------------------------------------------------------------------|
# | Output 					: country changes in database	|
# | --------------------------------------------------------------------|
# | Models 					: AppUser									|
# | --------------------------------------------------------------------|
# | Forms 					: SetCountryForm						|
# |_____________________________________________________________________|
def set_country(request):
	form = SetCountryForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('set_country.html', variables)

#  _____________________________________________________________________
# |                      set_type	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: Click on set type 				|
# |---------------------------------------------------------------------|
# | Output 					: type changes in database.	|
# | --------------------------------------------------------------------|
# | Models 					: AppUser									|
# | --------------------------------------------------------------------|
# | Forms 					: SetTypeForm							|
# |_____________________________________________________________________|


def set_type(request):
	form = SetTypeForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('set_type.html', variables)

#  _____________________________________________________________________
# |                      income_categories	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on income categories				|
# |---------------------------------------------------------------------|
# | Output 					: User can view income category list	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					: 											|
# |_____________________________________________________________________|	



def income_categories(request):
	variables = RequestContext(request,{})
	return render_to_response('income_categories.html', variables)


  _____________________________________________________________________
# |                     add_ income_category	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on add new link				|
# |---------------------------------------------------------------------|
# | Output 					: New category added as income category to 
#                             database.	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					: CategoriesForm					|
# |_____________________________________________________________________|

def add_income_category(request):
	form = CategoriesForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('add_income_category.html', variables)

  _____________________________________________________________________
# |                      expense_categories	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on expense categories				|
# |---------------------------------------------------------------------|
# | Output 					: User can view expense category list	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					:											|
# |_____________________________________________________________________|


def expense_categories(request):
	variables = RequestContext(request,{})
	return render_to_response('expense_categories.html', variables)


  _____________________________________________________________________
# |                      add_expense_category	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on add new link				|
# |---------------------------------------------------------------------|
# | Output 					: New category added as expense category to 
#                              database	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					:CategoriesForm					|
# |_____________________________________________________________________|

def add_expense_category(request):
	form = CategoriesForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('add_expense_category.html', variables)

  _____________________________________________________________________
# |                      edit_category	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on edit link of a category				|
# |---------------------------------------------------------------------|
# | Output 					: expense category changes will be done in 
#                              database	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					:CategoryForm					|
# |_____________________________________________________________________|


def edit_category(request,id):
	form = CategoryForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('edit_category.html', variables)

  _____________________________________________________________________
# |                      archive_category	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on archive link of a expense 
#                              category				|
# |---------------------------------------------------------------------|
# | Output 					: Category data will be archive in database	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					:					|
# |_____________________________________________________________________|

def archive_category(request,id):
	variables = RequestContext(request,{})
	return render_to_response('archive_category.html', variables)

  _____________________________________________________________________
# |                      delete_category	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: User click on delete link of a expense 
#                             category 				|
# |---------------------------------------------------------------------|
# | Output 					: Category data will be delete from database	|
# | --------------------------------------------------------------------|
# | Models 					: Category								|
# | --------------------------------------------------------------------|
# | Forms 					:					|
# |_____________________________________________________________________|


def delete_category(request,id):
	variables = RequestContext(request,{})
	return render_to_response('delete_category.html', variables)

  _____________________________________________________________________
# |                      credits	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: Enter task description, date, user assigned, 
#                             status(default status open) and save.		|
# |---------------------------------------------------------------------|
# | Output 					: Task will be created and user assigned will
#                              get it in his task list.					|
# | --------------------------------------------------------------------|
# | Models 					: 											|
# | --------------------------------------------------------------------|
# | Forms 					:											|
# |_____________________________________________________________________|


def credits(request):
	variables = RequestContext(request,{})
	return render_to_response('credits.html', variables)


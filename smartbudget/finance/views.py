from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import TransactionForm	

# Create your views here.
#  _____________________________________________________________________
# |                      dashboard.                                   |
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: Click on dash board link							|
# |---------------------------------------------------------------------|
# | Output 					: show account details 		|
# | --------------------------------------------------------------------|
# | Models 					:	Transaction,Category										|
# | --------------------------------------------------------------------|
# | Forms 					:	TransactionDashboardForm   										|
# |_____________________________________________________________________|
def dashboard(request):
	variables = RequestContext(request,{})
	return render_to_response('dashboard.html', variables)

#  _____________________________________________________________________
# |               add_income.                                 |
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: click on add income link and submit with data					|
# |---------------------------------------------------------------------|
# | Output 					: Income transaction will be saved to database. 		|
# | 	 					 	|
# | --------------------------------------------------------------------|
# | Models 					: Transaction							|
# | --------------------------------------------------------------------|
# | Forms 					: 	TransactionForm					|
# |_____________________________________________________________________|
def add_income(request):
	form = TransactionForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('add_income.html', variables)

#  _____________________________________________________________________
# |               sadd_expense 	                                 		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: click on add income link and submit with data					|
# |---------------------------------------------------------------------|
# | Output 					: Expense transaction will be saved to database. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: TransactionForm						|
# |_____________________________________________________________________|
def add_expense(request):
	form = TransactionForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('add_expense.html', variables)

#  _____________________________________________________________________
# |                      view_transaction_daily 	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on daily transaction link 				|
# |---------------------------------------------------------------------|
# | Output 					: User can view per day transaction. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	TransactionDateFilterForm										|
# |_____________________________________________________________________|
def view_transaction_daily(request):
	variables = RequestContext(request,{})
	return render_to_response('view_transaction_daily.html', variables)

#  _____________________________________________________________________
# |                      view_transaction_monthly	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on monthly transaction link 				|
# |---------------------------------------------------------------------|
# | Output 					: User can view per day transaction. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	TransactionMonthlyFilterForm						|
# |_____________________________________________________________________|


def view_transaction_monthly(request):
	variables = RequestContext(request,{})
	return render_to_response('view_transaction_monthly.html', variables)


#  _____________________________________________________________________
# |                      view_transaction_yearly	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on yearly transaction link 				|
# |---------------------------------------------------------------------|
# | Output 					: User can view per month transaction. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	TransactionYearlyFilterForm						|
# |_____________________________________________________________________|

def view_transaction_yearly(request):
	variables = RequestContext(request,{})
	return render_to_response('view_transaction_yearly.html', variables)

#  _____________________________________________________________________
# |                      edit_transaction_	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on edit link it				|
# |---------------------------------------------------------------------|
# | Output 					: Transaction will be changes in database. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	TransactionForm						|
# |_____________________________________________________________________|


def edit_transaction(request,id):
	form = TransactionForm()
	variables = RequestContext(request,{'form':form})
	return render_to_response('edit_transaction.html', variables)

#  _____________________________________________________________________
# |                      delete_transaction                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on delete link 				|
# |---------------------------------------------------------------------|
# | Output 					:Transaction will be deleted from database 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	TransactionForm					|
# |_____________________________________________________________________|

def delete_transaction(request,id):
	variables = RequestContext(request,{})
	return render_to_response('delete_transaction.html', variables)

#  _____________________________________________________________________
# |                      view_graph_monthly	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on monthly graph link				|
# |---------------------------------------------------------------------|
# | Output 					: User can view monthly income expense graph.. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	ViewGraphMonthlyForm						|
# |_____________________________________________________________________|


def view_graph_monthly(request):
	variables = RequestContext(request,{})
	return render_to_response('view_graph_monthly.html', variables)

#  _____________________________________________________________________
# |                      view_graph_yearly	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on yearly graph link				|
# |---------------------------------------------------------------------|
# | Output 					: User can view yearly income expense graph. 	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	ViewGraphYearlyForm						|
# |_____________________________________________________________________|



def view_graph_yearly(request):
	variables = RequestContext(request,{})
	return render_to_response('view_graph_yearly.html', variables)

#  _____________________________________________________________________
# |                      view_graph_category	                           		|
# |---------------------------------------------------------------------|
# | Login required			: True   									|
# |---------------------------------------------------------------------|
# | Input 					: clicking on category graph link.				|
# |---------------------------------------------------------------------|
# | Output 					: User can view date range category graph.	|
# | 	 					  	|
# | --------------------------------------------------------------------|
# | Models 					: transaction									|
# | --------------------------------------------------------------------|
# | Forms 					: 	ViewGraphCategoryForm						|
# |_____________________________________________________________________|	


def view_graph_category(request):
	variables = RequestContext(request,{})
	return render_to_response('view_graph_category.html', variables)


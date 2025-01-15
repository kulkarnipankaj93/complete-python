manufact_plants = ['Mumbai','Banglore','Delhi','Chennai']
Company_info = {'Comapny_name':'Ford','Estd_year':1980,'office_location':manufact_plants}
product_info = {'Mumbai':[{'model_name':'Freestyle','man_year':2001},{'model_name':'Ecosport','man_year':2002}],
                'Banglore':[{'model_name':'Figo','man_year':2001}],
                'Delhi':[{'model_name':'Aspire','man_year':2010}],
                'Chennai':[{'model_name':'Endeavour','man_year':2001},{'model_name':'Fista','man_year':2005}]}

print(product_info)

# program to print products manufactured at given location- using two variables
for location,model in product_info.items():
    if location == 'Delhi':
        print(model)


# program to print products manufactured at given location- using one variable
for location in product_info:
    if location == 'Delhi':
        print(product_info[location])


# program to print model names which are manufactured in given year
print("Car manufacturing company is:",Company_info['Company_name'])
print("Models manufactured in 2001 are as follows:")
for location, model_info in product_info.items():
    for model in model_info:
        if model['man_year'] == 2001:
            print(model['model_name'])


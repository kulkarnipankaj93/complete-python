# First way to import package - Importing module from package
from asia import india
print(india.capital)

# second way to import - Importing function/variables from module
from europe.germany import ind_year as german_ind                # model level import must be at top
german_ind()

# if same name functions are imported from two modules it will execute from latest module imported
from asia.bangladesh import ind_year
from europe.scotland import ind_year
ind_year()


# to import total directory we need to convert it to package
# and to convert that directory into package we need to create "__init__.py" module

from .forms import UsaForm,IncomeForm,GermanyForm,CanadaForm,AustraliaForm
from .formulas import usaformula,franceformula,ukformula,germanyformula,canadaformula,australiaformula
countries={
    'usa': {
        'name': 'United States',
        'currency': '$',
        'form': UsaForm,
        'function': usaformula,
        'min_single':75000,
        'max_single':99000,
        'min_married':150000,
        'max_married':198000,
        'min_Head_of_houshold':112500,
        'max_Head_of_houshold':136500,
    },
    'ca': {
        'name': 'Canada',
        'currency': '$',
        'form': CanadaForm,
        'function': canadaformula,
    },
    'au': {
        'name': 'Australia',
        'currency': '$',
        'form': AustraliaForm,
        'function': australiaformula,
        'description': 'Only Employees who make <b>$1500</b> or less '
                       'per <b>Fortnight</b> will benefit from stimulus check.'
                       ' If the Employees make more than that, then their Employer may '
                       'use the subsidy payment to reduce the cost of the salary payment.'
                       ' The Employers may also voluntarily elect to pass through some or '
                       'all of the payment to employees as an additional amount.'
    },
    'ge': {
        'name': 'Germany',
        'currency': '€',
        'form': GermanyForm,
        'function': germanyformula,
        'parent_percentage': 67,
        'non_parent_percentage':60,
        'description': 'Only the employees who has been laid'
                      ' off from their company will benefit from a stimulus check.'
    },
    'uk': {
        'name': 'United Kingdom',
        'currency': '£',
        'min_value': 3125,
        'form': IncomeForm,
        'function': ukformula,
    },

    'fr': {
        'name': 'France',
        'currency': '€',
        'function': franceformula,
        'min_wage': 1521.22,
        'max_value': 5485,
        'form': IncomeForm
    },

}

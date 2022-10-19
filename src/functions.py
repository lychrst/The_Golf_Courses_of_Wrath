import pandas as pd
import statsmodels.api as sm

def km3_to_Mgal(num):
    '''Converts square kilometers into million gallon units.
    
    Parameters
    ----------
    num: float or int 
    The number of square kilometers being converted.
    
    Returns 
    -------
    Mgal: float 
    The number of million gallons that result from the conversion.
    '''
    Mgal =((num)*264172052358.15) /1000000
    return Mgal


def acre_feet_to_Mgal(num):
    '''Converts acre feet into million gallon units.
    
    Parameters
    ----------
    num: Float or int 
    The number of acre feet being converted.
    
    Returns 
    -------
    Mgal: Float 
    The number of million gallons that result from the conversion.
    '''
    Mgal =((num)*325724.1405576) /1000000
    return Mgal

def dashes_to_zeros(col):
    '''Replaces two dashes with zeroes.
    
    Parameters
    ----------
    col: str 
    Column in Dataframe being modified.
    
    Returns 
    -------
    val: float 
    0.00 stored as a float
    '''
    val= (col).apply(lambda x: x.replace('--', '0.00')).astype(float)
    return val

def correlation_pairs(data, lower, upper):
    '''Creates correlation pairs for variables contained within a data source.
    
    Parameters
    ----------
    Data: pandas DataFrame 
    DataFrame containing the data being analyzed for correlations.
    
    lower: int or float
    The lower percentage threshold.  All correlation pairs will have values at
    or above this number.
    
    upper: int or float 
    The upper percentage cutoff.  All correlation pairs will have values at
    or below this number.
    
    Returns 
    -------
    span: float
    The correlation pairs that had values at or between the lower and upper bound.
    ''' 
    df=data.corr().abs().stack().reset_index().sort_values(0, ascending=False)
    df['pairs'] = list(zip(df.level_0, df.level_1))
    df.set_index(['pairs'], inplace = True)
    df.drop(columns=['level_1', 'level_0'], inplace = True)
    df.columns = ['cc']

    df.drop_duplicates(inplace=True)
    span = df[(df.cc>lower) & (df.cc <upper)]
    return span

def standardized_model(X, Y):
    '''Creates a model that uses standard deviation to compare the impact
    dependent variable(s) have on the independent variable. 
    
    Parameters
    ----------
    x : int or float
    The dependent variable(s) being analyzed.
    
    y: int or float
    The independent variable being analyzed.
    
    Returns 
    -------
    standardized_results.params : float
    
    The impact one standard deviation of a dependent variable has on the 
    independent variable.
    '''
    X_standardized = X.copy()
    for col in X_standardized:
        X_standardized[col] = (X_standardized[col]\
        - X_standardized[col].mean()) / X_standardized[col].std()
        standardized_model = sm.OLS(Y, sm.add_constant(X_standardized))
    standardized_results = standardized_model.fit()
    return standardized_results.params                                
                                
                                



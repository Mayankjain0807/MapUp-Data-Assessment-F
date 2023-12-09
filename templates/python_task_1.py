import pandas as pd
import numpy as np
def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
        # Write your logic here
    df_1 =  pd.pivot_table(df, values ='car', index =['id_1'], 
                         columns =['id_2']) 
    # convert dataframe into nummpy
    arr = table_1.to_numpy()

    # fill the diagnol of matrix with 0

    np.fill_diagonal(arr, 0)
  
    # convert the array back to a DataFrame
    df = pd.DataFrame(arr, columns=df_1.columns, index=df_1.index)

    return df

def get_type_count(df)->dict:
    
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    categorical_data = [] 
    for index, row in df.iterrows():
        if row['car'] <= 15:
            categorical_data.append("low")
        elif row['car'] >15 and row['car'] <=25:
            categorical_data.append("medium")
        else:
            categorical_data.append("high")
    df['car_type'] = pd.DataFrame(categorical_data)
    dict = {}
    for i in categorical_data:
        dict[i] = categorical_data.count(i)
        
    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    # calculate the twice the mean of bus column
    mean_bus = df['bus'].mean()*2
    # Find the index of bus column where value greater than the teice the mean value
    list = [] 
    for index, row in df.iterrows():
        if row['bus'] > mean_bus:
            list.append(index)
    list.sort()
    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    for index, row in matrix.iterrows():
        for i in matrix.columns:
            if row[i] > 20:
                row[i] = round(row[i]*0.75,2)
            else:
                row[i] = round(row[i]*1.25,2)

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()

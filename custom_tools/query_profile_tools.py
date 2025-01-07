from modules.vertica import read

def check_long_running_queries(vertica_conn, from_datetime, to_datetime, user_name=None):
    '''
    args:
        1. vertica_conn: vertica connection object
        2. from_datetime: datetime string in 'YYYY-MM-DD HH:MM' format
        3. to_datetime: datetime string in 'YYYY-MM-DD HH:MM' format
        4. user_name: user name which can be used in where condition of the query (default None)
    
    returns: dataframe with columns 'query_start', 'query_duration_us', and 'query'

    query_start denotes when the query was started executing
    query_duration_us denotes the duration of query execution in microseconds
    query is first 100 characters of actual query
    '''

    if user_name is None:
        query = f"""
        select query_start,query_duration_us,left(query,110) from netstats.query_profiles where query_start between '{from_datetime}' AND '{to_datetime}' order by query_start;
        """
    else:
        query = f"""
        select query_start,query_duration_us,left(query,110) from netstats.query_profiles where user_name= '{user_name}' and query_start between '{from_datetime}' AND '{to_datetime}' order by query_start;
        """
    
    df = read(vertica_conn, query, ["query_start", "query_duration_us", "query"])
    
    return df

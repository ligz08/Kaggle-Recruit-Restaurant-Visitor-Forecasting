def plotDatesByYeamMonth(dateSeries):
    '''
    :param dateSeries:  pandas.Series of dtype datetime64[ns],
                        or something that can be converted to datetime64[ns]' by pd.to_datetime()
    :return: matplotlib.Axes object
    '''
    import pandas as pd
    dateSeries = pd.to_datetime(dateSeries)
    ax = dateSeries\
            .groupby([dateSeries.dt.year, dateSeries.dt.month])\
            .size()\
            .plot.bar()
    ax.set_xlabel('(Year, Month)')
    ax.set_ylabel('# records each month')
    return ax
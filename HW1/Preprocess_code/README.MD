# Code on preprocessing the data


## Download the etf code 

* yahoo_finance_crawler_for_singlegroup : It is for download etf data on yahoo-finance for our etfgroup

* crawler_all_ETF : Is is for download all etf data we need on yahoo-finance (etf is filter by date before)

## Filter etf_data on date

* Filter_download_ETF : Its just for knowing the etf we download before which is already download 

* Filter_date_time_testing_code : just like its name . it just testing how to filter datetime on the download csv etf_data

* filter_all_etf : It filter all data we download on each ETF_group . we want to know the date its fit the dateline we want or not .
It can save mach time rather than we download all etf_data at the first time

## Merge data

* merge_singlegroup_data : we just merge all etf data to one csv . we just want etf's (adj close and date)

* merge : It merge all etf_data after we filter it

## Calculate data

* calculate_return_rate : we calculate the return rate on single group of etf

* calculate_all_return_rate : we calculate all etf_data into return rate and save it into another data_set  
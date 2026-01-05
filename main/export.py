# script to export to csv if requested (from input.py)

def export(check_bool, df):
    if check_bool == True:
        df.to_csv('test.csv')

if __name__ == "__main__":
    csv_fun(df)
# Export pulled data to CSV if requested

def export(check_bool, df):
    if check_bool == True:
        df.to_csv('test.csv')

if __name__ == "__main__":
    csv_fun(df)
def export(check_bool, df):
    if check_bool == True:
        df.to_csv(f'export.csv')

if __name__ == "__main__":
    export(df)
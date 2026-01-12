def export(check_bool, export_df):
    if check_bool == True:
        export_df.to_csv(f'export.csv')

if __name__ == "__main__":
    export(export_df)
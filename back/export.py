# Export pulled data to CSV if requested

# Change to input df from wrangler
def export(check_bool, w_df):
    if check_bool == True:
        df.to_csv('test.csv')

if __name__ == "__main__":
    csv_fun(df)
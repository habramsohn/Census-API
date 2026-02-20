def selection(arg, data):
    selected = [var.get("var", None) for var in data[arg]]
    return selected


def wrun(df, arg, data):
    selected = selection(arg, data)
    new_df = df[selected]
    new_df.index.name = "year"
    return new_df


def wrangle_csv(df, data):
    csv = [i.get("var", None) for l in data.values() for i in l]
    csv = [col for col in csv if col is not None]  # Filter out None values
    export_df = df[csv]
    export_df.index.name = "year"
    return export_df
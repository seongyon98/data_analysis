import pandas as pd


def create_fakedatamart(df: pd.DataFrame) -> pd.DataFrame:
    today = pd.to_datetime("today")
    df["birthdate"] = pd.to_datetime(df["birthdate"], format="%Y%m%d")

    df["city"] = df["residence"].str.split().str[0]

    df["birth_year"] = df["birthdate"].dt.year

    df["age"] = (
        today.year
        - df["birthdate"].dt.year
        - (
            today.month
            < df["birthdate"].dt.month
            | (
                (today.month == df["birthdate"].dt.month)
                & (today.day < df["birthdate"].dt.day)
            )
        )
    ).astype(int)

    df["blood"] = df["blood_group"].str.slice(0, -1)

    df["age_category"] = df["age"].apply(caterogize_age)

    column_list = [
        "uuid",
        "name",
        "job",
        "sex",
        "blood",
        "city",
        "birth_year",
        "age",
        "age_category",
    ]

    df_datemart = df[column_list]

    return df_datemart


def caterogize_age(age: int):
    if age >= 90:
        return "90대 이상"
    else:
        return str(age // 10 * 10) + "대"

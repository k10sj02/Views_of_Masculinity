import pandas as pd

SOURCE_DATA_NOT_SELECTED = "Not selected"

# employment
EMPLOYED = "employed"
NOT_EMPLOYED = "not_employed"

# sexual orientation
STRAIGHT = "straight"
BISEXUAL = "bisexual"
NOT_STRAIGHT = "not_straight"

# race
WHITE = "white"
NOT_WHITE = "not_white"

# schooling
NO_HIGH_SCHOOL = "no_high_school"
HIGH_SCHOOL = "high_school"
COLLEGE_GRADUATE = "college_graduate"
GRADUATE = "graduate"

# regions
NORTHEAST = "northeast"
SOUTHEAST = "southeast"
MIDWEST = "midwest"
SOUTHWEST = "southwest"
WEST = "west"

Q0001_SUBSTITUTION = {
    "Very masculine": "very_masculine",
    "Somewhat masculine": "somewhat_masculine",
    "Not very masculine": "not_very_masculine",
    "Not at all masculine": "not_at_all_masculine",
    "No answer": pd.NA,
}

Q0001_QUANTIZATION = {
    "very_masculine": 1,
    "somewhat_masculine": 2 / 3,
    "not_very_masculine": 1 / 3,
    "not_at_all_masculine": 0,
}

Q0002_SUBSTITUTION = {
    "Very important": "very_important",
    "Somewhat important": "somewhat_important",
    "Not too important": "not_too_important",
    "Not at all important": "not_at_all_important",
    "No answer": pd.NA,
}

Q0002_QUANTIZATION = {
    "very_important": 1,
    "somewhat_important": 2 / 3,
    "not_too_important": 1 / 3,
    "not_at_all_important": 0,
}

Q0009_SUBSTITUTION = {
    "Employed, working full-time": EMPLOYED,
    "Employed, working part-time": EMPLOYED,
    "No answer": pd.NA,
    "Not employed-retired": NOT_EMPLOYED,
    "Not employed, looking for work": NOT_EMPLOYED,
    "Not employed, NOT looking for work": NOT_EMPLOYED,
    "Not employed, student": NOT_EMPLOYED,
}

Q0009_QUANTIZATION = {
    EMPLOYED: 1,
    NOT_EMPLOYED: 0,
}

Q0025_QUANTIZATION = {
    True: 1,
    False: 0,
}


Q0026_SUBSTITUTION = {
    "Gay": NOT_STRAIGHT,
    "Straight": STRAIGHT,
    "No answer": pd.NA,
    "Bisexual": BISEXUAL,
    "Other": pd.NA,
}

Q0026_QUANTIZATION = {
    STRAIGHT: 1,
    BISEXUAL: 0.5,
    NOT_STRAIGHT: 0,
}

Q0028_SUBSTITUTION = {
    "Hispanic": NOT_WHITE,
    "White": WHITE,
    "Other": NOT_WHITE,
    "Black": NOT_WHITE,
    "Asian": NOT_WHITE,
}

Q0028_QUANTIZATION = {
    WHITE: 1,
    NOT_WHITE: 0,
}

Q0029_SUBSTITUTION = {
    "Did not complete high school": NO_HIGH_SCHOOL,
    "Some college": HIGH_SCHOOL,
    "High school or G.E.D.": HIGH_SCHOOL,
    "Associate's degree": HIGH_SCHOOL,
    "College graduate": COLLEGE_GRADUATE,
    "Post graduate degree": GRADUATE,
}

Q0029_QUANTIZATION = {
    GRADUATE: 1,
    COLLEGE_GRADUATE: 2 / 3,
    HIGH_SCHOOL: 1 / 3,
    NO_HIGH_SCHOOL: 0,
}

Q0030_SUBSTITUTION = {
    # NORTHEAST
    "Connecticut": NORTHEAST,
    "Delaware": NORTHEAST,
    "District of Columbia (DC)": NORTHEAST,
    "Maine": NORTHEAST,
    "Maryland": NORTHEAST,
    "Massachusetts": NORTHEAST,
    "New Hampshire": NORTHEAST,
    "New Jersey": NORTHEAST,
    "New York": NORTHEAST,
    "Pennsylvania": NORTHEAST,
    "Rhode Island": NORTHEAST,
    "Vermont": NORTHEAST,
    # SOUTHEAST
    "Alabama": SOUTHEAST,
    "Arkansas": SOUTHEAST,
    "Florida": SOUTHEAST,
    "Georgia": SOUTHEAST,
    "Kentucky": SOUTHEAST,
    "Louisiana": SOUTHEAST,
    "Mississippi": SOUTHEAST,
    "North Carolina": SOUTHEAST,
    "South Carolina": SOUTHEAST,
    "Tennessee": SOUTHEAST,
    "Virginia": SOUTHEAST,
    "West Virginia": SOUTHEAST,
    # MIDWEST
    "Illinois": MIDWEST,
    "Indiana": MIDWEST,
    "Iowa": MIDWEST,
    "Kansas": MIDWEST,
    "Michigan": MIDWEST,
    "Minnesota": MIDWEST,
    "Missouri": MIDWEST,
    "Nebraska": MIDWEST,
    "North Dakota": MIDWEST,
    "Ohio": MIDWEST,
    "South Dakota": MIDWEST,
    "Wisconsin": MIDWEST,
    # SOUTHWEST
    "Arizona": SOUTHWEST,
    "New Mexico": SOUTHWEST,
    "Oklahoma": SOUTHWEST,
    "Texas": SOUTHWEST,
    # WEST
    "Alaska": WEST,
    "California": WEST,
    "Colorado": WEST,
    "Hawaii": WEST,
    "Idaho": WEST,
    "Montana": WEST,
    "Nevada": WEST,
    "Oregon": WEST,
    "Utah": WEST,
    "Washington": WEST,
    "Wyoming": WEST,
}


def combine_has_children(q0025_0001_value: str, q0025_0002_value: str):
    return (q0025_0001_value, q0025_0002_value) != (
        SOURCE_DATA_NOT_SELECTED,
        SOURCE_DATA_NOT_SELECTED,
    )


def clean_data(source: pd.DataFrame):
    dest = pd.DataFrame()

    dest["q0001"] = source["q0001"].map(Q0001_SUBSTITUTION)
    dest["q0002"] = source["q0002"].map(Q0002_SUBSTITUTION)
    dest["q0009"] = source["q0009"].map(Q0009_SUBSTITUTION)
    dest["q0025"] = source["q0025_0001"].combine(
        source["q0025_0002"], combine_has_children
    )
    dest["q0026"] = source["q0026"].map(Q0026_SUBSTITUTION)
    dest["q0028"] = source["q0028"].map(Q0028_SUBSTITUTION)
    dest["q0029"] = source["q0029"].map(Q0029_SUBSTITUTION)
    # hard to quantify, dropped for now
    # dest["q0030"] = source["q0030"].map(Q0030_SUBSTITUTION)

    dest.dropna(inplace=True)
    return dest


def quantize_data(source: pd.DataFrame):
    dest = pd.DataFrame()
    dest["q0001"] = source["q0001"].map(Q0001_QUANTIZATION)
    dest["q0002"] = source["q0002"].map(Q0002_QUANTIZATION)
    dest["q0009"] = source["q0009"].map(Q0009_QUANTIZATION)
    dest["q0025"] = source["q0025"].map(Q0025_QUANTIZATION)
    dest["q0026"] = source["q0026"].map(Q0026_QUANTIZATION)
    dest["q0028"] = source["q0028"].map(Q0028_QUANTIZATION)
    dest["q0029"] = source["q0029"].map(Q0029_QUANTIZATION)

    return dest


if __name__ == "__main__":
    source = pd.read_csv("Data/raw-responses.csv")
    cleaned_data = clean_data(source)
    cleaned_data.to_csv("Data/cleaned-responses.csv")

    quantized_data = quantize_data(cleaned_data)
    quantized_data.to_csv("Data/quantized-data.csv")

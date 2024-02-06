import pandas as pd

NO_ANSWER = "no_answer"

# employment
EMPLOYED = "employed"
NOT_EMPLOYED = "not_employed"

# sexual orientation
STRAIGHT = "straight"
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

Q0009_SUBSTITUTION = {
    "Employed, working full-time": EMPLOYED,
    "Employed, working part-time": EMPLOYED,
    "No answer": NO_ANSWER,
    "Not employed-retired": NOT_EMPLOYED,
    "Not employed, looking for work": NOT_EMPLOYED,
    "Not employed, NOT looking for work": NOT_EMPLOYED,
    "Not employed, student": NOT_EMPLOYED,
}

Q0026_SUBSTITUTION = {
    "Gay": NOT_STRAIGHT,
    "Straight": STRAIGHT,
    "No answer": NO_ANSWER,
    "Bisexual": NOT_STRAIGHT,
    "Other": NOT_STRAIGHT,
}

Q0028_SUBSTITUTION = {
    "Hispanic": NOT_WHITE,
    "White": WHITE,
    "Other": NOT_WHITE,
    "Black": NOT_WHITE,
    "Asian": NOT_WHITE,
}

Q0029_SUBSTITUTION = {
    "Did not complete high school": NO_HIGH_SCHOOL,
    "Some college": HIGH_SCHOOL,
    "High school or G.E.D.": HIGH_SCHOOL,
    "Associate's degree": HIGH_SCHOOL,
    "College graduate": COLLEGE_GRADUATE,
    "Post graduate degree": GRADUATE,
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

if __name__ == "__main__":
    dataframe = pd.read_csv("Data/raw-responses.csv")
    dataframe["_employment_status"] = dataframe["q0009"].map(Q0009_SUBSTITUTION)
    dataframe["_sexual_orientation"] = dataframe["q0026"].map(Q0026_SUBSTITUTION)
    dataframe["_race"] = dataframe["q0028"].map(Q0028_SUBSTITUTION)
    dataframe["_schooling"] = dataframe["q0029"].map(Q0029_SUBSTITUTION)
    dataframe["_region"] = dataframe["q0030"].map(Q0030_SUBSTITUTION)

    print(dataframe["_region"].value_counts())

import pandas

df = pandas.read_csv("StudentsPerformance.csv")


class Marks:
    def __init__(self):
        pass

    def highestlowest(self):
        while True:
            prompt = input("Enter math score,reading score,writing score or skip:  ").lower()
            if "math score" in prompt:
                user1 = input("highest,lowest,or average:  ").lower()
                if "highest" in user1:
                    print("The highest score is:", df["math score"].max())
                elif "lowest" in user1:
                    print("The lowest score is:", df["math score"].min())

                elif "average" in user1:
                    print("The average score is:", df["math score"].mean())

            elif "reading score" in prompt:
                user2 = input("highest,lowest,or average:  ").lower()
                if "highest" in user2:
                    print("The highest score is:", df["reading score"].max())
                elif "lowest" in user2:
                    print("The lowest score is:", df["reading score"].min())

                elif "average" in user2:
                    print("The average score is:", df["reading score"].mean())
                elif "skip" in user2:
                    print("skipped")

            elif "writing score" in prompt:
                user2 = input("highest,lowest,or average:  ").lower()
                if "highest" in user2:
                    print("The highest score is:", df["writing score"].max())
                elif "lowest" in user2:
                    print("The lowest score is:", df["writing score"].min())

                elif "average" in user2:
                    print("The average score is:", df["writing score"].mean())
            else:
                break
        print(" ")

    def checkspecific(self):
        while True:
            prompt2 = int(input("Enter a Number from 1 - 10 or 0 to stop: "))
            if prompt2 == 0:
                break
            highest_score = df.loc[prompt2, ["math score", "writing score", "reading score"]].max()
            lowest_score = df.loc[prompt2, ["math score", "writing score", "reading score"]].min()
            average_score = df.loc[prompt2, ["math score", "writing score", "reading score"]].mean()
            print("StudentID", df.loc[prompt2]["StudentID"], "'s highest score is:", highest_score
                  , ", lowest score is:", lowest_score, ", and the average score:", average_score)
            if average_score >= 90:
                print("The Letter GRADE:", "A")
            elif average_score >= 80:
                print("LETTER GRADE:", "B")
            elif average_score >= 70:
                print("LETTER GRADE:", "C")
            elif average_score >= 60:
                print("LETTER GRADE:", "D")
            elif average_score <= 60:
                print("LETTER GRADE:", "F")
            print(" ")


df["Number"] = range(1, 11)
df.set_index("Number", inplace=True)  # "inplace" sets the new index permanently
print(df)
Marks.highestlowest("self")
Marks.checkspecific("self")

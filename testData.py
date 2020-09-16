class testData:
    def __init__(self):
        self.golf_pred = [
        ["Rainy", "Hot", "High", "False"],
        ["Rainy", "Hot", "High", "True"],
        ["Overcast", "Hot", "High", "False"],
        ["Sunny", "Mild", "High", "False"],
        ["Sunny", "Cool", "Normal", "False"],
        ["Sunny", "Cool", "Normal", "True"],
        ["Overcast", "Cool", "Normal", "True"],
        ["Rainy", "Mild", "High", "False"],
        ["Rainy", "Cool", "Normal", "True"],
        ["Sunny", "Mild", "Normal", "False"],
        ["Rainy", "Mild", "Normal", "True"],
        ["Overcast", "Mild", "High", "True"],
        ["Overcast", "Hot", "Normal", "False"],
        ["Sunny", "Mild", "High", "True"]]
        self.golf_target = [
        "No",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "Yes",
        "No",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "Yes",
        "No",
        "No"]

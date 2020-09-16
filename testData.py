from py1r import oneR
#A test of the model given a toy dataset.
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
        self.golf_test_pred = [
            ["Overcast", "Hot", "High", "False"],
            ["Sunny", "Mild", "High", "False"],
            ["Sunny", "Cool", "Normal", "False"],
            ["Sunny", "Cool", "Normal", "True"],
            ["Overcast", "Cool", "Normal", "True"]
        ]
        self.golf_test_target = [
            "Yes",
            "Yes",
            "No",
            "Yes",
            "No",
        ]
if __name__ == "__main__":
    frame = oneR()
    data = testData()
    frame.fit(data.golf_pred,data.golf_target)
    print("Given a toy train and a toy test, the predictions for test:\n" + str(data.golf_test_pred))
    print(frame.predict(data.golf_test_pred))
    print("Accuracy: " + str(frame.score(data.golf_test_pred,data.golf_test_target)))
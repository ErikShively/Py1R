import numpy as np

class oneR:

    #Constructor
    def __init__(self):
        self.rule = []
        self.accuracy = 0
        self.fitShape = []
        self.targets = []

    def _checkInputs(self,X,y) -> bool:

        """
        Internal function to ensure input is valid.
        Parameters:

        X: Array-like of training values.
        y: Array-like of target values.

        Returns:
        bool: Input is valid
        """

        tClasses = len(np.unique(y))
        if(tClasses > 2):
            print("Max unique target values: 2. " + str(tClasses) + " given.")
            return False
        
        #Note that list comprehension is slow and this searches the entire list instead of breaking on an exception
        #This is done this way mostly for readability
        if(all(len(row) == len(X[0]) for row in X) == False):
            print("The X array is not uniform.")
            return False

        if(len(X) != len(y)):
            print("Target array must be the same size as rows.")
            return False

        return True

    def _checkPredict(self,X) -> bool:

        """
        Internal function.
        Makes sure input is valid for the predict method.

        Parameters:
        X: array-like of training values.

        Returns:
        bool: Input is valid
        """

        if(len(X.T) != self.fitShape[1]):
            print("Shape mismatch. Axis 1 is length " + str(len(X.T)) + ". Needs: " + str(self.fitShape[1]))
            return False

        if(len(X.shape) != 2):
            print("Shape mismatch. Array must be 2 dimensions. " + str(len(X.shape)) + " given. If you're testing a single row, cast it as a 2d list with [list]")
            return False
        
        return True



    def fit(self, X, y):

        """
        Trains the model, given X and y.
        Parameters:

        X: Array-like of training data
        y: Array-like of targets

        Returns:
        self: An object that represents a trained model
        """

        if(self._checkInputs(X,y)):
            X,y = np.array(X), np.array(y)
            self.fitShape = X.shape
            self.targets = np.unique(y)
            countTables = []
            topRule = []
            maxAccuracy = 0
            attrTotal = dict()
            for col in X.T:
                cTable = dict()
                unique,counts = np.unique(col,return_counts=True)
                for idx,attr in enumerate(unique):
                    tTable = dict()
                    for target in np.unique(y):
                        tTable[target] = 0
                    cTable[attr] = tTable
                    attrTotal[attr] = counts[idx]
                for idx,row in enumerate(col):
                    cTable[row][y[idx]] += 1
                countTables.append(cTable)
            for idx,table in enumerate(countTables):
                for attr, cTable in table.items():
                    for target, count in cTable.items():
                        accuracy = (count/attrTotal[attr])
                        if(accuracy > maxAccuracy):
                            maxAccuracy = accuracy
                            topRule = [idx,attr,target]
            self.rule = topRule
            self.accuracy = maxAccuracy

        return self

    def predict(self, X) -> list:
        """
        Predicts a target value.
        Parameters:

        X: Array-like of test data

        Returns:
        predictions: a list of predicted outcomes for each row of X
        """

        X = np.array(X)
        predictions = []
        if(self._checkPredict(X)):
            counterTarget = list(self.targets)
            counterTarget.remove(self.rule[2])
            counterTarget = counterTarget[0]
            for entry in X:
                predictions.append(self.rule[2] if entry[self.rule[0]] == self.rule[1] else counterTarget)
        return predictions

    def score(self,X,y) -> float:
        """
        Calculates the accuracy of the model, given test data
        Parameters:

        X: Array-like of test data
        y: Array-like of target values.

        Returns:
        accuracy: a float that represents correctly guessed/total values
        """
        if(self.rule == []):
            print("This model is untrained. Train using the fit method before trying to score.")
            return 0
        if(self._checkInputs(X,y)):
            X = np.array(X)
            correct = 0
            for idx,row in enumerate(X):
                if(self.predict([row]) == [y[idx]]):
                    correct += 1
            return(correct/X.shape[0])
        else:
            return 0

if(__name__ == "__main__"):
    data = testData.testData()
    frame = oneR()
    trained = frame.fit(data.golf_pred,data.golf_target)
    print(trained.predict([
        ["Sunny", "Mild", "High", "True"],
        ["Rainy", "Hot", "High", "True"]]))
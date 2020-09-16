# Py1R
This is a python implementation of the One Rule classifier.
One Rule is a binomial classifier, which means it can only classify between two values.
Credit to Dr. Saed Sayad for the test data and algorithm overview: 
https://www.saedsayad.com/oner.htm
## When to use:
Generally, something like Naive Bayes will do a better job, and it has multinomial implementations in Sci-Kit Learn. This was done mostly for completion, since Sci-Kit Learn doesn't have an implmentation.
## Methods:
`fit(X,y)`
Trains the model by training data X and target data y.

| Parameter | Description |
| --- | --- |
| X | Array-like of training data |
| y | Array-like of target data |

| Returns | Description |
| --- | --- |
| self | An object to hold the trained model |

`predict(X)`
Makes a prediction on the given data
| Parameter | Description |
| --- | --- |
| X | Array-like of test data |

| Returns | Description |
| --- | ---|
| Predictions | A list of predicted values |

`score(X,y)`
Calculates the accuracy of the model, given a set of data to test.
| Parameter | Description |
| --- | --- |
| X | Array-like of training data |
| y | Array-like of target data |

| Returns | Description |
| --- | --- |
| accuracy | A float representing (# of correct classified)/(Total classified) |

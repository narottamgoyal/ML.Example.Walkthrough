# ML.Example.Walkthrough

Decision tree, SVM, and KNN 
Naive Bayes classifier

## convert 30(column) features to 2
* PCA(principle component analysis)

## ImBalance data set problem
1. NearMis is for under sampling
2. SmotoTemk is for over sampling

## Cross validation
1. leave one out - old and not good, low bias (takes only 1 number of set in test and remaining in train)
2. K fold (takes n number of set in test and remaining in train)
3. Stratified (takes all types of set in test and train with K fold technique)
4. Time Series (example for stop price prediction)

## Confusion matrix

TP | FN         TP + TN
------- = -------------------- = Accuracy
FP | TN    TP + TN + FP + FN


## Precision, Recall & f1 Score

                 TP
Precision =  ---------
              TP + FP
              

## In ANN 
1. if o/p is 0 or 1 then use binary_crossentropy and if o/p is having multiple category then use category_crossentropy  loss function
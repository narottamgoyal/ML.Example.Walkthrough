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

```
TP | FN         TP + TN
------- = -------------------- = Accuracy
FP | TN    TP + TN + FP + FN
```

## Precision, Recall & f1 Score

```
                 TP
Precision =  ---------
              TP + FP
```              

## In ANN 
1. if o/p is 0 or 1 then use binary_crossentropy and if o/p is having multiple category then use category_crossentropy loss function

## SVM its basically used in Classification

## Find best hyper parameter for classification
1. Grid Search CV (its slow)
2. Randomized Search CV (its better)

## Clustering
1. K-Means is used to clustering (need to pass number (k value) of clusters to be found), This number (K value) can be determined using Elbow method & DbScan (this is better)
2. Hierarical clustering unsupervised

## Handel missing values
1. delete if dataset is huge
2. create seprate model and prdict the missing value column and then fill all the missing values
3. use mean (Average), median(sort in ascending order and take the mid value in case of odd, in case of even take the average of 2 middle values) and mode (take most occurning value) technique

## Ensemble Technique
1. Bagging (Bootstrap aggregatation) Row sampling with Replacement
    - Random forest
2. Boosting
    - AdaBoost
    - Gradiant Boosting
    - XgBoost

## Voting Classifier
1. Hard
    - Mean/Average/Median (Regression) & Majority (classifier) of result
    
2. Soft
    - result with percentage

## XbBoost will be used to do hyperParameter optimization



## DNA Sequencing : split DNA data (big string) into specific numbers of char

# Life cycle of DS

1. Data Gathering
    - Web Scraping
    - 3rd party api's

2. Feature engineering
    - Handle NaN
    - Handle Imbalance
    - Remoise Noise
    - Format the data
    - Clean the data
    - Normalization
    - Handel categorical values
    
3. Feature(Column) Selection
    - Heat Map
    - Pearson corrision
    - extra tree classifier
    
4. Model Creation
    - Select the right model
    - Hyper parameter optimization/tunning
 
5. Test the Model

## Normalization (required when equidian distance is calculated, not required in decision tree) 
1. Scalar
```
                X - Xmean
ScalarValue = ------------
                 Xstd
```

2. MinMax
```
                 X - Xmin
minMax Value =  -----------
                 Xmax - Xmin
```



```
y = mx + c
c = intercept
m = slope
x = independent feature
y = dependent feature


c = y - mx

m = r * (SdY / SdX)

     1
r = ---------------- * (Sum of (Xi - Xm) * (Yi - Ym))
    (n-1)(SdY * SdX)
    
SdY = standard devision of Y
Ym = Y mean
Xm = X mean

                                  1
standard devision X = sqr of ( ---------- * Sum of (Xi - Xm))
                                (n-1)
```

## how to find outlier
1. box plot
2. scatter plot
3. Z-Score
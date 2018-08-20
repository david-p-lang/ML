# ML
Machine Learning

I am using Apples MLLogisticRegressionClassifier to complete Kaggle's Titanic Survival - Classification Voting
 competition.
 
 Logistic regression:
--------------------------------------------------------
Number of examples          : 714
Number of classes           : 2
Number of feature columns   : 11
Number of unpacked features : 11
Number of coefficients      : 1399
Starting Accelerated Gradient (FISTA)
--------------------------------------------------------
Tuning step size. First iteration could take longer than subsequent iterations.
+-----------+----------+-----------+--------------+-------------------+---------------------+
| Iteration | Passes   | Step size | Elapsed Time | Training Accuracy | Validation Accuracy |
+-----------+----------+-----------+--------------+-------------------+---------------------+
| 0         | 1        | 4.000000  | 0.000698     | 0.406162          | 0.406162            |
| 1         | 2        | 0.001804  | 0.024186     | 0.963585          | 0.963585            |
| 2         | 3        | 0.001804  | 0.027441     | 0.997199          | 0.997199            |
| 3         | 4        | 0.001804  | 0.031380     | 1.000000          | 1.000000            |
| 4         | 5        | 0.001203  | 0.035181     | 1.000000          | 1.000000            |
| 5         | 6        | 0.001203  | 0.038074     | 1.000000          | 1.000000            |
| 10        | 11       | 0.001203  | 0.053202     | 1.000000          | 1.000000            |
| 50        | 51       | 0.001203  | 0.177558     | 1.000000          | 1.000000            |
| 96        | 97       | 0.001203  | 0.317081     | 1.000000          | 1.000000            |
+-----------+----------+-----------+--------------+-------------------+---------------------+
SUCCESS: Optimal solution found.

----------------------------------
Number of examples: 714
Number of classes: 2
Accuracy: 100.00%

******CONFUSION MATRIX******
----------------------------------
True\Pred 0    1    
0         424  0    
1         0    290  

******PRECISION RECALL******
----------------------------------
Class Precision(%)   Recall(%)      
0     100.00         100.00         
1     100.00         100.00         



Columns:
    actual_count	integer
    class	integer
    missed_predicting_this	integer
    precision	float
    predicted_correctly	integer
    predicted_this_incorrectly	integer
    recall	float
Rows: 2
Data:
+----------------+----------------+------------------------+----------------+---------------------+
| actual_count   | class          | missed_predicting_this | precision      | predicted_correctly |
+----------------+----------------+------------------------+----------------+---------------------+
| 266            | 0              | 0                      | 1              | 266                 |
| 152            | 1              | 0                      | 1              | 152                 |
+----------------+----------------+------------------------+----------------+---------------------+
+----------------------------+----------------+
| predicted_this_incorrectly | recall         |
+----------------------------+----------------+
| 0                          | 1              |
| 0                          | 1              |
+----------------------------+----------------+
[2 rows x 7 columns]

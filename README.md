# apriori-algorithm
The Apriori algorithm detects frequent subsets given a dataset of association rules. 

This Python 3 implementation first prompts the user for the minimum support threshold to be used in the Apriori algorithm. For example, if the minimum support was 3, then on subsets with a support of 3 or higher are included.

## Using the script
Here is an example using the provided dataset and a minimum support of 6:
```
$ python apriori.py 
What min. support do you want to use? 
6

**** Apriori with minSupport = 6 ****

Sets:

frozenset(['a'])
frozenset(['b'])
frozenset(['c'])
frozenset(['a', 'b'])
frozenset(['a', 'c'])
frozenset(['c', 'b'])
frozenset(['a', 'c', 'b'])

Counts:

(frozenset(['a', 'c', 'b']), 3)
(frozenset(['d']), 5)
(frozenset(['b']), 7)
(frozenset(['a']), 8)
(frozenset(['e']), 3)
(frozenset(['c', 'b']), 5)
(frozenset(['a', 'c']), 4)
(frozenset(['c']), 6)
(frozenset(['a', 'b']), 5)
```
## Changing dataset to use with your own data
The given data set is named 'Dataset-apriori.txt'. To use your own data you should use a csv format, then you just have to change line 58 in 'apriori.py' to reflect your own file name:
```python
dataSetFilename = 'Dataset-apriori.txt'
```



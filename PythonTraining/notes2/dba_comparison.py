''' 1970 Dr E F Codd:  Relational Databases
SQL -> DBA

PriceRange
----------
* symbol    TEXT(5)
  low       REAL
  high      REAL
  midpoint  REAL

SELECT symbol, low, midpoint, high
FROM PriceRange
WHERE midpoint BETWEEN 26 and 29;

Virtues:  Easy to query
Vices:    Wastes storage space and risks data inconsistency

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

PriceRange
----------
* symbol    TEXT(5)
  low       REAL
  high      REAL

SELECT symbol, low, (low + high) / 2 AS midpoint, high
FROM PriceRange
WHERE (low + high) / 2 AS midpoint BETWEEN 26 and 29;

Virtues:   Efficient use of space and reduced risk of inconsistency
Vice:      Hard to query

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

PriceRangeInternal
------------------
* symbol    TEXT(5)
  low       REAL
  high      REAL

CREATE VIEW PriceRange
SELECT symbol, low, (low + high) / 2 AS midpoint, high
FROM PriceRangeInternal;

SELECT symbol, low, midpoint, high
FROM PriceRange
WHERE midpoint BETWEEN 26 and 29;

Virtues:   Efficient use of space and reduced risk of inconsistency
           and easy to query
'''

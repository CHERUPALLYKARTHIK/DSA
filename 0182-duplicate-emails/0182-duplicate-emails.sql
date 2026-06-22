# Write your MySQL query statement below
select email as Email
from Person
Group By email
having count(*)>1;
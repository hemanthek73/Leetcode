# Write your MySQL query statement below
select Email from
(select Email,count(Email) as c 
from Person
group by Email) as temp
where c>1
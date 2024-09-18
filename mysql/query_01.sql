use churn_db;
create table customer_join as
select customer_master.customer_id, customer_master.name, 
	   customer_master.class, customer_master.gender, 
       customer_master.start_date, customer_master.end_date,
       customer_master.campaign_id, customer_master.is_deleted,
       class_master.class_name, class_master.price 
from customer_master
left join class_master on customer_master.class = class_master.class;

select * from customer_join;

select * 
from customer_join
left join campaign_master on customer_join.campaign_id = campaign_master.campaign_id;

alter table customer_join
add column campaign_name varchar(20) not null;

SET SQL_SAFE_UPDATES = 0;
update customer_join
set campaign_name = (SELECT campaign_name FROM campaign_master WHERE customer_join.campaign_id = campaign_master.campaign_id)
WHERE campaign_id IS NOT NULL;
SET SQL_SAFE_UPDATES = 1;

select * from customer_join;

select * from customer_join2;
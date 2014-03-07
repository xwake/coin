update django_cron_cron set executing = 0 where 1=1;
--create table blog_urlresult_bak as select * from blog_urlresult;
--delete from django_cron_job
select * from proxier where active = 1;
--delete from proxier;
--delete from blog_urlresult where id > 134;
--select * from proxier where time_checked < strftime('%s','now') - 86400
--create table blog_sourcelink_bak as select * from blog_sourcelink;
/*insert into blog_sourcelink
select a.*,1 from blog_sourcelink_bak a;*/
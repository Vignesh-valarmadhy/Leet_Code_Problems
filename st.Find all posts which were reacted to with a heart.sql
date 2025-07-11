-- Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

-- Tables
-- facebook_reactions
-- facebook_posts
-- More about this question
-- Hints
-- Expected Output
-- facebook_reactions
-- Preview
-- poster	friend	reaction	date_day	post_id
-- 2	1	like	1	0
-- 2	6	like	1	0
-- 1	2	like	1	1
-- 1	3	heart	1	1
-- 1	4	like	1	1
-- 1	5	heart	1	1
-- 1	6	like	1	1
-- 2	1	like	2	2
-- 2	6	like	2	2
-- 1	2	like	2	3
-- 1	3	like	2	3
-- 1	4	like	2	3
-- 1	5	like	2	3
-- 1	6	like	2	3
-- 2	1	laugh	1	0
-- 2	6	laugh	1	1
-- 1	2	laugh	1	0
-- 1	3	laugh	1	3
-- 1	4	laugh	1	4
-- date_day:
-- int
-- friend:
-- bigint
-- post_id:
-- bigint
-- poster:
-- bigint
-- reaction:
-- text
-- facebook_posts
-- Preview
-- post_id	poster	post_text	post_keywords	post_date
-- 0	2	The Lakers game from last night was great.	[basketball,lakers,nba]	2019-01-01
-- 1	1	Lebron James is top class.	[basketball,lebron_james,nba]	2019-01-02
-- 2	2	Asparagus tastes OK.	[asparagus,food]	2019-01-01
-- 3	1	Spaghetti is an Italian food.	[spaghetti,food]	2019-01-02
-- 4	3	User 3 is not sharing interests	[#spam#]	2019-01-01
-- 5	3	User 3 posts SPAM content a lot	[#spam#]	2019-01-02
-- post_date:
-- date
-- post_id:
-- bigint
-- post_keywords:
-- text
-- post_text:
-- text
-- poster:
-- bigint


select distinct fp. * 

from facebook_reactions fr
JOIN facebook_posts fp
ON fr.post_id = fp.post_id
where fr.reaction = 'like';
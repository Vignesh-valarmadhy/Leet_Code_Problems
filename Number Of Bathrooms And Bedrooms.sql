-- Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

select 
city, property_type, 
avg(cast(bathrooms as float)),
avg(cast(bedrooms as float))
from airbnb_search_details
group by city , property_type;
select r.name, r.id from recipe as r
join recipes as rs on r.id = rs.recipe_id
join my_food as mf on mf.fk_ingredient_id = rs.ingredient_id
group by (r.name, r.id)
having count(mf.fk_ingredient_id) = 
(Select ic.count from ingredient_count as ic where r.id=ic.recipe_id)
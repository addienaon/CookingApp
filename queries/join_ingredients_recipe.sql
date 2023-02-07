select r.name, r.id, i.name from recipe as r
join recipes as rs on r.id = rs.recipe_id
join ingredient as i on i.id = rs.ingredient_id
where r.id = 1451

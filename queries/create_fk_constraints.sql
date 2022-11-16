CREATE TABLE recipees(
	recipee_id INT,
	CONSTRAINT fk_recipee
		FOREIGN KEY(recipee_id)
			REFERENCES recipee(id),
	ingredient_id INT,
	CONSTRAINT fk_ingredient
		FOREIGN KEY(ingredient_id)
			REFERENCES ingredient(id),
	amount INT,
	unit_id INT,
	CONSTRAINT fk_unit
		FOREIGN KEY(unit_id)
			REFERENCES unit(id)
);
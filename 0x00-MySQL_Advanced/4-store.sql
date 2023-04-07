-- creates  trigger that decreases the qty of an item after adding a new order
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;

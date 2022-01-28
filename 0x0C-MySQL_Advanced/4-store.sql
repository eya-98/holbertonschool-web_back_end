-- creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER remove_item
AFTER INSERT ON orders
FOR EACH ROW
    UPDATE items SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;
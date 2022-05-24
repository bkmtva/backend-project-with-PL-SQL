--jоличество продуктов
set serveroutput on;

CREATE OR REPLACE TRIGGER update_available_units 
    AFTER INSERT or UPDATE ON poll_productshoppingcart
    FOR EACH ROW DECLARE product_id_var integer; 
        quantity_var INTEGER; 

    BEGIN 
    product_id_var := :new.item_id;

            SELECT poll_product.count INTO quantity_var FROM poll_product 
            WHERE id = product_id_var; 
            IF quantity_var >= 2 and :new.quantity > :old.quantity
                THEN UPDATE poll_product SET poll_product.count = poll_product.count - 1
                WHERE id = product_id_var; 
                DBMS_OUTPUT.PUT_LINE('decriased');
            ELSIF quantity_var >= 2 and :new.quantity < :old.quantity
                THEN UPDATE poll_product SET poll_product.count = poll_product.count + 1 
                WHERE id = product_id_var; 
                DBMS_OUTPUT.PUT_LINE('inc');
            ELSIF quantity_var = 1 
                THEN UPDATE poll_product SET poll_product.count = 0 
                WHERE id = product_id_var; 
                DBMS_OUTPUT.PUT_LINE('fref');
            END IF; 
END;



CREATE OR REPLACE TRIGGER del_update_available_units 
    AFTER delete ON poll_productshoppingcart
    FOR EACH ROW DECLARE product_id_var INTEGER; 
        quantity_var INTEGER;  
    BEGIN
    product_id_var := :old.item_id;

            SELECT poll_product.count INTO quantity_var FROM poll_product 
            WHERE id = product_id_var; 
            IF quantity_var >= 1 
                THEN UPDATE poll_product SET poll_product.count = poll_product.count + :old.quantity 
                WHERE id = product_id_var; 
            ELSIF quantity_var = 0
                THEN UPDATE poll_product SET poll_product.count = :old.quantity 
                WHERE id = product_id_var; 
            END IF; 

END;


CREATE OR REPLACE TRIGGER insert_available_units 
    AFTER insert ON poll_productshoppingcart
    FOR EACH ROW DECLARE product_id_var INTEGER; 
        quantity_var INTEGER; 

    BEGIN
    product_id_var := :new.item_id;
    
             UPDATE poll_product SET poll_product.count = poll_product.count - 1
             WHERE id = product_id_var; 
           
        

END;

--добавление продукта в дискпродакт
CREATE OR REPLACE TRIGGER update_poll_discproduct
    AFTER INSERT ON poll_product
    FOR EACH ROW 
    DECLARE 
    p_id_var NVARCHAR2(100 CHAR);
    nob_disc_price_var NUMBER(9,2);
    disc_price NUMBER(9,2);
    begin
    insert into poll_discproduct(p_id, nob_disc_price, disc_price) Values (:new.id, :new.p_price, :new.p_price);
    
    end;
    
--подстчет количества продуктов в каждой категории
Create or replace trigger countCategory
after insert on poll_product 
declare
prod_id number;
category_id number;
p_id number;
begin
    select max(id) into prod_id from poll_product;
    select cat_id into category_id from poll_product where id = prod_id;
        update poll_category set c_count = c_count + 1 where id = category_id;
--    select id into p_id from poll_product where id = prod_id;
--        update poll_product set poll_product.count = poll_product.count + 1 where id = prod_id;
end;






--working with archive




Create or replace trigger MinusCountCategory
after insert on archive 
declare
prod_id number;
category_id number;

begin
    select max(item_id) into prod_id from users_archive1;
    select a_prodduct_category into category_id from archive where item_id = prod_id;
        update poll_category set c_count = c_count - 1 where id = category_id;
end;
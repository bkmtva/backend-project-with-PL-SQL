SET SERVEROUTPUT ON;

--скидка
CREATE or replace procedure discount
AS
    Cursor c1 is Select id, p_price,p_price, p_time_create from poll_product;
    disc_var NUMBER(9,2);
    nob_var number(9,2);
    pro_id NUMBER(19,0);
    p_time_create_var TIMESTAMP(6);
Begin
OPEN c1;
        LOOP
            FETCH c1 INTO pro_id, disc_var, nob_var, p_time_create_var;
            EXIT WHEN c1%NOTFOUND;
            
            if disc_var = nob_var AND (trunc(sysdate)-trunc(p_time_create_var)) >= 10 Then
            update poll_product SET p_price = disc_var * (20/100) where id = pro_id;
            update poll_discproduct SET disc_price = disc_var * (20/100) where id = pro_id;
            p_time_create_var := p_time_create_var + 10;
            
        else
        null;
        end if;  
        END LOOP;
        
    CLOSE c1;

   COMMIT;
    
        
end;


begin
discount;
end;






CREATE OR REPLACE PROCEDURE ARCHIVE_WRITER IS
    
   Cursor c1 is Select quantity, item_id from poll_productshoppingcart;
    quantity_var number(11,0);
    item_id_var NUMBER(19,0);

Begin
OPEN c1;
        
     LOOP
            FETCH c1 INTO quantity_var, item_id_var;
            EXIT WHEN c1%NOTFOUND;
            INSERT INTO 
                users_archive1(quantity, item_id) 
                values(quantity_var, item_id_var);
        end loop;
        close c1;
        DELETE from poll_productshoppingcart;
        Delete from poll_shoppingcart;
        DELETE from poll_shoppingcart_items;
       
END;
































--CREATE OR REPLACE TRIGGER update_available_units 
--    AFTER INSERT or UPDATE ON poll_shoppingcart_items
--    FOR EACH ROW DECLARE product_id_var INTEGER; 
--        quantity_var INTEGER; 
--    CURSOR products_cur IS 
--    SELECT item_id FROM poll_productshoppingcart WHERE id = :new.id; 
--    BEGIN OPEN products_cur; 
--        LOOP FETCH products_cur INTO product_id_var;
--            EXIT WHEN products_cur%notfound; 
--            SELECT poll_product.count INTO quantity_var FROM poll_product 
--            WHERE id = product_id_var; 
--            IF quantity_var >= 2 
--                THEN UPDATE poll_product SET poll_product.count = poll_product.count - 1 
--                WHERE id = product_id_var; 
--            ELSIF quantity_var = 1 
--                THEN UPDATE poll_product SET poll_product.count = 0 
--                WHERE id = product_id_var; 
--            END IF; 
--        END LOOP; 
--    CLOSE products_cur;
--END;



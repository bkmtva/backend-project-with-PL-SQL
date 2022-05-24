--родукты который в дефиците
CREATE OR REPLACE FUNCTION ProductsInShortSupply
    RETURN NUMBER
    AS
        CURSOR prodquan
            IS
                SELECT poll_product.id, p_title, author_id, POLL_PRODUCT.count
                    FROM POLL_PRODUCT
                    WHERE poll_product.count < 10;
        id_var POLL_PRODUCT.ID%TYPE;
        p_title_var POLL_PRODUCT.p_title%TYPE;
        author_id_var POLL_PRODUCT.author_id%TYPE;
        count_var POLL_PRODUCT.count%TYPE;
        
        numOfProd NUMBER(9,2) := 0;
    BEGIN
        OPEN prodquan;
        DELETE FROM poll_shortsupply;
        LOOP
            FETCH prodquan INTO id_var, p_title_var, author_id_var, count_var;
            
                EXIT WHEN prodquan%NOTFOUND;
                
                INSERT INTO poll_shortsupply(id, s_p_title, s_count)
            VALUES(id_var, p_title_var, count_var);
            DBMS_OUTPUT.PUT_LINE('PRODUCT ID: ' || id_var || ' NAME: ' || p_title_var || ' QUANTITY IN SHORT SUPPLY: ' || count_var);
            numOfProd := numOfProd + 1;
            

        END LOOP;
        
        CLOSE prodquan;
        
        IF numOfProd = 0 THEN
            DBMS_OUTPUT.PUT_LINE('No ProductsInShortSupply');
            
        END IF;
        
        
        COMMIT;
        DBMS_OUTPUT.PUT_LINE(numOfProd);
        RETURN numOfProd;
    END;
    
    
CREATE OR REPLACE FUNCTION in_dollar(in_tenge in number)
    RETURN NUMBER is
    dollar_price number;
    begin
    dollar_price := in_tenge / 432;
    return dollar_price ;
    end;
    
CREATE OR REPLACE FUNCTION in_ruble(in_tenge in number)
    RETURN NUMBER is
    ruble_price number;
    begin
    ruble_price := in_tenge / 6.61;
    return ruble_price ;
    end;
  declare 
  num Number;
  begin 
  num:=60;
  in_dollar(num);
  end;
  
declare
c number;

BEGIN
c:=ProductsInShortSupply();
dbms_output.put_line(c);
end;    
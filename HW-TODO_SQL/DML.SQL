-- INSER SCRIPT - SINGLE VALUE
-- INSERT/SELECT/UPDATE/DELETE

INSERT INTO
    public.tasks
        (title, done)
	VALUES 
        ('Another Task', false)
        ;

-- INSER SCRIPT - MULTI VALUE
INSERT INTO
    public.tasks
        (title, done)
	VALUES 
        ('Another GOOD Task A', false),
        ('Another GOOD Task B', true),
        ('Another GOOD Task C', false),
        ('Another GOOD Task D', true),
        ('Another GOOD Task E', false)
        ;

-- SELECT STANDART
SELECT title, done
	FROM public.tasks;

-- <OPERATION > table/col WHERE <CONDITION>

-- SELECT + WHERE
SELECT title, done
	FROM public.tasks
    WHERE done = true;

SELECT title
	FROM public.tasks
    WHERE title = 'Another GOOD Task E';

SELECT title, done
	FROM public.tasks
    WHERE title LIKE '%GOOD%';


SELECT title, done
	FROM public.tasks
    WHERE title LIKE 'Another%' 
        AND done=false  
        ;

-- UPDATE STANDART
UPDATE public.tasks
	SET  done=false
	WHERE title = 'Another GOOD Task E';

UPDATE public.tasks
	SET  done=false
	WHERE done = true;

-- SELECT + AGGREGATION
SELECT count(title)
	FROM public.tasks;

SELECT MAX(title)
	FROM public.tasks;

SELECT MIN(title)
	FROM public.tasks;

SELECT count(title)
	FROM public.tasks
    WHERE done = false;
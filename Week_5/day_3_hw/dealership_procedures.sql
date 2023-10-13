DELIMITER // 
CREATE PROCEDURE next_service(
	IN employee_id INT,
	IN serviced_id INT,
	IN work_done VARCHAR(255)
)
BEGIN
	INSERT INTO service_records
	VALUES(
	serviced_id,
	employee_id,
	work_done
	)
	UPDATE service_dept
	SET service_date = NOW()
	WHERE service_dept.service_id = serviced_id;

COMMIT;
END // 


CALL next_service(201, 2201, 'new wiper blades');



DELIMITER // 
CREATE PROCEDURE new_cust(
	IN owner_name VARCHAR(255),
	IN contact_info VARCHAR(255),
	IN billing_info VARCHAR(255)
)
BEGIN
	INSERT INTO owners
	VALUES(
		(SELECT MAX(owner_id) from owners o) +1 ,
		contact_info,
		billing_info,
		owner_name
		);
COMMIT;
END// 

CALL new_cust('Billy Bones', '555-234-6870', '647 Shipman Blvd');
CALL new_cust('Bowie Davidsonella', '555-777-5974', '19495 Owlton St');



DELIMITER // 
CREATE PROCEDURE new_car(
	IN owner_id INT,
	IN make_model VARCHAR(60),
	IN milage INT
)
BEGIN
	INSERT INTO vehicles
	VALUES(
		(SELECT MAX(owner_id) from owners o) +1 
		owner_id,
		make_model,
		milage
		);

COMMIT;
END // 
 
 Provding Bank Detail
===================
REST API service that can provide:

1. Give a bank branch IFSC code, get branch details
2. Give a bank name and city, gets details of all branches of the bank in the city


Demo For IFSC code- 
```bash
https://dudley-poutine-54936.herokuapp.com/api/getbank/ABHY0065002 
```
Demo For City and Bank - 
```bash
https://dudley-poutine-54936.herokuapp.com/api/bankdetail/MUMBAI/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED
```

Git Clone:
```bash
https://github.com/imdad000/Fyle_Bank_API
```

Database which is to be created and then make a table consists of:
```bash
CREATE TABLE banks (
    name character varying(49),
    id bigint NOT NULL
);

CREATE TABLE branches (
    ifsc character varying(11) NOT NULL,
    bank_id bigint,
    branch character varying(74),
    address character varying(195),
    city character varying(50),
    district character varying(50),
    state character varying(26)
);
```
Install requirements using:
```bash
pip install .
```

-- Create database & tables.
-- docker image handles creating database and public and public schemas 
-- as well as assigning them as default.

-- set up environment variables.
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


-- create enum for status codes.
CREATE type public.status_code as enum ('enabled', 'disabled', 'suspended');

-- create table to store campaign budget data.
create table public.employee(
	id int GENERATED ALWAYS AS IDENTITY,
	full_name text NOT NULL,
	status_code status_code NOT NULL DEFAULT 'enabled',
	CONSTRAINT pk_employee_id PRIMARY KEY (id)
);
